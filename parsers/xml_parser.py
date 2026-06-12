from abstracted.abstracted_parser import AbstractedBaseParser

from json2xml import json2xml
from json2xml.utils import readfromstring

import xmltodict

class XMLParser(AbstractedBaseParser):
    def to_json(self, input_data):
        output = xmltodict.parse(input_data)
        
        return output
        
    def from_json(self, input_data):
        output = json2xml.Json2xml(input_data, pretty=True).to_xml()
        
        return output
        