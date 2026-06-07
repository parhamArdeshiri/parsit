from abstracted.abstracted_factory import AbstractedBaseFactory

from parsers.xml_parser import XMLParser

class XMLParserFactory(AbstractedBaseFactory):
    
    def create_parser(self):
        return XMLParser()
    