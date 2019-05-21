# Generated by Django 2.2.1 on 2019-05-21 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='content',
        ),
        migrations.AddField(
            model_name='message',
            name='words',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='message',
            name='writer',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]