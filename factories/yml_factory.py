from abstracted.abstracted_factory import AbstractedBaseFactory

from parsers.yml_parser import YMLParser

class YMLParserFactory(AbstractedBaseFactory):
    def create_parser(self):
        return YMLParser()