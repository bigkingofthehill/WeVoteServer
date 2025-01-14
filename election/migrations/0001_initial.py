# Generated by Django 3.2.13 on 2022-06-10 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BallotpediaElection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ballotpedia_election_id', models.PositiveIntegerField(null=True, unique=True, verbose_name='ballotpedia election id')),
                ('google_civic_election_id', models.PositiveIntegerField(null=True, verbose_name='google civic election id')),
                ('election_description', models.CharField(max_length=255, null=True, verbose_name='election description')),
                ('election_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='election type')),
                ('election_day_text', models.CharField(blank=True, max_length=255, null=True, verbose_name='election day')),
                ('ocd_division_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='ocd division id')),
                ('district_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='district name')),
                ('district_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='district type')),
                ('state_code', models.CharField(blank=True, max_length=2, null=True, verbose_name='state code for the election')),
                ('is_general_election', models.BooleanField(default=False)),
                ('is_general_runoff_election', models.BooleanField(default=False)),
                ('is_primary_election', models.BooleanField(default=False)),
                ('is_primary_runoff_election', models.BooleanField(default=False)),
                ('is_partisan', models.BooleanField(default=False)),
                ('candidate_lists_complete', models.BooleanField(default=False)),
                ('internal_notes', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_civic_election_id', models.CharField(max_length=20, null=True, unique=True, verbose_name='google civic election id')),
                ('google_civic_election_id_new', models.PositiveIntegerField(null=True, verbose_name='google civic election id')),
                ('ballotpedia_election_id', models.PositiveIntegerField(null=True, unique=True, verbose_name='ballotpedia election id')),
                ('ctcl_uuid', models.CharField(blank=True, max_length=36, null=True, verbose_name='ctcl uuid')),
                ('election_name', models.CharField(max_length=255, verbose_name='election name')),
                ('election_day_text', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='election day')),
                ('ocd_division_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='ocd division id')),
                ('ballotpedia_kind_of_election', models.CharField(blank=True, max_length=255, null=True, verbose_name='election filter')),
                ('state_code', models.CharField(blank=True, db_index=True, max_length=2, null=True, verbose_name='state code for the election')),
                ('state_code_list_raw', models.CharField(blank=True, max_length=255, null=True)),
                ('include_in_list_for_voters', models.BooleanField(default=False)),
                ('internal_notes', models.TextField(blank=True, default=None, null=True)),
                ('ignore_this_election', models.BooleanField(default=False)),
                ('election_preparation_finished', models.BooleanField(default=False)),
                ('candidate_photos_finished', models.BooleanField(default=False)),
                ('is_national_election', models.BooleanField(default=False)),
                ('use_ballotpedia_as_data_source', models.BooleanField(default=False)),
                ('use_ctcl_as_data_source', models.BooleanField(default=False)),
                ('use_ctcl_as_data_source_by_state_code', models.CharField(blank=True, max_length=255, null=True)),
                ('use_google_civic_as_data_source', models.BooleanField(default=False)),
                ('use_vote_usa_as_data_source', models.BooleanField(default=False)),
                ('vote_usa_election_id', models.CharField(max_length=255, null=True)),
                ('vote_usa_same_day_election_suffix_list', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
