# Generated by Django 2.2.17 on 2021-02-21 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommunistParty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('acronym', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='')),
                ('url', models.CharField(max_length=80)),
                ('foundation_date', models.DateField(auto_now_add=True)),
                ('ambit', models.CharField(max_length=80)),
            ],
        ),
    ]
