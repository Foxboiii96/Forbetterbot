import toml

try:
    with open("config.toml") as f:
        _config = toml.load(f)
except FileNotFoundError:
    raise FileNotFoundError("config.toml not found. Please create one from config.example.toml.")

DISCORD_TOKEN = _config.get("bot", {}).get("token")

if not DISCORD_TOKEN:
    raise ValueError("`token` not found in config.toml. Please add it under the `[bot]` section.")
