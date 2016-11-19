from command import Command

class ConfigCommand(Command):
    name = "config"
    description = "Config project."

    def initializeParser(self, parser):
        pass
    
    def run(self, options, args):
        print('config')
        pass