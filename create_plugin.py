import os
import argparse

def create_plugin(name: str):
    plugin_path = os.path.join("forbetter", "plugins", f"{name}.py")
    if os.path.exists(plugin_path):
        print(f"Plugin '{name}' already exists.")
        return

    with open(plugin_path, "w") as f:
        f.write(
            f'''import lightbulb

loader = lightbulb.Loader("{name}")

@loader.command
class {name.capitalize()}(
    lightbulb.SlashCommand,
    name="{name}",
    description="A new command.",
):
    @lightbulb.invoke
    async def callback(self, ctx: lightbulb.Context) -> None:
        await ctx.respond("Command executed!")
'''
        )
    print(f"Plugin '{name}' created at {plugin_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new plugin.")
    parser.add_argument("name", type=str, help="The name of the plugin to create.")
    args = parser.parse_args()
    create_plugin(args.name)
