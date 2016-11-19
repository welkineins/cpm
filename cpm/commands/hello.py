from command import Command

class HelloCommand(Command):
    name = "hello"
    description = "Say hello to your name."
    
    def initializeParser(self, parser):
        parser.add_argument('name', default='Jack')
    
    def run(self, options, args):
        print("hello " + args.name)