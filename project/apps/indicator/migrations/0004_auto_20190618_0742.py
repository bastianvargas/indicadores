# Generated by Django 2.2.2 on 2019-06-18 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicator', '0003_auto_20190618_0656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='date',
            old_name='date',
            new_name='date_currency',
        ),
    ]
