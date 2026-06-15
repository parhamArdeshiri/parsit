from abstracted.abstracted_factory import AbstractedBaseFactory

from parsers.toml_parser import TOMLParser

class TOMLParserFactory(AbstractedBaseFactory):
    
    def create_parser(self):
        return TOMLParser()
    