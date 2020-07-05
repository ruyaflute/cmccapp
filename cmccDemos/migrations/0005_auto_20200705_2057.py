# Generated by Django 3.0.7 on 2020-07-05 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmccDemos', '0004_auto_20200615_2236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cmccdemo',
            old_name='summary',
            new_name='topic',
        ),
        migrations.RemoveField(
            model_name='cmccdemo',
            name='new_field',
        ),
        migrations.AddField(
            model_name='cmccdemo',
            name='blog_content',
            field=models.TextField(default='Blog content'),
        ),
        migrations.AddField(
            model_name='cmccdemo',
            name='create_date',
            field=models.TimeField(default='Blog content', max_length=5000),
        ),
        migrations.AddField(
            model_name='cmccdemo',
            name='subtopic',
            field=models.CharField(default='subtopic', max_length=200),
        ),
    ]
