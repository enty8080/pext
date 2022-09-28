"""
This plugin requires HatSploit: https://hatsploit.com
Current source: https://github.com/EntySec/HatSploit
"""

from hatsploit.lib.plugin import Plugin


class HatSploitPlugin(Plugin):
    details = {
        'Name': "Pwny pext Plugin",
        'Plugin': "pext",
        'Authors': [
            'Ivan Nikolsky (enty8080) - plugin developer',
        ],
        'Description': "Plugin called pext for testing.",
    }

    commands = {
        'pext': {
            'test': {
                'Description': "Test.",
                'Usage': "test",
                'MinArgs': 0,
            }
        }
    }

    def test(self, argc, argv):
        pass

    def load(self):
        pass
