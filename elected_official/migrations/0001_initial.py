# Generated by Django 3.2.13 on 2022-06-10 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectedOfficial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('we_vote_id', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='we vote permanent id of this person in this position')),
                ('elected_office_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='elected_office_id id')),
                ('elected_office_we_vote_id', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='we vote permanent id for the office this elected official is running for')),
                ('elected_office_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name of the office')),
                ('politician_id', models.BigIntegerField(blank=True, null=True, verbose_name='politician unique identifier')),
                ('politician_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='we vote politician id')),
                ('elected_official_name', models.CharField(max_length=255, verbose_name='elected official name')),
                ('google_civic_elected_official_name', models.CharField(max_length=255, verbose_name='elected official name exactly as received from google civic')),
                ('political_party', models.CharField(blank=True, max_length=255, null=True, verbose_name='political_party')),
                ('photo_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='photoUrl')),
                ('photo_url_from_maplight', models.URLField(blank=True, null=True, verbose_name='elected official portrait url of elected official from maplight')),
                ('photo_url_from_vote_smart', models.URLField(blank=True, null=True, verbose_name='elected official portrait url of elected official from vote smart')),
                ('order_on_ballot', models.CharField(blank=True, max_length=255, null=True, verbose_name='order on ballot')),
                ('google_civic_election_id', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='google civic election id')),
                ('ocd_division_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='ocd division id')),
                ('state_code', models.CharField(blank=True, max_length=2, null=True, verbose_name='state this elected official serves')),
                ('elected_official_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='website url of elected official')),
                ('facebook_url', models.URLField(blank=True, null=True, verbose_name='facebook url of elected official')),
                ('facebook_profile_image_url_https', models.URLField(blank=True, null=True, verbose_name='url of profile image from facebook')),
                ('twitter_url', models.URLField(blank=True, null=True, verbose_name='twitter url of elected official')),
                ('twitter_user_id', models.BigIntegerField(blank=True, null=True, verbose_name='twitter id')),
                ('elected_official_twitter_handle', models.CharField(max_length=255, null=True, verbose_name='elected official twitter screen_name')),
                ('twitter_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='elected official plain text name from twitter')),
                ('twitter_location', models.CharField(blank=True, max_length=255, null=True, verbose_name='elected official location from twitter')),
                ('twitter_followers_count', models.IntegerField(blank=True, default=0, verbose_name='number of twitter followers')),
                ('twitter_profile_image_url_https', models.URLField(blank=True, null=True, verbose_name='url of logo from twitter')),
                ('twitter_profile_background_image_url_https', models.URLField(blank=True, null=True, verbose_name='tile-able background from twitter')),
                ('twitter_profile_banner_url_https', models.URLField(blank=True, null=True, verbose_name='profile banner image from twitter')),
                ('twitter_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Text description of this organization from twitter.')),
                ('we_vote_hosted_profile_image_url_large', models.URLField(blank=True, null=True, verbose_name='we vote hosted large image url')),
                ('we_vote_hosted_profile_image_url_medium', models.URLField(blank=True, null=True, verbose_name='we vote hosted medium image url')),
                ('we_vote_hosted_profile_image_url_tiny', models.URLField(blank=True, null=True, verbose_name='we vote hosted tiny image url')),
                ('google_plus_url', models.URLField(blank=True, null=True, verbose_name='google plus url of elected official')),
                ('vote_smart_id', models.CharField(max_length=200, null=True, verbose_name='votesmart unique identifier')),
                ('maplight_id', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='maplight unique identifier')),
                ('youtube_url', models.URLField(blank=True, null=True, verbose_name='youtube url of elected official')),
                ('elected_official_email', models.CharField(blank=True, max_length=255, null=True, verbose_name='elected official email')),
                ('elected_official_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='elected official phone')),
                ('wikipedia_page_id', models.BigIntegerField(blank=True, null=True, verbose_name='pageid')),
                ('wikipedia_page_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Page title on Wikipedia')),
                ('wikipedia_photo_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of wikipedia logo')),
                ('linkedin_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='linkedin url of elected_official')),
                ('linkedin_photo_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of linkedin logo')),
                ('other_source_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='other source url of elected_official')),
                ('other_source_photo_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of other source image')),
                ('ballotpedia_elected_official_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='ballotpedia integer id')),
                ('ballotpedia_elected_official_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='elected official name exactly as received from ballotpedia')),
                ('ballotpedia_elected_official_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of elected official on ballotpedia')),
                ('ballotpedia_page_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Page title on Ballotpedia')),
                ('ballotpedia_photo_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of ballotpedia logo')),
                ('ctcl_uuid', models.CharField(blank=True, max_length=36, null=True, verbose_name='ctcl uuid')),
            ],
        ),
        migrations.CreateModel(
            name='ElectedOfficialsAreNotDuplicates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elected_official1_we_vote_id', models.CharField(max_length=255, null=True, verbose_name='first elected official we are tracking')),
                ('elected_official2_we_vote_id', models.CharField(max_length=255, null=True, verbose_name='second elected official we are tracking')),
            ],
        ),
    ]
