# Generated by Django 4.1.5 on 2023-01-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_bookmark_draft_work_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='draft',
            field=models.BooleanField(default=True),
        ),
    ]
