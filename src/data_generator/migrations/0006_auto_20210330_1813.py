# Generated by Django 3.1.7 on 2021-03-30 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_generator', '0005_remove_column_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='column',
            name='range',
        ),
        migrations.AddField(
            model_name='column',
            name='range_max',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='column',
            name='range_min',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]