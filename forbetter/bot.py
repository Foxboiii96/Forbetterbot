import os
import logging
import lightbulb
from forbetter import config

logging.basicConfig(level=logging.INFO)

bot = lightbulb.BotApp(token=config.DISCORD_TOKEN)


def load_plugins():
    plugins_dir = os.path.join(os.path.dirname(__file__), "plugins")
    for filename in os.listdir(plugins_dir):
        if filename.endswith(".py") and not filename.startswith("_"):
            try:
                bot.load_extensions(f"forbetter.plugins.{filename[:-3]}")
                logging.info(f"Loaded plugin {filename}")
            except Exception as e:
                logging.error(f"Failed to load plugin {filename}: {e}")


@bot.listen(lightbulb.LightbulbStartedEvent)
async def on_started(event: lightbulb.LightbulbStartedEvent) -> None:
    logging.info("Bot has started!")


@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    exception = event.exception.__cause__ or event.exception
    logging.error(f"Error in command '{event.context.command.name}': {exception}")
    await event.context.respond(
        "An unexpected error occurred. The developers have been notified."
    )


if __name__ == "__main__":
    load_plugins()
    bot.run()
