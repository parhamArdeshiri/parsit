from factories.csv_factory import CSVParserFactory
from factories.xml_factory import XMLParserFactory
from factories.yml_factory import YMLParserFactory

factories = {
    "csv": CSVParserFactory(),
    "xml": XMLParserFactory(),
    "yml": YMLParserFactory()
}
