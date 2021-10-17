from collections import defaultdict
from kindle.models import DBBook
from kindle_clippings_parser.models import Book
from langdetect import detect


def dao_insert_book(book_data: Book):
    language_counter = defaultdict(int)
    for highlight in book_data.highlights:
        highlight_language_code = detect(highlight.text)
        language_counter[highlight_language_code] += 1

    sorted_items = sorted(language_counter.items(), key=lambda x: x[1], reverse=True)
    sorted_language_codes = [x[0] for x in sorted_items]
    language_code = sorted_language_codes[0]

    books_query_set = dao_get_books_by_title_publisher_author(book_data)
    if books_query_set.count() < 1:
        db_book = (DBBook(
            title=book_data.title,
            publisher=book_data.publisher,
            author=book_data.author,
            language_code=language_code,
        ))
        db_book.save()
        return db_book

    return books_query_set.first()


def dao_get_books_by_title_publisher_author(book_data: Book):
    return (DBBook.objects
            .filter(title=book_data.title, publisher=book_data.publisher, author=book_data.author)
    )

def dao_get_books():
    return DBBooks.objects.all()
