# Generated by Django 5.0.6 on 2024-06-26 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
