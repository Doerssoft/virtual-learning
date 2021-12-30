# Generated by Django 3.2.9 on 2021-12-19 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auhor_name', models.CharField(max_length=75)),
                ('mesage_from_author', models.TextField(max_length=1000)),
                ('about_author', models.TextField(max_length=1000)),
                ('author_image', models.ImageField(blank=True, null=True, upload_to='author_image')),
                ('author_fb_link', models.URLField(max_length=500)),
                ('author_twitter_link', models.URLField(max_length=500)),
                ('author_google_link', models.URLField(max_length=500)),
                ('author_linkedin_link', models.URLField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='author_fb_link',
        ),
        migrations.RemoveField(
            model_name='course',
            name='social_link',
        ),
        migrations.AlterField(
            model_name='course',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_author', to='courses.author'),
        ),
    ]