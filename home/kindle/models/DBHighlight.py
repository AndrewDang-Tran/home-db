import uuid

from django.db import models

from kindle.models.DBBook import DBBook

class DBHighlight(models.Model):
    highlight_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book_id = models.ForeignKey(DBBook, on_delete=models.CASCADE, db_column='book_id')
    location = models.CharField(max_length=255)
    relative_page_number = models.IntegerField()
    text = models.CharField(max_length=255)
    highlight_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'highlights'
        models.UniqueConstraint(fields=['book_id', 'text'], name='unique_book_highlight')

