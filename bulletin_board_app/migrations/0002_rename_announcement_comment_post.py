# Generated by Django 4.2.4 on 2023-09-07 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='announcement',
            new_name='post',
        ),
    ]