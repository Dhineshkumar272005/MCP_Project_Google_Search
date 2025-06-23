from mcp.server.fastmcp import FastMCP
import webbrowser
import urllib.parse

mcp =FastMCP("Google search")

@mcp.tool()
def open_google_search(query:str):
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={encoded_query}"
    webbrowser.open(url)

@mcp.resource("greeting://{name}")
def get_greeting(name:str) -> str:
    return f"Hello {name}!"

