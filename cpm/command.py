import argparse

class Command(object):
    name = ""
    description = ""
    aliases = []

    def __init__(self, parser):
        self.parser = parser
        self.initializeParser(parser)
        self.parser.set_defaults(cmd_callback=self.run)

    def initializeParser(self, parser):
        raise NotImplementedError( "Should have implemented this" )
    
    def run(self, options, args):
        raise NotImplementedError( "Should have implemented this" )
