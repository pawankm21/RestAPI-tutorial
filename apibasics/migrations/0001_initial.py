# Generated by Django 3.2.3 on 2021-05-28 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('agent', models.CharField(max_length=50)),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField()),
                ('interest_rate', models.IntegerField()),
            ],
        ),
    ]
