# Generated by Django 2.2.1 on 2019-10-07 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='desprition_html',
        ),
    ]
