import os
import hikari
import lightbulb
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

bot = lightbulb.BotApp(token=os.environ["DISCORD_TOKEN"])

def load_plugins():
    for filename in os.listdir("forbetter/plugins"):
        if filename.endswith(".py") and not filename.startswith("_"):
            bot.load_extensions(f"forbetter.plugins.{filename[:-3]}")

@bot.listen(hikari.StartedEvent)
async def on_started(event: hikari.StartedEvent) -> None:
    print("Bot has started!")

if __name__ == "__main__":
    load_plugins()
    bot.run()
