# Generated by Django 2.2.4 on 2019-09-05 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20190825_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='session',
        ),
        migrations.AddField(
            model_name='message',
            name='nickname',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
    ]
