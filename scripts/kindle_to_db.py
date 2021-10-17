from kindle_clippings_parser import KindleClippingsParser
from kindle_clippings_parser.models import Book, Highlight, KindleClippings, KindleClippingsParserConfig

def get_kindle_highlights():
    config = KindleClippingsParserConfig(True, 'PST8PDT')
    parser = KindleClippingsParser(config)
    book_highlights = parser.parse_kindle_clippings('/Users/andrew/workspace/kindle-clippings-parser/example_clippings.txt')
    return book_highlights

