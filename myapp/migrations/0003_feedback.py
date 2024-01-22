# Generated by Django 4.2.6 on 2023-12-29 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_mynotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('number', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('massage', models.TextField()),
            ],
        ),
    ]
