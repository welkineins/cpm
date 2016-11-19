from command import Command

class UpdateCommand(Command):
    name = "update"
    description = "Update project."

    def initializeParser(self, parser):
        pass
    
    def run(self, options, args):
        print('update')
        pass