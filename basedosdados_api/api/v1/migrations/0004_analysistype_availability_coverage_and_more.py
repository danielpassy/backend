# -*- coding: utf-8 -*-
# Generated by Django 4.1.3 on 2023-01-19 19:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("v1", "0003_area_organization_area"),
    ]

    operations = [
        migrations.CreateModel(
            name="AnalysisType",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("name_en", models.CharField(max_length=255)),
                ("name_pt", models.CharField(max_length=255)),
                ("tag_en", models.CharField(max_length=255)),
                ("tag_pt", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Analysis Type",
                "verbose_name_plural": "Analysis Types",
                "db_table": "analysis_type",
                "ordering": ["name_pt"],
            },
        ),
        migrations.CreateModel(
            name="Availability",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                ("name_en", models.CharField(max_length=255)),
                ("name_pt", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Coverage",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("temporal_coverage", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Coverage",
                "verbose_name_plural": "Coverages",
                "db_table": "coverage",
                "ordering": ["temporal_coverage"],
            },
        ),
        migrations.CreateModel(
            name="DirectoryPrimaryKey",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "verbose_name": "Directory Primary Key",
                "verbose_name_plural": "Directory Primary Keys",
                "db_table": "directory_primary_key",
                "ordering": ["slug"],
            },
        ),
        migrations.CreateModel(
            name="Entity",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                ("name_en", models.CharField(max_length=255)),
                ("name_pt", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Entity",
                "verbose_name_plural": "Entities",
                "db_table": "entity",
                "ordering": ["slug"],
            },
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                ("name_en", models.CharField(max_length=255)),
                ("name_pt", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="License",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                ("name_en", models.CharField(max_length=255)),
                ("name_pt", models.CharField(max_length=255)),
                ("url", models.URLField()),
            ],
            options={
                "verbose_name": "License",
                "verbose_name_plural": "Licenses",
                "db_table": "license",
                "ordering": ["slug"],
            },
        ),
        migrations.CreateModel(
            name="Status",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                ("name_en", models.CharField(max_length=255)),
                ("name_pt", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Status",
                "verbose_name_plural": "Statuses",
                "db_table": "status",
                "ordering": ["slug"],
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                ("name_en", models.CharField(max_length=255)),
                ("name_pt", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Tag",
                "verbose_name_plural": "Tags",
                "db_table": "tag",
                "ordering": ["slug"],
            },
        ),
        migrations.CreateModel(
            name="Theme",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                ("name_en", models.CharField(max_length=255)),
                ("name_pt", models.CharField(max_length=255)),
                ("logo_url", models.URLField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Theme",
                "verbose_name_plural": "Themes",
                "db_table": "theme",
                "ordering": ["slug"],
            },
        ),
        migrations.CreateModel(
            name="TimeUnit",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                ("name_en", models.CharField(max_length=255)),
                ("name_pt", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Time Unit",
                "verbose_name_plural": "Time Units",
                "db_table": "time_unit",
                "ordering": ["slug"],
            },
        ),
        migrations.AddField(
            model_name="area",
            name="area_ip_address_required",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="UpdateFrequency",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("number", models.IntegerField()),
                (
                    "time_unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="update_frequencies",
                        to="v1.timeunit",
                    ),
                ),
            ],
            options={
                "verbose_name": "Update Frequency",
                "verbose_name_plural": "Update Frequencies",
                "db_table": "update_frequency",
                "ordering": ["number"],
            },
        ),
        migrations.CreateModel(
            name="ObservationLevel",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "entity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="observation_levels",
                        to="v1.entity",
                    ),
                ),
                (
                    "information_requests",
                    models.ManyToManyField(
                        related_name="entity_columns", to="v1.informationrequest"
                    ),
                ),
                (
                    "raw_data_sources",
                    models.ManyToManyField(
                        related_name="entity_columns", to="v1.rawdatasource"
                    ),
                ),
                (
                    "tables",
                    models.ManyToManyField(
                        related_name="entity_columns", to="v1.table"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Key",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("value", models.CharField(max_length=255)),
                (
                    "coverages",
                    models.ManyToManyField(related_name="keys", to="v1.coverage"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EntityColumn",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "column",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="entity_columns",
                        to="v1.column",
                    ),
                ),
                (
                    "entity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="entity_columns",
                        to="v1.entity",
                    ),
                ),
                (
                    "observation_level",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="entity_columns",
                        to="v1.observationlevel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Dictionary",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "column",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dictionary",
                        to="v1.column",
                    ),
                ),
                (
                    "keys",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dictionaries",
                        to="v1.key",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="coverage",
            name="area",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="coverages",
                to="v1.area",
            ),
        ),
        migrations.AddField(
            model_name="column",
            name="directory_primary_key",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="columns",
                to="v1.directoryprimarykey",
            ),
        ),
        migrations.AddField(
            model_name="informationrequest",
            name="status",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="information_requests",
                to="v1.status",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="informationrequest",
            name="update_frequency",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="information_requests",
                to="v1.updatefrequency",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="rawdatasource",
            name="availability",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="raw_data_sources",
                to="v1.availability",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="rawdatasource",
            name="languages",
            field=models.ManyToManyField(
                blank=True, related_name="raw_data_sources", to="v1.language"
            ),
        ),
        migrations.AddField(
            model_name="rawdatasource",
            name="license",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="raw_data_sources",
                to="v1.license",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="rawdatasource",
            name="update_frequency",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="raw_data_sources",
                to="v1.updatefrequency",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="table",
            name="license",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tables",
                to="v1.license",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="table",
            name="update_frequency",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tables",
                to="v1.updatefrequency",
            ),
            preserve_default=False,
        ),
    ]
