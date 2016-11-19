import argparse

class Command(object):
    def __init__(self, parser):
        self.parser = parser
        self.initializeParser(parser)
        self.parser.set_defaults(func=self.run)

    def initializeParser(self, parser):
        raise NotImplementedError( "Should have implemented this" )
    
    def run(self, options, args):
        raise NotImplementedError( "Should have implemented this" )
