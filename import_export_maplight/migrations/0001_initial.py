# Generated by Django 3.2.13 on 2022-06-10 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MapLightCandidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_id', models.IntegerField(unique=True, verbose_name='candidate id')),
                ('display_name', models.CharField(max_length=255, verbose_name='display name')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='first name')),
                ('gender', models.CharField(default='U', max_length=1, verbose_name='gender')),
                ('last_funding_update', models.DateField(blank=True, default=None, null=True, verbose_name='last funding update date')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='last name')),
                ('middle_name', models.CharField(max_length=255, verbose_name='middle name')),
                ('name_prefix', models.CharField(blank=True, max_length=255, verbose_name='name prefix')),
                ('name_suffix', models.CharField(blank=True, max_length=255, verbose_name='name suffix')),
                ('original_name', models.CharField(blank=True, max_length=255, verbose_name='original name')),
                ('party', models.CharField(blank=True, max_length=255, verbose_name='political party')),
                ('photo', models.CharField(blank=True, max_length=255, verbose_name='photo url')),
                ('politician_id', models.IntegerField(unique=True, verbose_name='politician id')),
                ('roster_name', models.CharField(blank=True, max_length=255, verbose_name='roster name')),
                ('type', models.CharField(blank=True, max_length=255, verbose_name='type')),
                ('url', models.CharField(blank=True, max_length=255, verbose_name='url')),
            ],
        ),
        migrations.CreateModel(
            name='MapLightContestOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_date', models.DateField(blank=True, default=None, null=True, verbose_name='election date')),
                ('contest_id', models.CharField(max_length=255, unique=True, verbose_name='contest id')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('type', models.CharField(max_length=255, verbose_name='type')),
                ('url', models.CharField(max_length=255, verbose_name='url')),
            ],
        ),
    ]
