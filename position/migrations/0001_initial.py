# Generated by Django 3.2.13 on 2022-06-10 23:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('twitter', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionNetworkScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewing_voter_id', models.PositiveIntegerField(db_index=True)),
                ('viewing_voter_we_vote_id', models.CharField(db_index=True, max_length=255)),
                ('google_civic_election_id', models.PositiveIntegerField(blank=True, db_index=True, default=None, null=True, verbose_name='google civic election id')),
                ('organization_we_vote_id', models.CharField(max_length=255, null=True)),
                ('friend_voter_we_vote_id', models.CharField(max_length=255, null=True)),
                ('candidate_we_vote_id', models.CharField(db_index=True, max_length=255, null=True)),
                ('measure_we_vote_id', models.CharField(db_index=True, max_length=255, null=True)),
                ('speaker_display_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name of the org or person with position')),
                ('is_support', models.BooleanField(default=False)),
                ('is_oppose', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PositionForFriends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('we_vote_id', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='we vote permanent id')),
                ('position_id', models.BigIntegerField(blank=True, null=True)),
                ('test', models.BigIntegerField(blank=True, null=True)),
                ('ballot_item_display_name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='text name for ballot item')),
                ('ballot_item_image_url_https', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of https image for candidate, measure or office')),
                ('ballot_item_image_url_https_large', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of https large version image for candidate, measure or office')),
                ('ballot_item_image_url_https_medium', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of https medium version image for candidate, measure or office')),
                ('ballot_item_image_url_https_tiny', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of https tiny version image for candidate, measure or office')),
                ('ballot_item_twitter_handle', models.CharField(max_length=255, null=True, verbose_name='twitter screen_name for candidate, measure, or office')),
                ('speaker_display_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name of the org or person with position')),
                ('speaker_image_url_https', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of https image for org or person with position')),
                ('speaker_image_url_https_large', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of https large version image for org or person with position')),
                ('speaker_image_url_https_medium', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of https medium version image for org or person with position')),
                ('speaker_image_url_https_tiny', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of https tiny version image for org or person with position')),
                ('speaker_twitter_handle', models.CharField(max_length=255, null=True, verbose_name='twitter screen_name for org or person with position')),
                ('twitter_followers_count', models.IntegerField(blank=True, default=0, verbose_name='number of twitter followers')),
                ('speaker_type', models.CharField(choices=[('C', 'Corporation'), ('G', 'Group'), ('I', 'Individual'), ('NW', 'News Corporation'), ('NP', 'Nonpartisan'), ('C3', 'Nonprofit 501c3'), ('C4', 'Nonprofit 501c4'), ('P', 'Political Action Committee'), ('PF', 'Public Figure'), ('TA', 'Trade Association or Union'), ('U', 'Unknown Type'), ('O', 'Group - Organization')], default='U', max_length=2, verbose_name='type of org')),
                ('date_entered', models.DateTimeField(db_index=True, default=None, null=True, verbose_name='date entered')),
                ('date_last_changed', models.DateTimeField(auto_now=True, null=True, verbose_name='date last changed')),
                ('organization_id', models.BigIntegerField(blank=True, db_index=True, null=True)),
                ('organization_we_vote_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='we vote permanent id for the organization')),
                ('is_private_citizen', models.BooleanField(null=True)),
                ('voter_id', models.BigIntegerField(blank=True, db_index=True, null=True)),
                ('voter_we_vote_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='we vote permanent id for the voter expressing the opinion')),
                ('public_figure_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='public figure we vote id')),
                ('google_civic_election_id', models.PositiveIntegerField(blank=True, db_index=True, default=0, null=True, verbose_name='google civic election id')),
                ('position_ultimate_election_date', models.PositiveIntegerField(default=None, null=True)),
                ('position_year', models.PositiveIntegerField(default=None, null=True)),
                ('state_code', models.CharField(blank=True, max_length=2, null=True, verbose_name='us state of the ballot item position is for')),
                ('vote_smart_rating_id', models.BigIntegerField(blank=True, null=True)),
                ('vote_smart_time_span', models.CharField(blank=True, max_length=255, null=True, verbose_name='the period in which the organization stated this position')),
                ('vote_smart_rating', models.CharField(blank=True, max_length=255, null=True, verbose_name='vote smart value between 0-100')),
                ('vote_smart_rating_integer', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='vote smart value between 0-100')),
                ('vote_smart_rating_name', models.CharField(blank=True, max_length=255, null=True)),
                ('tweet_source_id', models.BigIntegerField(blank=True, null=True)),
                ('contest_office_id', models.BigIntegerField(blank=True, db_index=True, null=True, verbose_name='id of contest_office')),
                ('contest_office_we_vote_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='we vote permanent id for the contest_office')),
                ('contest_office_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name of the office')),
                ('race_office_level', models.CharField(blank=True, max_length=255, null=True, verbose_name='race office level')),
                ('candidate_campaign_id', models.BigIntegerField(blank=True, db_index=True, null=True, verbose_name='id of candidate')),
                ('candidate_campaign_we_vote_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='we vote permanent id for the candidate')),
                ('google_civic_candidate_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='candidate name exactly as received from google civic')),
                ('politician_id', models.BigIntegerField(blank=True, null=True, verbose_name='')),
                ('politician_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='we vote permanent id for politician')),
                ('political_party', models.CharField(max_length=255, null=True, verbose_name='candidate political party')),
                ('contest_measure_id', models.BigIntegerField(blank=True, db_index=True, null=True, verbose_name='id of contest_measure')),
                ('contest_measure_we_vote_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='we vote permanent id for the contest_measure')),
                ('google_civic_measure_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='measure title exactly as received from google civic')),
                ('stance', models.CharField(choices=[('SUPPORT', 'Supports'), ('STILL_DECIDING', 'Still deciding'), ('NO_STANCE', 'No stance'), ('INFO_ONLY', 'Information only'), ('OPPOSE', 'Opposes'), ('PERCENT_RATING', 'Percentage point rating')], db_index=True, default='NO_STANCE', max_length=15)),
                ('statement_text', models.TextField(blank=True, null=True)),
                ('statement_html', models.TextField(blank=True, null=True)),
                ('more_info_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='url with more info about this position')),
                ('from_scraper', models.BooleanField(default=False)),
                ('organization_certified', models.BooleanField(default=False)),
                ('volunteer_certified', models.BooleanField(default=False)),
                ('twitter_user_entered_position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='twitter.twitteruser', verbose_name='')),
                ('voter_entering_position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='authenticated user who entered position')),
            ],
            options={
                'ordering': ('date_entered',),
            },
        ),
        migrations.CreateModel(
            name='PositionEntered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('we_vote_id', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='we vote permanent id')),
                ('position_id', models.BigIntegerField(blank=True, null=True)),
                ('test', models.BigIntegerField(blank=True, null=True)),
                ('ballot_item_display_name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='text name for ballot item')),
                ('ballot_item_image_url_https', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of https image for candidate, measure or office')),
                ('ballot_item_image_url_https_large', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of https large version image for candidate, measure or office')),
                ('ballot_item_image_url_https_medium', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of https medium version image for candidate, measure or office')),
                ('ballot_item_image_url_https_tiny', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of https tiny version image for candidate, measure or office')),
                ('ballot_item_twitter_handle', models.CharField(max_length=255, null=True, verbose_name='twitter screen_name for candidate, measure, or office')),
                ('speaker_display_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name of the org or person with position')),
                ('speaker_image_url_https', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of https image for org or person with position')),
                ('speaker_image_url_https_large', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of https large version image for org or person with position')),
                ('speaker_image_url_https_medium', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of https medium version image for org or person with position')),
                ('speaker_image_url_https_tiny', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of https tiny version image for org or person with position')),
                ('speaker_twitter_handle', models.CharField(max_length=255, null=True, verbose_name='twitter screen_name for org or person with position')),
                ('twitter_followers_count', models.IntegerField(blank=True, default=0, verbose_name='number of twitter followers')),
                ('speaker_type', models.CharField(choices=[('C', 'Corporation'), ('G', 'Group'), ('I', 'Individual'), ('NW', 'News Corporation'), ('NP', 'Nonpartisan'), ('C3', 'Nonprofit 501c3'), ('C4', 'Nonprofit 501c4'), ('P', 'Political Action Committee'), ('PF', 'Public Figure'), ('TA', 'Trade Association or Union'), ('U', 'Unknown Type'), ('O', 'Group - Organization')], default='U', max_length=2, verbose_name='type of org')),
                ('date_entered', models.DateTimeField(db_index=True, default=None, null=True, verbose_name='date entered')),
                ('date_last_changed', models.DateTimeField(auto_now=True, null=True, verbose_name='date last changed')),
                ('organization_id', models.BigIntegerField(blank=True, db_index=True, null=True)),
                ('organization_we_vote_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='we vote permanent id for the organization')),
                ('is_private_citizen', models.BooleanField(null=True)),
                ('voter_id', models.BigIntegerField(blank=True, db_index=True, null=True)),
                ('voter_we_vote_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='we vote permanent id for the voter expressing the opinion')),
                ('public_figure_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='public figure we vote id')),
                ('google_civic_election_id', models.CharField(db_index=True, default=0, max_length=255, null=True, verbose_name='google civic election id')),
                ('position_ultimate_election_date', models.PositiveIntegerField(default=None, null=True)),
                ('position_year', models.PositiveIntegerField(default=None, null=True)),
                ('state_code', models.CharField(blank=True, db_index=True, max_length=2, null=True, verbose_name='us state of the ballot item position is for')),
                ('google_civic_election_id_new', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='google civic election id')),
                ('vote_smart_rating_id', models.BigIntegerField(blank=True, null=True)),
                ('vote_smart_time_span', models.CharField(blank=True, max_length=255, null=True, verbose_name='the period in which the organization stated this position')),
                ('vote_smart_rating', models.CharField(blank=True, max_length=255, null=True, verbose_name='vote smart value between 0-100')),
                ('vote_smart_rating_integer', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='vote smart value between 0-100')),
                ('vote_smart_rating_name', models.CharField(blank=True, max_length=255, null=True)),
                ('tweet_source_id', models.BigIntegerField(blank=True, null=True)),
                ('contest_office_id', models.BigIntegerField(blank=True, db_index=True, null=True, verbose_name='id of contest_office')),
                ('contest_office_we_vote_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='we vote permanent id for the contest_office')),
                ('contest_office_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name of the office')),
                ('race_office_level', models.CharField(blank=True, max_length=255, null=True, verbose_name='race office level')),
                ('candidate_campaign_id', models.BigIntegerField(blank=True, db_index=True, null=True, verbose_name='id of candidate')),
                ('candidate_campaign_we_vote_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='we vote permanent id for the candidate')),
                ('google_civic_candidate_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='candidate name exactly as received from google civic')),
                ('google_civic_measure_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='measure title exactly as received from google civic')),
                ('politician_id', models.BigIntegerField(blank=True, null=True, verbose_name='')),
                ('politician_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='we vote permanent id for politician')),
                ('political_party', models.CharField(max_length=255, null=True, verbose_name='political party')),
                ('contest_measure_id', models.BigIntegerField(blank=True, db_index=True, null=True, verbose_name='id of contest_measure')),
                ('contest_measure_we_vote_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='we vote permanent id for the contest_measure')),
                ('stance', models.CharField(choices=[('SUPPORT', 'Supports'), ('STILL_DECIDING', 'Still deciding'), ('NO_STANCE', 'No stance'), ('INFO_ONLY', 'Information only'), ('OPPOSE', 'Opposes'), ('PERCENT_RATING', 'Percentage point rating')], db_index=True, default='NO_STANCE', max_length=15)),
                ('statement_text', models.TextField(blank=True, null=True)),
                ('statement_html', models.TextField(blank=True, null=True)),
                ('more_info_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='url with more info about this position')),
                ('from_scraper', models.BooleanField(default=False)),
                ('organization_certified', models.BooleanField(default=False)),
                ('volunteer_certified', models.BooleanField(default=False)),
                ('twitter_user_entered_position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='twitter.twitteruser', verbose_name='')),
                ('voter_entering_position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='authenticated user who entered position')),
            ],
            options={
                'ordering': ('date_entered',),
            },
        ),
    ]
