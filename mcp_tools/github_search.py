import httpx
from mcp.types import CallToolResult, TextResourceContents
from backend_models.models import SearchReposArgs

DEFAULT_WIDGET_URI = "ui://widget/github-search.html"

def create_github_search_tool(mcp, include_ui=True, widget_uri=DEFAULT_WIDGET_URI):
    
    async def github_search(query: str, language: str = None, max_results: int = 5):
        args = SearchReposArgs(query=query, language=language, max_results=max_results)
        url = f"https://api.github.com/search/repositories?q={args.query}"
        if args.language:
            url += f"+language:{args.language}"
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
            items = resp.json().get("items", [])[:args.max_results]
        structured = [
            {"name": i["name"], "full_name": i["full_name"], "url": i["html_url"], "stars": i["stargazers_count"]}
            for i in items
        ]
        return CallToolResult(
            structuredContent={"repos": structured, "result_count": len(structured)},
            _meta={
                "openai.com/widget": "github-search-widget",
                "openai/outputTemplate": widget_uri,
                "openai/toolInvocation/invoking": "Searching GitHub repos...",
                "openai/toolInvocation/invoked": "Here are your GitHub results."
            }
        )

    if include_ui:
        @mcp.resource(widget_uri)
        def get_widget_ui() -> str:
            return TextResourceContents(
                uri=widget_uri,
                mimeType="text/html",
                text="<div>React GitHub Search Widget Goes Here</div>"
            )

    return github_search
