# Generated by Django 3.2.3 on 2021-05-28 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apibasics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='type',
            new_name='typeof',
        ),
    ]
