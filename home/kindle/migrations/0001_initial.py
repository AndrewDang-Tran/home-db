# Generated by Django 3.2.8 on 2021-10-17 16:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DBBook',
            fields=[
                ('book_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('language_code', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='DBHighlight',
            fields=[
                ('highlight_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=255)),
                ('relative_page_number', models.IntegerField()),
                ('text', models.CharField(max_length=255)),
                ('highlight_date', models.DateTimeField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('book_id', models.ForeignKey(db_column='book_id', on_delete=django.db.models.deletion.CASCADE, to='kindle.dbbook')),
            ],
            options={
                'db_table': 'highlights',
            },
        ),
    ]
