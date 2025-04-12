# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("DVMCP Server", "1.0.0")


# Add an addition tool
@mcp.tool()
def addition(a):
    """Sum tool"""
    return eval(a) 
    
    # This is a simple example and should not be used in production due to security risks. 
    # In a real-world scenario, you should implement proper input validation and error handling.
    # For example:
    # try:
    #     numbers = map(float, a.split(","))
    #     return sum(numbers)       
    # except ValueError:
    #     return "Invalid input. Please provide a comma-separated list of numbers."

    # What if you try as input for the LLM connected to this MCPServer:
    #   print("Not safe, but it works")
    # What if you try:
    #   print(open('lol.txt','x').write())
    # It works? what other inputs could be used to exploit this? ...
    

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"