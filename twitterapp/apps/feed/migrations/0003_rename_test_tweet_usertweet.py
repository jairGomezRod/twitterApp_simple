# Generated by Django 3.2.8 on 2021-10-26 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_tweet_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='test',
            new_name='userTweet',
        ),
    ]
