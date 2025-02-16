# Generated by Django 3.2.13 on 2022-06-10 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReactionLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_id', models.PositiveIntegerField(db_index=True, default=None, null=True)),
                ('voter_we_vote_id', models.CharField(db_index=True, default=None, max_length=255, null=True)),
                ('voter_display_name', models.CharField(max_length=255, null=True)),
                ('liked_item_we_vote_id', models.CharField(db_index=True, default=None, max_length=255, null=True)),
                ('activity_tidbit_we_vote_id', models.CharField(db_index=True, default=None, max_length=255, null=True)),
                ('date_last_changed', models.DateTimeField(auto_now=True, null=True, verbose_name='date last changed')),
            ],
        ),
    ]
