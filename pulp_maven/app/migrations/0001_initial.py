# Generated by Django 2.2.3 on 2019-08-04 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [("core", "0003_remove_upload_completed")]

    operations = [
        migrations.CreateModel(
            name="MavenDistribution",
            fields=[
                (
                    "basedistribution_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.BaseDistribution",
                    ),
                )
            ],
            options={"abstract": False},
            bases=("core.basedistribution",),
        ),
        migrations.CreateModel(
            name="MavenRemote",
            fields=[
                (
                    "remote_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.Remote",
                    ),
                )
            ],
            options={"abstract": False},
            bases=("core.remote",),
        ),
        migrations.CreateModel(
            name="MavenArtifact",
            fields=[
                (
                    "content_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.Content",
                    ),
                ),
                ("group_id", models.CharField(max_length=255)),
                ("artifact_id", models.CharField(max_length=255)),
                ("version", models.CharField(max_length=255)),
                ("filename", models.CharField(max_length=255)),
            ],
            options={
                "unique_together": {("group_id", "artifact_id", "version", "filename")}
            },
            bases=("core.content",),
        ),
    ]
