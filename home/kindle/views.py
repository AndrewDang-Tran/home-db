from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from kindle_clippings_parser import KindleClippingsParser
from kindle_clippings_parser.models import Book, Highlight, KindleClippings, KindleClippingsParserConfig
from kindle.services.KindleHighlightsService import insert_books_and_highlights, sync_japanese_highlights_with_anki_sentence_cards


# Create your views here.

class KindleView(APIView):
    @csrf_exempt
    def post(self, request):
        config = KindleClippingsParserConfig(True, 'PST8PDT')
        parser = KindleClippingsParser(config)
        kindle_clippings = parser.parse_kindle_clippings('/Users/andrew/workspace/kindle-clippings-parser/example_clippings.txt')
        insert_books_and_highlights(kindle_clippings)
        sync_japanese_highlights_with_anki_sentence_cards()
        return Response({"status": "pass"}, status=status.HTTP_200_OK)



