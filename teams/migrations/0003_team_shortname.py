# Generated by Django 4.1.3 on 2022-12-18 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0002_team_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="shortname",
            field=models.CharField(max_length=3, null=True),
        ),
    ]
