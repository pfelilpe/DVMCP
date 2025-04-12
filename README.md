# Damn Vulnerable MCP Server Demo

A simplier implementation of a Damn Vulnerable MCP Server that adds two or more numbers

## Overview
The MCP Server Demo is a demonstration of excessive agency that could lead to Remote Code Execution (RCE) if the MCP were running on an external server. 🛡️

## Features
- 🚀 Basic MCP server implementation.
- 📂 Demonstrates server functionality with `server.py`.

## Warning

⚠️ This project is a **vulnerable MCP server** designed to demonstrate how poor implementation practices can lead to security issues. It is intended for educational purposes only.

❌ **Do not use this project in production environments.**

## Prerequisites
- 🐍 Python 3.10 or higher.
- 💡 A virtual environment is recommended for managing dependencies.

## Installation
1. 📥 Clone the repository:
   ```bash
   git clone <repository-url>
   cd DVMCP
   ```

2. 📦 Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. ▶️ Link the MCP Server with Copilot:
   ```bash
   vscode://settings/mcp
   ```

2. Add the server configuration to the `settings.json` file in VS Code:

   ```json
   "servers": {
       "DVMCP": {
           "command": "uv",
           "args": [
               "run",
               "--with",
               "mcp[cli]",
               "mcp",
               "run",
               "/Users/pfelilpe/Documents/DVMCP/server.py"
           ],
           "env": {}
       }
   }
   ```

3. Click on **Start Server**.

4. Interact with Copilot in Agent mode, for example:
   ```
   1+1 with addition
   ```

5. Experiment with code injection to explore potential OS Injection vulnerabilities... 🕵️‍♂️

6. You can find a safer implementation of this simpler MCP at `/safe/server.py`. 🔒

## Adding MCP to Your Python Project

We recommend using `uv` to manage your Python projects. 🛠️

If you haven't created a `uv`-managed project yet, initialize one:

```bash
uv init mcp-server-demo
cd mcp-server-demo
```

Then add MCP to your project dependencies:

```bash
uv add "mcp[cli]"
```

Alternatively, for projects using `pip` for dependencies:

```bash
pip install "mcp[cli]"
```

## Running the Standalone MCP Development Tools

To run the `mcp` command with `uv`:

```bash
uv run mcp
```

## Project Structure
- `server.py`: 🖥️ Main server implementation.
- `pyproject.toml`: 📜 Project configuration file.
- `README.md`: 📖 Documentation for the project.
- `uv.lock`: 🔒 Lock file for dependencies.
- `__pycache__/`: 🗂️ Contains compiled Python files.

## Contributing
🤝 Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
📄 This project is licensed under the terms of the LICENSE file in the root directory.

## Created by pfelilpe

## Buy Me a Coffee
If you found this project helpful or interesting, consider buying me a coffee to support my work: ☕️

[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/pfelilpe)
