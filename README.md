# MCP Tools Package

This is a **tool-only MCP package** for sharing reusable ChatGPT tools across multiple projects.

### Included Tools:
- Laptop Comparison Tool
- GitHub Search Tool

### Usage:
```python
from mcp_tools import create_laptop_compare_tool, create_github_search_tool
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("shared-tools")

laptop_tool, laptop_ui = create_laptop_compare_tool(mcp)
github_tool, github_ui = create_github_search_tool(mcp)
Installation:
Locally: uv install ./

Publish to private registry for team-wide use

yaml
Copy code

---

✅ **Key Features of this Package**
- Tools are **independent of server**: can be plugged into any MCP server.
- Shared models in `backend_models` allow consistent type contracts.
- Each tool can optionally serve its React widget via MCP.
- Ready for **local installation** or **private package registry** deployment.

---

If you want, I can **also write an example `project/` folder** that **plugs this `mcp_tools_package` into an MCP server** and runs it, showing **laptop compare + GitHub search live in one server**.  








