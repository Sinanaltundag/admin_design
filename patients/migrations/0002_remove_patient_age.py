# Generated by Django 4.0.5 on 2022-06-13 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='age',
        ),
    ]