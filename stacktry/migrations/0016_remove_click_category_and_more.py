# Generated by Django 4.2.3 on 2023-10-18 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stacktry", "0015_click_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="click",
            name="category",
        ),
        migrations.RemoveField(
            model_name="click",
            name="grappling_participation_count",
        ),
        migrations.RemoveField(
            model_name="click",
            name="jiu_jitsu_participation_count",
        ),
        migrations.RemoveField(
            model_name="click",
            name="kick_boxing_participation_count",
        ),
        migrations.RemoveField(
            model_name="click",
            name="yoga_participation_count",
        ),
    ]
