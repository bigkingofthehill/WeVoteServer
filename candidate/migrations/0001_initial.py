# Generated by Django 3.2.13 on 2022-06-10 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('we_vote_id', models.CharField(blank=True, db_index=True, default=None, max_length=255, null=True, unique=True, verbose_name='we vote permanent id of this candidate')),
                ('maplight_id', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='maplight candidate id')),
                ('vote_smart_id', models.CharField(blank=True, default=None, max_length=15, null=True, verbose_name='vote smart candidate id')),
                ('contest_office_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='contest_office_id id')),
                ('contest_office_we_vote_id', models.CharField(blank=True, db_index=True, default=None, max_length=255, null=True, verbose_name='we vote permanent id for the office this candidate is running for')),
                ('contest_office_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name of the office')),
                ('politician_id', models.BigIntegerField(blank=True, null=True, verbose_name='politician unique identifier')),
                ('politician_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='we vote politician id')),
                ('candidate_name', models.CharField(max_length=255, verbose_name='candidate name')),
                ('google_civic_candidate_name', models.CharField(max_length=255, null=True, verbose_name='candidate name exactly as received from google civic')),
                ('google_civic_candidate_name2', models.CharField(max_length=255, null=True, verbose_name='candidate name exactly as received from google civic')),
                ('google_civic_candidate_name3', models.CharField(max_length=255, null=True, verbose_name='candidate name exactly as received from google civic')),
                ('candidate_gender', models.CharField(blank=True, max_length=255, null=True, verbose_name='candidate gender')),
                ('birth_day_text', models.CharField(blank=True, max_length=10, null=True, verbose_name='birth day')),
                ('party', models.CharField(blank=True, max_length=255, null=True, verbose_name='party')),
                ('photo_url', models.TextField(blank=True, null=True, verbose_name='photoUrl')),
                ('photo_url_from_ctcl', models.TextField(blank=True, null=True)),
                ('photo_url_from_maplight', models.TextField(blank=True, null=True, verbose_name='candidate portrait url of candidate from maplight')),
                ('photo_url_from_vote_smart', models.TextField(blank=True, null=True, verbose_name='candidate portrait url of candidate from vote smart')),
                ('photo_url_from_vote_usa', models.TextField(blank=True, null=True)),
                ('order_on_ballot', models.CharField(blank=True, max_length=255, null=True, verbose_name='order on ballot')),
                ('google_civic_election_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='google civic election id')),
                ('google_civic_election_id_new', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='google civic election id')),
                ('ocd_division_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='ocd division id')),
                ('instagram_handle', models.TextField(blank=True, null=True, verbose_name="candidate's instagram handle")),
                ('instagram_followers_count', models.IntegerField(blank=True, null=True, verbose_name="count of candidate's instagram followers")),
                ('candidate_ultimate_election_date', models.PositiveIntegerField(default=None, null=True)),
                ('candidate_year', models.PositiveIntegerField(default=None, null=True)),
                ('state_code', models.CharField(blank=True, db_index=True, max_length=2, null=True, verbose_name='state this candidate serves')),
                ('date_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('candidate_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='website url of candidate')),
                ('candidate_contact_form_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='website url of candidate contact form')),
                ('facebook_url', models.TextField(blank=True, null=True, verbose_name='facebook url of candidate')),
                ('facebook_url_is_broken', models.BooleanField(default=False, verbose_name='facebook url is broken')),
                ('facebook_profile_image_url_https', models.TextField(blank=True, null=True, verbose_name='url of profile image from facebook')),
                ('twitter_url', models.URLField(blank=True, null=True, verbose_name='twitter url of candidate')),
                ('twitter_user_id', models.BigIntegerField(blank=True, null=True, verbose_name='twitter id')),
                ('candidate_twitter_handle', models.CharField(max_length=255, null=True)),
                ('candidate_twitter_handle2', models.CharField(max_length=255, null=True)),
                ('candidate_twitter_handle3', models.CharField(max_length=255, null=True)),
                ('candidate_twitter_updates_failing', models.BooleanField(default=False)),
                ('twitter_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='candidate plain text name from twitter')),
                ('twitter_location', models.CharField(blank=True, max_length=255, null=True, verbose_name='candidate location from twitter')),
                ('twitter_followers_count', models.IntegerField(blank=True, default=0, verbose_name='number of twitter followers')),
                ('twitter_profile_image_url_https', models.TextField(blank=True, null=True, verbose_name='locally cached url of candidate profile image from twitter')),
                ('twitter_profile_background_image_url_https', models.TextField(blank=True, null=True, verbose_name='tile-able background from twitter')),
                ('twitter_profile_banner_url_https', models.TextField(blank=True, null=True, verbose_name='profile banner image from twitter')),
                ('twitter_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Text description of this organization from twitter.')),
                ('vote_usa_office_id', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Vote USA permanent id for the office')),
                ('vote_usa_politician_id', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Vote USA permanent id for this candidate')),
                ('vote_usa_profile_image_url_https', models.TextField(blank=True, default=None, null=True)),
                ('profile_image_type_currently_active', models.CharField(choices=[('FACEBOOK', 'Facebook'), ('TWITTER', 'Twitter'), ('UNKNOWN', 'Unknown'), ('UPLOADED', 'Uploaded'), ('VOTE_USA', 'Vote-USA')], default='UNKNOWN', max_length=10)),
                ('we_vote_hosted_profile_facebook_image_url_large', models.TextField(blank=True, null=True)),
                ('we_vote_hosted_profile_facebook_image_url_medium', models.TextField(blank=True, null=True)),
                ('we_vote_hosted_profile_facebook_image_url_tiny', models.TextField(blank=True, null=True)),
                ('we_vote_hosted_profile_twitter_image_url_large', models.TextField(blank=True, null=True)),
                ('we_vote_hosted_profile_twitter_image_url_medium', models.TextField(blank=True, null=True)),
                ('we_vote_hosted_profile_twitter_image_url_tiny', models.TextField(blank=True, null=True)),
                ('we_vote_hosted_profile_uploaded_image_url_large', models.TextField(blank=True, null=True)),
                ('we_vote_hosted_profile_uploaded_image_url_medium', models.TextField(blank=True, null=True)),
                ('we_vote_hosted_profile_uploaded_image_url_tiny', models.TextField(blank=True, null=True)),
                ('we_vote_hosted_profile_vote_usa_image_url_large', models.TextField(blank=True, null=True)),
                ('we_vote_hosted_profile_vote_usa_image_url_medium', models.TextField(blank=True, null=True)),
                ('we_vote_hosted_profile_vote_usa_image_url_tiny', models.TextField(blank=True, null=True)),
                ('we_vote_hosted_profile_image_url_large', models.TextField(blank=True, null=True)),
                ('we_vote_hosted_profile_image_url_medium', models.TextField(blank=True, null=True)),
                ('we_vote_hosted_profile_image_url_tiny', models.TextField(blank=True, null=True)),
                ('flickr_url', models.TextField(blank=True, null=True)),
                ('go_fund_me_url', models.TextField(blank=True, null=True)),
                ('google_plus_url', models.URLField(blank=True, null=True, verbose_name='google plus url of candidate')),
                ('vimeo_url', models.TextField(blank=True, null=True)),
                ('youtube_url', models.URLField(blank=True, null=True, verbose_name='youtube url of candidate')),
                ('candidate_email', models.CharField(blank=True, max_length=255, null=True, verbose_name='candidate email')),
                ('candidate_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='candidate phone')),
                ('wikipedia_page_id', models.BigIntegerField(blank=True, null=True, verbose_name='pageid')),
                ('wikipedia_page_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Page title on Wikipedia')),
                ('wikipedia_photo_url', models.TextField(blank=True, null=True, verbose_name='url of wikipedia logo')),
                ('linkedin_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='linkedin url of candidate')),
                ('linkedin_photo_url', models.TextField(blank=True, null=True, verbose_name='url of linkedin logo')),
                ('other_source_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='other source url of candidate')),
                ('other_source_photo_url', models.TextField(blank=True, null=True, verbose_name='url of other source image')),
                ('ballotpedia_candidate_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='ballotpedia integer id')),
                ('ballotpedia_candidate_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='candidate name exactly as received from ballotpedia')),
                ('ballotpedia_candidate_summary', models.TextField(blank=True, default=None, null=True, verbose_name='candidate summary from ballotpedia')),
                ('ballotpedia_candidate_url', models.TextField(blank=True, null=True, verbose_name='url of candidate on ballotpedia')),
                ('ballotpedia_election_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='ballotpedia election id')),
                ('ballotpedia_image_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='ballotpedia image id')),
                ('ballotpedia_profile_image_url_https', models.TextField(blank=True, null=True, verbose_name='locally cached candidate profile image from ballotpedia')),
                ('ballotpedia_office_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='ballotpedia elected office integer id')),
                ('ballotpedia_page_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Page title on Ballotpedia')),
                ('ballotpedia_person_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='ballotpedia integer id')),
                ('ballotpedia_photo_url', models.TextField(blank=True, null=True, verbose_name='url of ballotpedia logo')),
                ('ballotpedia_race_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='ballotpedia race integer id')),
                ('ballot_guide_official_statement', models.TextField(blank=True, default='', null=True, verbose_name='official candidate statement from ballot guide')),
                ('crowdpac_candidate_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='crowdpac integer id')),
                ('ctcl_uuid', models.CharField(blank=True, max_length=36, null=True, verbose_name='ctcl uuid')),
                ('candidate_is_top_ticket', models.BooleanField(default=False, verbose_name='candidate is top ticket')),
                ('candidate_is_incumbent', models.BooleanField(default=False, verbose_name='candidate is the current incumbent')),
                ('candidate_participation_status', models.CharField(blank=True, max_length=255, null=True, verbose_name='candidate participation status')),
                ('withdrawn_from_election', models.BooleanField(default=False, verbose_name='Candidate has withdrawn from election')),
                ('withdrawal_date', models.DateField(null=True, verbose_name='Withdrawal date from election')),
                ('do_not_display_on_ballot', models.BooleanField(default=False)),
                ('migrated_to_link', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateLogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_process_id', models.PositiveIntegerField(db_index=True, null=True)),
                ('candidate_we_vote_id', models.CharField(max_length=255)),
                ('candidate_field_name', models.CharField(max_length=255, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('google_civic_election_id', models.PositiveIntegerField(db_index=True, null=True)),
                ('is_from_twitter', models.BooleanField(db_index=True, default=False, null=True)),
                ('kind_of_log_entry', models.CharField(db_index=True, default=None, max_length=50, null=True)),
                ('log_entry_deleted', models.BooleanField(db_index=True, default=False)),
                ('log_entry_message', models.TextField(null=True)),
                ('state_code', models.CharField(db_index=True, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CandidatesAreNotDuplicates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate1_we_vote_id', models.CharField(max_length=255, null=True, verbose_name='first candidate we are tracking')),
                ('candidate2_we_vote_id', models.CharField(max_length=255, null=True, verbose_name='second candidate we are tracking')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateToOfficeLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_we_vote_id', models.CharField(db_index=True, max_length=255)),
                ('contest_office_we_vote_id', models.CharField(db_index=True, max_length=255)),
                ('google_civic_election_id', models.PositiveIntegerField(db_index=True, default=0)),
                ('state_code', models.CharField(db_index=True, max_length=2, null=True)),
                ('position_dates_set', models.BooleanField(default=False)),
            ],
        ),
    ]