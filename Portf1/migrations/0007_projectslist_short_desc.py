# Generated by Django 3.0.4 on 2020-04-11 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portf1', '0006_projectslist_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectslist',
            name='short_desc',
            field=models.CharField(max_length=100, null=True),
        ),
    ]