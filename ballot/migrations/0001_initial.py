# Generated by Django 3.2.13 on 2022-06-10 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BallotItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_id', models.IntegerField(db_index=True, default=0, verbose_name='the voter unique id')),
                ('polling_location_we_vote_id', models.CharField(blank=True, db_index=True, default=None, max_length=255, null=True, verbose_name='we vote permanent id of the map point')),
                ('google_civic_election_id', models.CharField(db_index=True, max_length=20, verbose_name='google civic election id')),
                ('google_civic_election_id_new', models.PositiveIntegerField(default=0, verbose_name='google civic election id')),
                ('state_code', models.CharField(db_index=True, max_length=2, null=True, verbose_name='state the ballot item is related to')),
                ('google_ballot_placement', models.BigIntegerField(blank=True, null=True, verbose_name='the order this item should appear on the ballot')),
                ('local_ballot_order', models.IntegerField(blank=True, null=True, verbose_name='locally calculated order this item should appear on the ballot')),
                ('contest_office_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='local id for this contest office')),
                ('contest_office_we_vote_id', models.CharField(blank=True, db_index=True, default=None, max_length=255, null=True, verbose_name='we vote permanent id for this office')),
                ('contest_measure_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='contest_measure unique id')),
                ('contest_measure_we_vote_id', models.CharField(blank=True, db_index=True, default=None, max_length=255, null=True, verbose_name='we vote permanent id for this measure')),
                ('ballot_item_display_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='a label we can sort by')),
                ('measure_subtitle', models.TextField(blank=True, default='', null=True, verbose_name='google civic referendum subtitle')),
                ('measure_text', models.TextField(blank=True, default='', null=True, verbose_name='measure text')),
                ('measure_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='url of measure')),
                ('yes_vote_description', models.TextField(blank=True, default=None, null=True, verbose_name='what a yes vote means')),
                ('no_vote_description', models.TextField(blank=True, default=None, null=True, verbose_name='what a no vote means')),
            ],
        ),
        migrations.CreateModel(
            name='BallotReturned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('we_vote_id', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='we vote permanent id')),
                ('voter_id', models.IntegerField(blank=True, null=True, verbose_name='the voter unique id')),
                ('polling_location_we_vote_id', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='we vote permanent id of the map point')),
                ('google_civic_election_id', models.PositiveIntegerField(db_index=True, default=0, verbose_name='google civic election id')),
                ('election_description_text', models.CharField(max_length=255, verbose_name='text label for this election')),
                ('election_date', models.DateField(null=True, verbose_name='election start date')),
                ('ballot_location_display_option_on', models.BooleanField(db_index=True, default=False)),
                ('ballot_location_display_name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='name that shows in button')),
                ('ballot_location_shortcut', models.CharField(blank=True, max_length=255, null=True, verbose_name='the url string to find this location')),
                ('ballot_location_order', models.PositiveIntegerField(default=0, verbose_name='order of these ballot locations in display')),
                ('text_for_map_search', models.CharField(max_length=255, verbose_name='address as entered')),
                ('latitude', models.FloatField(null=True, verbose_name='latitude returned from Google')),
                ('longitude', models.FloatField(null=True, verbose_name='longitude returned from Google')),
                ('state_code', models.CharField(db_index=True, max_length=2, null=True, verbose_name='state code returned or calculated')),
                ('normalized_line1', models.CharField(blank=True, max_length=255, null=True, verbose_name='normalized address line 1 returned from Google')),
                ('normalized_line2', models.CharField(blank=True, max_length=255, null=True, verbose_name='normalized address line 2 returned from Google')),
                ('normalized_city', models.CharField(blank=True, max_length=255, null=True, verbose_name='normalized city returned from Google')),
                ('normalized_state', models.CharField(blank=True, max_length=255, null=True, verbose_name='normalized state returned from Google')),
                ('normalized_zip', models.CharField(blank=True, max_length=255, null=True, verbose_name='normalized zip returned from Google')),
                ('date_last_updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='date ballot items last retrieved')),
            ],
        ),
        migrations.CreateModel(
            name='BallotReturnedEmpty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polling_location_we_vote_id', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='we vote permanent id of the map point')),
                ('google_civic_election_id', models.PositiveIntegerField(db_index=True, default=0, verbose_name='google civic election id')),
                ('is_from_ctcl', models.BooleanField(default=False)),
                ('is_from_vote_usa', models.BooleanField(default=False)),
                ('state_code', models.CharField(db_index=True, max_length=2, null=True, verbose_name='state code returned or calculated')),
                ('date_last_updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='date ballot items last retrieved')),
            ],
        ),
        migrations.CreateModel(
            name='VoterBallotSaved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_id', models.IntegerField(default=0, verbose_name='the voter unique id')),
                ('google_civic_election_id', models.PositiveIntegerField(default=0, verbose_name='google civic election id')),
                ('state_code', models.CharField(max_length=2, null=True, verbose_name='state the ballot item is related to')),
                ('election_description_text', models.CharField(max_length=255, verbose_name='text label for this election')),
                ('election_date', models.DateField(null=True, verbose_name='election start date')),
                ('original_text_for_map_search', models.CharField(max_length=255, verbose_name='address as entered')),
                ('original_text_city', models.CharField(max_length=255, null=True)),
                ('original_text_state', models.CharField(max_length=255, null=True)),
                ('original_text_zip', models.CharField(max_length=255, null=True)),
                ('substituted_address_city', models.CharField(max_length=255, null=True)),
                ('substituted_address_state', models.CharField(max_length=255, null=True)),
                ('substituted_address_zip', models.CharField(max_length=255, null=True)),
                ('substituted_address_nearby', models.CharField(max_length=255, verbose_name='address from nearby ballot_returned')),
                ('is_from_substituted_address', models.BooleanField(default=False)),
                ('is_from_test_ballot', models.BooleanField(default=False)),
                ('polling_location_we_vote_id_source', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='we vote permanent id of the map point this was copied from')),
                ('ballot_returned_we_vote_id', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='ballot_returned we_vote_id this was copied from')),
                ('ballot_location_display_name', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='the name of the ballot the voter is looking at')),
                ('ballot_location_shortcut', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='the url string used to find specific ballot')),
            ],
        ),
    ]
