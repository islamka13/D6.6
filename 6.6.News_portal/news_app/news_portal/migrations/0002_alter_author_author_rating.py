# Generated by Django 4.2 on 2023-05-18 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_rating',
            field=models.IntegerField(default=0),
        ),
    ]
