# Generated by Django 2.0.4 on 2018-04-22 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterUniqueTogether(
            name='guest',
            unique_together={('event', 'phone')},
        ),
    ]
