# Generated by Django 3.2.7 on 2022-11-21 04:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Book', '0004_book_user'),
        ('loanbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LoadBook',
            new_name='LoanBook',
        ),
    ]
