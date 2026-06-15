from factories.toml_factory import TOMLParserFactory
from factories.xml_factory import XMLParserFactory
from factories.yml_factory import YMLParserFactory

factories = {
    ".toml": TOMLParserFactory(),
    ".xml": XMLParserFactory(),
    ".yml": YMLParserFactory()
}
