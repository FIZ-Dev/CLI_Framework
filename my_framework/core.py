import argparse

class MyFramework:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="MyFramework CLI")
        self.commands = {}

    def add_command(self, name, func):
        self.commands[name] = func
        self.parser.add_argument(f"--{name}", action="store_true", help=f"Run {name} command")

    def run(self):
        args = vars(self.parser.parse_args())
        for command, active in args.items():
            if active and command in self.commands:
                self.commands[command]()
