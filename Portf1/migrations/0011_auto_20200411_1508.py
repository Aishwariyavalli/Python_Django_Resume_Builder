# Generated by Django 3.0.4 on 2020-04-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portf1', '0010_moreinfo_major'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moreinfo',
            name='Highschoolcgpa',
            field=models.FloatField(null=True, verbose_name='high school cgpa'),
        ),
        migrations.AlterField(
            model_name='moreinfo',
            name='Highschoolname',
            field=models.CharField(max_length=200, null=True, verbose_name='high school name'),
        ),
        migrations.AlterField(
            model_name='moreinfo',
            name='collegecgpa',
            field=models.FloatField(null=True, verbose_name='college cgpa'),
        ),
        migrations.AlterField(
            model_name='moreinfo',
            name='collegename',
            field=models.CharField(max_length=200, null=True, verbose_name='college name'),
        ),
        migrations.AlterField(
            model_name='moreinfo',
            name='firstname',
            field=models.CharField(max_length=300, null=True, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='moreinfo',
            name='lastname',
            field=models.CharField(max_length=300, null=True, verbose_name='last name'),
        ),
    ]
