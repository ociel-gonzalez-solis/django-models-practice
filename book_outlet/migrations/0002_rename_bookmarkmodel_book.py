# Generated by Django 4.0.6 on 2022-07-27 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookmarkModel',
            new_name='Book',
        ),
    ]