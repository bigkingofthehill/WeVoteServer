# Generated by Django 3.2.13 on 2022-06-10 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookmarkItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_id', models.BigIntegerField(blank=True, null=True)),
                ('candidate_id', models.BigIntegerField(blank=True, null=True)),
                ('candidate_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='we vote permanent id')),
                ('contest_office_id', models.BigIntegerField(blank=True, null=True)),
                ('contest_office_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='we vote permanent id')),
                ('contest_measure_id', models.BigIntegerField(blank=True, null=True)),
                ('contest_measure_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='we vote permanent id')),
                ('bookmark_status', models.CharField(choices=[('BOOKMARKED', 'Item Bookmarked'), ('NOT_BOOKMARKED', 'Item Not Bookmarked')], default='NOT_BOOKMARKED', max_length=16)),
                ('date_last_changed', models.DateTimeField(auto_now=True, null=True, verbose_name='date last changed')),
            ],
        ),
        migrations.CreateModel(
            name='BookmarkItemList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
