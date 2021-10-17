from kindle.models import DBHighlight, DBBook
from kindle_clippings_parser.models import Highlight


def dao_insert_highlight(book: DBBook, highlight_data: Highlight):
    highlights_query_set = dao_get_highlights_by_book_and_text(book, highlight_data)
    if highlights_query_set.count() < 1:
        db_highlight = (DBHighlight(
            book_id=book,
            location=highlight_data.location,
            relative_page_number=highlight_data.relative_page_number,
            text=highlight_data.text,
            highlight_date=highlight_data.highlight_date,
        ))
        db_highlight.save()
        return db_highlight

    return highlights_query_set.first()

def dao_get_highlights_by_book_and_text(book: DBBook, highlight_data: Highlight):
    return (DBHighlight.objects
            .filter(book_id=book, text=highlight_data.text)
    )

def dao_get_highlights():
    return DBHighlight.objects.all()

def dao_get_highlights_by_book_language(language_code: str):
    return (DBHighlight.objects
            .filter(book_id__language_code=language_code)
    )


