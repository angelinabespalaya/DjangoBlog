# Generated by Django 5.0.2 on 2024-03-04 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_body_en_en_post_body_ru_ru_post_title_en_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body_en_EN',
            new_name='body_en',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='body_ru_RU',
            new_name='body_ru',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title_en_EN',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title_ru_RU',
            new_name='title_ru',
        ),
    ]
