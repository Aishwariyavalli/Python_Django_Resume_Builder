# Generated by Django 3.0.4 on 2020-04-10 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Portf1', '0002_auto_20200410_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=20)),
                ('image', models.FilePathField(path='/img')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projectslist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='education',
            name='sname',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='sname',
        ),
        migrations.DeleteModel(
            name='BasicInfo',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.AddField(
            model_name='item',
            name='projectslist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portf1.ProjectsList'),
        ),
    ]
