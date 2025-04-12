# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("DVMCP Server", "1.0.0")


# Add an addition tool
@mcp.tool()
def addition(a):
    """Sum tool"""
    return eval(a)


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"