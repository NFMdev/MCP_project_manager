from mcp.server.fastmcp import tool
from llm.claude_wrapper import generate_project_code

@tool()
def generate_code(prompt: str, project_name: str) -> dict:
    files = generate_project_code(prompt)
    return {"project": project_name, "files": files}