# Generated by Django 4.1 on 2022-08-31 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_menuentry_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField()),
                ('review_text', models.CharField(max_length=800)),
            ],
        ),
    ]