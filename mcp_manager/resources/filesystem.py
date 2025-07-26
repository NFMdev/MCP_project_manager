from mcp.server.fastmcp import resource
from pathlib import Path

BASE = Path("projects")

@resource("filesystem://{project}/{filename}")
def fs_read(project: str, filename: str) -> str:
    return (BASE / project / filename).read_text()

@resource("filesystem://{project}/{filename}", method="PUT")
def fs_write(project: str, filename: str, content: str) -> str:
    path = BASE / project / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return f"Written to {path}"