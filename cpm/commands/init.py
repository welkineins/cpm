from command import Command

class InitCommand(Command):
    name = "init"
    description = "Initialize project."

    def initializeParser(self, parser):
        pass
    
    def run(self, options, args):
        print('init')
        pass