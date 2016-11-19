from command import Command

class BuildCommand(Command):
    name = "build"
    description = "Build project."

    def initializeParser(self, parser):
        pass
    
    def run(self, options, args):
        print('build')
        pass