# Generated by Django 3.2.13 on 2022-06-10 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentFriend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewer_voter_we_vote_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='voter we vote id person 1')),
                ('viewer_organization_we_vote_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('viewee_voter_we_vote_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='voter we vote id person 2')),
                ('viewee_organization_we_vote_id', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('date_last_changed', models.DateTimeField(auto_now=True, null=True, verbose_name='date last changed')),
            ],
        ),
        migrations.CreateModel(
            name='FriendInvitationEmailLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_voter_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='we vote id for the sender')),
                ('sender_email_ownership_is_verified', models.BooleanField(default=False)),
                ('recipient_email_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='email we vote id for recipient')),
                ('recipient_voter_email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='email address for recipient')),
                ('recipient_first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='first name')),
                ('recipient_last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='last name')),
                ('secret_key', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='secret key to accept invite')),
                ('invitation_message', models.TextField(blank=True, null=True)),
                ('invitation_status', models.CharField(choices=[('PENDING_EMAIL_VERIFICATION', 'Pending verification of your email'), ('NO_RESPONSE', 'No response yet'), ('ACCEPTED', 'Invitation accepted'), ('IGNORED', 'Voter invited chose to ignore the invitation')], default='NO_RESPONSE', max_length=50)),
                ('date_last_changed', models.DateTimeField(auto_now=True, null=True, verbose_name='date last changed')),
                ('merge_by_secret_key_allowed', models.BooleanField(default=True)),
                ('invitation_table', models.CharField(default='EMAIL', max_length=8)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FriendInvitationFacebookLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_facebook_id', models.BigIntegerField(blank=True, null=True, verbose_name='facebook user id of sender')),
                ('recipient_facebook_id', models.BigIntegerField(blank=True, null=True, verbose_name='facebook user id of recipient')),
                ('recipient_facebook_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='recipient facebook full name')),
                ('facebook_request_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='facebook app request id')),
                ('invitation_status', models.CharField(choices=[('PENDING_EMAIL_VERIFICATION', 'Pending verification of your email'), ('NO_RESPONSE', 'No response yet'), ('ACCEPTED', 'Invitation accepted'), ('IGNORED', 'Voter invited chose to ignore the invitation')], default='NO_RESPONSE', max_length=50)),
                ('date_last_changed', models.DateTimeField(auto_now=True, null=True, verbose_name='date last changed')),
                ('invitation_table', models.CharField(default='FACEBOOK', max_length=8)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FriendInvitationTwitterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_voter_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='we vote id for the sender')),
                ('recipient_twitter_handle', models.CharField(max_length=255, verbose_name='twitter screen_name')),
                ('secret_key', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='secret key to accept invite')),
                ('invitation_message', models.TextField(blank=True, null=True)),
                ('invitation_status', models.CharField(choices=[('PENDING_EMAIL_VERIFICATION', 'Pending verification of your email'), ('NO_RESPONSE', 'No response yet'), ('ACCEPTED', 'Invitation accepted'), ('IGNORED', 'Voter invited chose to ignore the invitation')], default='NO_RESPONSE', max_length=50)),
                ('date_last_changed', models.DateTimeField(auto_now=True, null=True, verbose_name='date last changed')),
                ('merge_by_secret_key_allowed', models.BooleanField(default=True)),
                ('invitation_table', models.CharField(default='TWITTER', max_length=8)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FriendInvitationVoterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_voter_we_vote_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='we vote id for the sender')),
                ('sender_email_ownership_is_verified', models.BooleanField(default=False)),
                ('recipient_voter_we_vote_id', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='we vote id for the recipient if we have it')),
                ('secret_key', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='secret key to accept invite')),
                ('invitation_message', models.TextField(blank=True, null=True)),
                ('invitation_status', models.CharField(choices=[('PENDING_EMAIL_VERIFICATION', 'Pending verification of your email'), ('NO_RESPONSE', 'No response yet'), ('ACCEPTED', 'Invitation accepted'), ('IGNORED', 'Voter invited chose to ignore the invitation')], default='NO_RESPONSE', max_length=50)),
                ('date_last_changed', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='date last changed')),
                ('merge_by_secret_key_allowed', models.BooleanField(default=True)),
                ('invitation_table', models.CharField(default='VOTER', max_length=8)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SuggestedFriend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewer_voter_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='voter we vote id person 1')),
                ('viewee_voter_we_vote_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='voter we vote id person 2')),
                ('voter_we_vote_id_deleted_first', models.CharField(blank=True, max_length=255, null=True, verbose_name='first voter to remove suggested friend')),
                ('voter_we_vote_id_deleted_second', models.CharField(blank=True, max_length=255, null=True, verbose_name='second voter to remove suggested friend')),
                ('friend_invite_sent', models.BooleanField(default=False)),
                ('current_friends', models.BooleanField(default=False)),
                ('date_last_changed', models.DateTimeField(auto_now=True, null=True, verbose_name='date last changed')),
            ],
        ),
    ]