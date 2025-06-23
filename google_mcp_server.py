from mcp.server.fastmcp import fastmcp
import webbrowser
import urllib.parse

mcp =fastmcp("Google search")

@mcp.tool()
def open_google_search(query:str):
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={encoded_query}"
    webbrowser.open(url)

@mcp.reseource("greeting://{name}")
def get_greeting(name:str) -> str:
    return f"Hello {name}!"

