# Generated by Django 2.2.2 on 2019-06-18 06:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('indicator', '0002_auto_20190617_0111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='date',
        ),
        migrations.RemoveField(
            model_name='currency',
            name='value',
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('value', models.FloatField(default=None)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicator.Currency')),
            ],
        ),
    ]
