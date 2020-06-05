# Generated by Django 3.0.6 on 2020-06-05 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('artist', models.CharField(blank=True, max_length=255, null=True)),
                ('album', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.CharField(blank=True, max_length=255, null=True)),
                ('length', models.CharField(blank=True, max_length=255, null=True)),
                ('codec', models.CharField(blank=True, max_length=255, null=True)),
                ('sample_rate', models.CharField(blank=True, max_length=255, null=True)),
                ('bitrate', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.IntegerField(choices=[(1, 'One Star'), (2, 'Two Stars'), (3, 'Three Stars'), (4, 'Four Stars'), (5, 'Five Stars')], null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('path', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
