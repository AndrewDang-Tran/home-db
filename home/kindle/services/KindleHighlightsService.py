from kindle_clippings_parser.models import Book, Highlight, KindleClippings, KindleClippingsParserConfig
from anki_helpers import AnkiConnectClient
from anki_helpers.models import AddNoteRequest, AddNoteOptions, DuplicateScopeOptions
from kindle.daos.BooksDAO import dao_insert_book
from kindle.daos.HighlightsDAO import dao_insert_highlight, dao_get_highlights_by_book_language

def insert_books_and_highlights(kindle_clippings: KindleClippings):
    for book in kindle_clippings.books:
        inserted_book = dao_insert_book(book)
        for highlight in book.highlights:
            inserted_highlight = dao_insert_highlight(inserted_book, highlight)

def sync_japanese_highlights_with_anki_sentence_cards():
    DECK_NAME = 'SentenceCards'
    SYNC_TAG = 'automatedSentenceCards'
    MODEL_NAME = 'MIA Japanese'

    anki_connect_client = AnkiConnectClient()
    if not anki_connect_client.is_online():
        raise EnvironmentException('AnkiConnect not installed or anki not open')

    anki_duplicate_scope_options = (DuplicateScopeOptions(
        deckName=DECK_NAME,
        checkChildren=True,
        checkAllModels=False,
    ))
    anki_add_note_options = (AddNoteOptions(
        allowDuplicate=False,
        duplicateScope=DECK_NAME,
        duplicateScopeOptions=anki_duplicate_scope_options,
    ))

    highlights_query_set = dao_get_highlights_by_book_language('ja')
    for highlight in highlights_query_set:
        fields = {
            'Expression': highlight.text,
        }
        anki_add_note_request = (AddNoteRequest(
            deckName=DECK_NAME,
            modelName=MODEL_NAME,
            fields=fields,
            tags=[SYNC_TAG],
            options=anki_add_note_options,
        ))
        anki_connect_client.add_note(anki_add_note_request)




