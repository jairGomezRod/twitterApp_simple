# Generated by Django 3.2.8 on 2021-10-26 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_alter_tweet_usertweet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='body',
            new_name='contentTweet',
        ),
    ]
