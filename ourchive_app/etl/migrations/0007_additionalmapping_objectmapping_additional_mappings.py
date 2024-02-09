# Generated by Django 4.2.4 on 2023-09-02 20:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0006_alter_objectmapping_object_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalMapping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('original_value', models.CharField(max_length=300)),
                ('destination_object', models.CharField(choices=[('tag', 'tag'), ('attribute', 'attribute')], max_length=100)),
                ('destination_value', models.CharField(max_length=120)),
                ('destination_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='objectmapping',
            name='additional_mappings',
            field=models.BooleanField(default=False),
        ),
    ]
