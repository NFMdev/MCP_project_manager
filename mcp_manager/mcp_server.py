from mcp.server.fastmcp import FastMCP
from tools.generate_code import generate_code
from tools.commit_code import commit_code
from tools.deploy_vercel import deploy_vercel

from resources.filesystem_provider import fs_read, fs_write

mcp = FastMCP("MCP-Server")

# Tools
mcp.register_tool(generate_code)
mcp.register_tool(commit_code)
mcp.register_tool(deploy_vercel)


# Resources
mcp.register_resource(fs_read)
mcp.register_resource(fs_write)

if __name__ == "__main__":
    mcp.run()
    print("MCP Server is running...")