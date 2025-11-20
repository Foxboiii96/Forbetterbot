import lightbulb

loader = lightbulb.Loader("ping")


@loader.command
class Ping(
    lightbulb.SlashCommand,
    name="ping",
    description="Checks if the bot is alive.",
):
    @lightbulb.invoke
    async def callback(self, ctx: lightbulb.Context) -> None:
        await ctx.respond("pong!")
