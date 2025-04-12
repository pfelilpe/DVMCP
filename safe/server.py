from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("MCP Safe Server", "1.0.0")


# Add an addition tool
@mcp.tool()
def safeaddition(a: str):
    """Sum tool"""
    try:
        numbers = map(float, a.split(","))
        return sum(numbers)
    except ValueError:
        return "Invalid input. Please provide a comma-separated list of numbers."


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
