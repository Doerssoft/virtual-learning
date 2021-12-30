# Generated by Django 3.2.9 on 2021-12-23 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(default=1, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='full_name',
            field=models.CharField(default=1, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=756),
        ),
    ]
