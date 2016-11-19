from command import Command

class HelloCommand(Command):
    def initializeParser(self, parser):
        parser.add_argument('-v', '--version', action='version', version="3.x")
        parser.add_argument('-b')
    
    def run(self, options, args):
        print("hellooooo~~~~")
        print(args.b)