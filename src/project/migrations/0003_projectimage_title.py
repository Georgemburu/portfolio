# Generated by Django 2.2 on 2019-04-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_framework'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='title',
            field=models.CharField(default='h', max_length=150),
            preserve_default=False,
        ),
    ]
