# Generated by Django 3.2.7 on 2022-11-20 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Book', '0004_book_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoadBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(default=django.utils.timezone.now)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Book.book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]