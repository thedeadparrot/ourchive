# Generated by Django 4.2.1 on 2023-06-21 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_invitation_join_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cookies_accepted',
            field=models.BooleanField(default=False),
        ),
    ]