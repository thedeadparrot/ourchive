# Generated by Django 2.2.6 on 2019-11-30 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20191117_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.BookmarkCollection'),
        ),
    ]
