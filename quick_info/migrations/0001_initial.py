# Generated by Django 3.2.13 on 2022-06-10 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuickInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('we_vote_id', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='we vote permanent id')),
                ('language', models.CharField(choices=[('en', 'English'), ('es', 'Spanish'), ('tl', 'Tagalog'), ('vi', 'Vietnamese'), ('zh', 'Chinese')], default='en', max_length=5)),
                ('info_text', models.TextField(blank=True, null=True)),
                ('info_html', models.TextField(blank=True, null=True)),
                ('ballot_item_display_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='text name for ballot item for quick display')),
                ('more_info_credit', models.CharField(blank=True, choices=[('not_specified', 'Not Specified'), ('ballotpedia', 'Ballotpedia'), ('direct', 'Direct Entry'), ('wikipedia', 'Wikipedia')], default='not_specified', max_length=15, null=True)),
                ('more_info_url', models.URLField(blank=True, null=True, verbose_name='url with more the full entry for this info')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='date entered')),
                ('last_editor_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='last editor we vote id')),
                ('contest_office_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='we vote permanent id for the contest_office')),
                ('candidate_campaign_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='we vote permanent id for the candidate')),
                ('politician_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='we vote permanent id for politician')),
                ('contest_measure_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='we vote permanent id for the contest_measure')),
                ('quick_info_master_we_vote_id', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='we vote id of other entry which is the master')),
                ('google_civic_election_id', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='google civic election id')),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
        migrations.CreateModel(
            name='QuickInfoMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('we_vote_id', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='we vote permanent id')),
                ('kind_of_ballot_item', models.CharField(choices=[('OFFICE', 'Office'), ('CANDIDATE', 'Candidate'), ('POLITICIAN', 'Politician'), ('MEASURE', 'Measure')], default='OFFICE', max_length=10)),
                ('language', models.CharField(choices=[('en', 'English'), ('es', 'Spanish'), ('tl', 'Tagalog'), ('vi', 'Vietnamese'), ('zh', 'Chinese')], default='en', max_length=5)),
                ('info_text', models.TextField(blank=True, null=True)),
                ('info_html', models.TextField(blank=True, null=True)),
                ('master_entry_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='text name for quick info master entry')),
                ('more_info_credit', models.CharField(blank=True, choices=[('not_specified', 'Not Specified'), ('ballotpedia', 'Ballotpedia'), ('direct', 'Direct Entry'), ('wikipedia', 'Wikipedia')], default='ballotpedia', max_length=15, null=True)),
                ('more_info_url', models.URLField(blank=True, null=True, verbose_name='url with more the full entry for this info')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='date entered')),
                ('last_editor_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='last editor we vote id')),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
    ]
