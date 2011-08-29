from ci.plugins.base import Plugin, Builder

class ToxBuilder(Builder):
    name = 'tox'

class ToxPlugin(Plugin):
    def get_builders(self):
        return [ToxBuilder]
