# Generated by Django 4.2.1 on 2023-06-24 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_userreport_resolved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userreport',
            options={'ordering': ['resolved', 'updated_on']},
        ),
        migrations.AlterModelOptions(
            name='userreportreason',
            options={'ordering': ['reason']},
        ),
    ]