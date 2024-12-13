class PluginManager:
    def __init__(self):
        self.plugins = {}

    def register(self, name, func):
        self.plugins[name] = func

    def execute(self, name):
        if name in self.plugins:
            self.plugins[name]()
        else:
            print(f"Plugin {name} not found.")
