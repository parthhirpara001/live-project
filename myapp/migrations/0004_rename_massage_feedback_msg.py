# Generated by Django 4.2.6 on 2023-12-29 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='massage',
            new_name='msg',
        ),
    ]
