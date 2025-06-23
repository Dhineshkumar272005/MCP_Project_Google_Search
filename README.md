# MCP_Project_Google_Search
---

# MCP Google Search Tool

This project provides a simple Python server using the MCP (Modular Command Platform) framework to expose tools for Google searching and greeting users. It demonstrates how to create custom MCP tools and resources, including opening a Google search in your browser and generating personalized greetings.

## Features

- **Google Search Tool:**  
  Instantly open a Google search for any query from your Python code.
- **Greeting Resource:**  
  Generate a personalized greeting for any name.

## File Structure

```
.
├── google_mcp_server.py
└── requirement.txt
```

## Requirements

- Python 3.7+
- MCP framework (must provide `mcp.server.fastmcp`)
- Standard Python libraries: `webbrowser`, `urllib.parse`

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Dhineshkumar272005/MCP_Project_Google_Search.git
   cd MCP_Project_Google_Search
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirement.txt
   ```
   > **Note:**  
   Ensure that the MCP framework is available. If it is a private or custom package, follow your organization’s installation instructions.

## Installation in Claude Desktop

  ```sh
  {
    "mcpServers": {
      "google_mcp_server":{
        "command": "uv",
        "args": [
          "run",
          "--with",
          "mcp[cli]",
          "mcp",
          "run",
          "path\to\your\location\google_mcp_server.py"
        ]
      }
    }
  }
  ```
  > **Note:**
  It should be placed in the `claude_desktop_config.json `

## Usage

### 1. Start the Server

Run the Python file:
```sh
python google_mcp_server.py
```

### 2. Available Tools

#### a. Google Search Tool

- **Function:** `open_google_search(query: str)`
- **Description:** Opens the default web browser and performs a Google search for the provided query.
- **Example:**
  ```python
  open_google_search("Python programming")
  ```
  This will open your browser to:  
  `https://www.google.com/search?q=Python+programming`

#### b. Greeting Resource

- **Function:** `get_greeting(name: str) -> str`
- **Description:** Returns a personalized greeting for the given name.
- **Example:**
  ```python
  get_greeting("Alice")
  # Output: "Hello Alice!"
  ```

## Code Overview

- **`fastmcp`**: Initializes the MCP server with the name "Google search".
- **`@mcp.tool()`**: Decorator to register a function as an MCP tool.
- **`@mcp.resource()`**: Decorator to register a function as an MCP resource.

## Troubleshooting

- **ModuleNotFoundError:**  
  If you see an error about `mcp.server.fastmcp`, ensure the MCP framework is installed and accessible in your Python environment.

- **Web Browser Not Opening:**  
  The `webbrowser.open()` function uses your system’s default browser. If nothing happens, check your system’s browser settings.

- **Typos in Decorators:**  
  Ensure you use `@mcp.resource` (not `@mcp.reseource`) and the correct case for all imports and class names.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE) (or specify your license here)

---
