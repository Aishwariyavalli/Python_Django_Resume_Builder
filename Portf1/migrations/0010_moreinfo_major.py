# Generated by Django 3.0.4 on 2020-04-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portf1', '0009_auto_20200411_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='moreinfo',
            name='major',
            field=models.CharField(max_length=200, null=True),
        ),
    ]