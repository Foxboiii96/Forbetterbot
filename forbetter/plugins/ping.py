import lightbulb

ping_plugin = lightbulb.Plugin("ping")

@ping_plugin.command
@lightbulb.command("ping", "Checks if the bot is alive.")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond("pong!")

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(ping_plugin)
