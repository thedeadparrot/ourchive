# Generated by Django 4.1.5 on 2023-01-26 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='draft',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='work',
            name='draft',
            field=models.BooleanField(default=True),
        ),
    ]
