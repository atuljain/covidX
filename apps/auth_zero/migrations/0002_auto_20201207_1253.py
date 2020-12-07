# Generated by Django 3.0.7 on 2020-12-07 12:53
import django.contrib.auth.models
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_zero", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdminUser",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("auth_zero.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="PatientUser",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("auth_zero.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="StaffUser",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("auth_zero.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="SupportUser",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("auth_zero.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="user_type",
            field=models.CharField(default="PATIENT", max_length=20),
        ),
    ]