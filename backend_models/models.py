from pydantic import BaseModel, Field
from typing import List, Optional

# Laptop Compare Tool Models
class CompareLaptopsArgs(BaseModel):
    laptop_names: List[str] = Field(..., description="List of laptop names to compare")

class Laptop(BaseModel):
    id: str
    name: str
    ram: int
    price: float

# GitHub Repo Search Tool Models
class SearchReposArgs(BaseModel):
    query: str
    language: Optional[str] = None
    max_results: int = 5

class RepoInfo(BaseModel):
    name: str
    full_name: str
    url: str
    stars: int
