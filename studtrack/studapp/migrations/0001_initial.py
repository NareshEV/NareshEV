# Generated by Django 4.0.3 on 2022-05-12 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('stuid', models.IntegerField(primary_key=True, serialize=False)),
                ('stuname', models.CharField(max_length=30)),
                ('studcourse', models.CharField(max_length=20)),
                ('staff', models.CharField(max_length=30)),
                ('chapter', models.IntegerField()),
                ('present', models.CharField(max_length=5)),
                ('date', models.IntegerField()),
                ('duration', models.IntegerField()),
            ],
        ),
    ]