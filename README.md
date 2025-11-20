# Forbetterbot - A Python Discord Bot Template

This is a fast, user-friendly, and plugin-ready Discord bot template built with Python and the `hikari` library. It's designed to be easily extensible, allowing you to create your own commands and features with minimal effort.

## Features

- **Fast and Modern:** Built on top of `hikari`, a modern and high-performance Discord API wrapper.
- **Plugin-Ready:** Easily extend the bot's functionality by creating new plugins in the `forbetter/plugins` directory.
- **Easy to Use:** The bot is designed to be easy to set up and use, even for beginners.
- **Secure:** The bot's token is loaded from a `config.toml` file, so you don't have to hardcode it in your code.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- A Discord bot token. You can get one from the [Discord Developer Portal](https://discord.com/developers/applications).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/forbetterbot.git
   cd forbetterbot
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   For development, you can install the development dependencies with:
   ```bash
   pip install -r requirements-dev.txt
   ```

3. **Configure the bot's token:**
   - Rename `config.example.toml` to `config.toml`.
   - Open `config.toml` and replace `"YOUR_DISCORD_TOKEN_HERE"` with your Discord bot token.

### Running the Bot

To start the bot, run the following command in the root directory of the project:

```bash
python -m forbetter
```

## Creating a Plugin

To make creating new plugins easier, you can use the `create_plugin.py` script. This will automatically generate a new plugin file with a basic command template.

```bash
python create_plugin.py your_plugin_name
```

This will create a new file at `forbetter/plugins/your_plugin_name.py` with a simple command.

## Testing

This project uses `pytest` for testing. To run the tests, use the following command:

```bash
PYTHONPATH=. pytest
```

## Linting and Formatting

This project uses `flake8` for linting and `black` for code formatting. To run the linter and formatter, use the following commands:

```bash
flake8 .
black .
```

## Docker

This project includes a `Dockerfile` to make it easy to build and run the bot in a containerized environment. To build the Docker image, use the following command:

```bash
docker build -t forbetterbot .
```

To run the bot in a Docker container, use the following command:

```bash
docker run -d -v $(pwd)/config.toml:/app/config.toml forbetterbot
```
