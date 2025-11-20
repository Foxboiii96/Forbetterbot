# Forbetterbot - A Python Discord Bot Template

This is a fast, user-friendly, and plugin-ready Discord bot template built with Python and the `hikari` library. It's designed to be easily extensible, allowing you to create your own commands and features with minimal effort.

## Features

- **Fast and Modern:** Built on top of `hikari`, a modern and high-performance Discord API wrapper.
- **Plugin-Ready:** Easily extend the bot's functionality by creating new plugins in the `forbetter/plugins` directory.
- **Easy to Use:** The bot is designed to be easy to set up and use, even for beginners.
- **Secure:** The bot's token is loaded from a `.env` file, so you don't have to hardcode it in your code.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- A Discord bot token. You can get one from the [Discord Developer Portal](https://discord.com/developers/applications).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/foxboiii96/forbetterbot.git
   cd forbetterbot
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the bot's token:**
   - Rename the `.env.example` file in the `config` directory to `.env`.
   - Open the `.env` file and paste your Discord bot token after `DISCORD_TOKEN=`.

### Running the Bot

To start the bot, run the following command in the root directory of the project:

```bash
python -m forbetter.bot
```

## Creating a Plugin

To create a new command, you can create a new Python file in the `forbetter/plugins` directory. The bot will automatically load it as a plugin.

Here's an example of a simple "hello" command:

```python
# forbetter/plugins/hello.py
import lightbulb

hello_plugin = lightbulb.Plugin("hello")

@hello_plugin.command
@lightbulb.command("hello", "Says hello to the user.")
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"Hello, {ctx.author.username}!")

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(hello_plugin)
```

The bot will automatically pick up the new command and make it available on Discord.
