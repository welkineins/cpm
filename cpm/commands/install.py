from command import Command

class InstallCommand(Command):
    name = "install"
    description = "Install project."

    def initializeParser(self, parser):
        pass
    
    def run(self, options, args):
        print('install')
        pass