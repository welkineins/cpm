from command import Command

class CleanCommand(Command):
    name = "clean"
    description = "Clean project."

    def initializeParser(self, parser):
        pass
    
    def run(self, options, args):
        print('clean')
        pass