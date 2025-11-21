from forbetter.plugins.ping import loader


def test_ping_command():
    assert len(loader._loadables) == 1
    ping_command = loader._loadables[0]._command
    assert ping_command._command_data.name == "ping"
    assert ping_command._command_data.description == "Checks if the bot is alive."
