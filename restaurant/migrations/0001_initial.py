# Generated by Django 4.1 on 2022-08-30 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MenuEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swedish_title', models.CharField(max_length=200)),
                ('swedish_description', models.CharField(max_length=200)),
                ('hungarian_title', models.CharField(max_length=200)),
                ('hungarian_description', models.CharField(max_length=200)),
                ('english_title', models.CharField(max_length=200)),
                ('english_description', models.CharField(max_length=200)),
                ('menu_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.menucategory')),
            ],
        ),
    ]