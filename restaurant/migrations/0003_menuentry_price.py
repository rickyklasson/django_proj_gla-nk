# Generated by Django 4.1 on 2022-08-30 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_menuentry_english_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuentry',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]