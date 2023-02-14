# -*- coding: utf-8 -*-
from uuid import uuid4

import calendar
from datetime import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from basedosdados_api.api.v1.utils import (
    check_kebab_case,
    check_snake_case,
)


class Area(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return str(self.slug)

    class Meta:
        db_table = "area"
        verbose_name = "Area"
        verbose_name_plural = "Areas"
        ordering = ["slug"]


class Coverage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    area = models.ForeignKey("Area", on_delete=models.CASCADE, related_name="coverages")
    temporal_coverages = models.ManyToManyField(
        "TemporalCoverage", related_name="coverages"
    )

    def __str__(self):
        return str(self.temporal_coverages)

    class Meta:
        db_table = "coverage"
        verbose_name = "Coverage"
        verbose_name_plural = "Coverages"
        ordering = ["id"]


class License(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return str(self.slug)

    class Meta:
        db_table = "license"
        verbose_name = "License"
        verbose_name_plural = "Licenses"
        ordering = ["slug"]


class Key(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    coverages = models.ManyToManyField("Coverage", related_name="keys")
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "keys"
        verbose_name = "Key"
        verbose_name_plural = "Keys"
        ordering = ["name"]


class Pipeline(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    github_url = models.URLField()

    def __str__(self):
        return str(self.github_url)

    class Meta:
        db_table = "pipeline"
        verbose_name = "Pipeline"
        verbose_name_plural = "Pipelines"
        ordering = ["github_url"]


class AnalysisType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "analysis_type"
        verbose_name = "Analysis Type"
        verbose_name_plural = "Analysis Types"
        ordering = ["name"]


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.slug)

    class Meta:
        db_table = "tag"
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["slug"]


class Theme(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    logo_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.slug)

    class Meta:
        db_table = "theme"
        verbose_name = "Theme"
        verbose_name_plural = "Themes"
        ordering = ["slug"]


class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    area = models.ForeignKey(
        "Area", on_delete=models.CASCADE, related_name="organizations"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return str(self.slug)

    class Meta:
        db_table = "organization"
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        ordering = ["slug"]


class Dataset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    organization = models.ForeignKey(
        "Organization", on_delete=models.CASCADE, related_name="datasets"
    )
    themes = models.ManyToManyField("Theme", related_name="datasets")
    tags = models.ManyToManyField("Tag", related_name="datasets")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.slug)

    class Meta:
        db_table = "dataset"
        verbose_name = "Dataset"
        verbose_name_plural = "Datasets"
        ordering = ["slug"]


class UpdateFrequency(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    entity = models.ForeignKey(
        "Entity", on_delete=models.CASCADE, related_name="update_frequencies"
    )
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)

    class Meta:
        db_table = "update_frequency"
        verbose_name = "Update Frequency"
        verbose_name_plural = "Update Frequencies"
        ordering = ["number"]


class Table(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    dataset = models.ForeignKey(
        "Dataset", on_delete=models.CASCADE, related_name="tables"
    )
    coverages = models.ManyToManyField("Coverage", related_name="tables")
    license = models.ForeignKey(
        "License", on_delete=models.CASCADE, related_name="tables"
    )
    partner_organization = models.ForeignKey(
        "Organization", on_delete=models.CASCADE, related_name="partner_tables"
    )
    update_frequency = models.ForeignKey(
        "UpdateFrequency", on_delete=models.CASCADE, related_name="tables"
    )
    pipeline = models.ForeignKey(
        "Pipeline", on_delete=models.CASCADE, related_name="tables"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_directory = models.BooleanField(default=False, blank=True, null=True)
    data_cleaning_description = models.TextField(blank=True, null=True)
    data_cleaning_code_url = models.URLField(blank=True, null=True)
    raw_data_url = models.URLField(blank=True, null=True)
    auxiliary_files_url = models.URLField(blank=True, null=True)
    architecture_url = models.URLField(blank=True, null=True)
    source_bucket_name = models.CharField(max_length=255, blank=True, null=True)
    uncompressed_file_size = models.BigIntegerField(blank=True, null=True)
    compressed_file_size = models.BigIntegerField(blank=True, null=True)
    number_rows = models.BigIntegerField(blank=True, null=True)
    number_columns = models.BigIntegerField(blank=True, null=True)
    observation_level = models.ManyToManyField(
        "ObservationLevel", related_name="tables", blank=True
    )

    def __str__(self):
        return str(self.slug)

    class Meta:
        db_table = "table"
        verbose_name = "Table"
        verbose_name_plural = "Tables"
        ordering = ["slug"]


class BigQueryTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "bigquery_types"
        verbose_name = "BigQuery Type"
        verbose_name_plural = "BigQuery Types"
        ordering = ["name"]


class Column(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    table = models.ForeignKey("Table", on_delete=models.CASCADE, related_name="columns")
    bigquery_type = models.ForeignKey(
        "BigQueryTypes", on_delete=models.CASCADE, related_name="columns"
    )
    coverages = models.ManyToManyField("Coverage", related_name="columns")
    directory_primary_key = models.ForeignKey(
        "Column",
        on_delete=models.PROTECT,
        related_name="columns",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=255)
    is_in_staging = models.BooleanField(default=True)
    is_partition = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    covered_by_dictionary = models.BooleanField(default=False, blank=True, null=True)
    measurement_unit = models.CharField(max_length=255, blank=True, null=True)
    contains_sensitive_data = models.BooleanField(default=False, blank=True, null=True)
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "column"
        verbose_name = "Column"
        verbose_name_plural = "Columns"
        ordering = ["name"]


class Dictionary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    column = models.OneToOneField(
        "Column", on_delete=models.CASCADE, related_name="dictionary"
    )
    keys = models.ForeignKey(
        "Key", on_delete=models.CASCADE, related_name="dictionaries"
    )


class CloudTable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    table = models.ForeignKey(
        "Table", on_delete=models.CASCADE, related_name="cloud_tables"
    )
    columns = models.ManyToManyField("Column", related_name="cloud_tables")
    gcp_project_id = models.CharField(max_length=255)
    gcp_dataset_id = models.CharField(max_length=255)
    gcp_table_id = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.gcp_project_id}.{self.gcp_dataset_id}.{self.gcp_table_id}"

    def clean(self) -> None:
        errors = {}
        if self.gcp_project_id and not check_kebab_case(self.gcp_project_id):
            errors["gcp_project_id"] = "gcp_project_id must be in kebab-case."
        if self.gcp_project_id and not check_snake_case(self.gcp_dataset_id):
            errors["gcp_dataset_id"] = "gcp_dataset_id must be in snake_case."
        if self.gcp_table_id and not check_snake_case(self.gcp_table_id):
            errors["gcp_table_id"] = "gcp_table_id must be in snake_case."
        for column in self.columns.all():
            if column.table != self.table:
                errors[
                    "columns"
                ] = f"Column {column} does not belong to table {self.table}."
        if errors:
            raise ValidationError(errors)

        return super().clean()

    class Meta:
        db_table = "cloud_table"
        verbose_name = "Cloud Table"
        verbose_name_plural = "Cloud Tables"
        ordering = ["id"]


class Availability(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.slug)

    class Meta:
        db_table = "availability"
        verbose_name = "Availability"
        verbose_name_plural = "Availabilities"
        ordering = ["slug"]


class Language(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.slug)

    class Meta:
        db_table = "language"
        verbose_name = "Language"
        verbose_name_plural = "Languages"
        ordering = ["slug"]


class RawDataSource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    dataset = models.ForeignKey(
        "Dataset", on_delete=models.CASCADE, related_name="raw_data_sources"
    )
    coverages = models.ManyToManyField("Coverage", related_name="raw_data_sources")
    availability = models.ForeignKey(
        "Availability", on_delete=models.CASCADE, related_name="raw_data_sources"
    )
    languages = models.ManyToManyField(
        "Language", related_name="raw_data_sources", blank=True
    )
    license = models.ForeignKey(
        "License", on_delete=models.CASCADE, related_name="raw_data_sources"
    )
    update_frequency = models.ForeignKey(
        "UpdateFrequency", on_delete=models.CASCADE, related_name="raw_data_sources"
    )
    area_ip_address_required = models.ManyToManyField(
        "Area", related_name="raw_data_sources", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    contains_structure_data = models.BooleanField(default=False)
    contains_api = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)
    required_registration = models.BooleanField(default=False)
    observation_level = models.ManyToManyField(
        "ObservationLevel", related_name="raw_data_sources", blank=True
    )

    def __str__(self):
        return str(self.slug)

    class Meta:
        db_table = "raw_data_source"
        verbose_name = "Raw Data Source"
        verbose_name_plural = "Raw Data Sources"
        ordering = ["slug"]


class Status(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.slug)

    class Meta:
        db_table = "status"
        verbose_name = "Status"
        verbose_name_plural = "Statuses"
        ordering = ["slug"]


class InformationRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    dataset = models.ForeignKey(
        "Dataset", on_delete=models.CASCADE, related_name="information_requests"
    )
    coverages = models.ManyToManyField("Coverage", related_name="information_requests")
    status = models.ForeignKey(
        "Status", on_delete=models.CASCADE, related_name="information_requests"
    )
    update_frequency = models.ForeignKey(
        "UpdateFrequency", on_delete=models.CASCADE, related_name="information_requests"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    origin = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    data_url = models.URLField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    observation_level = models.ManyToManyField(
        "ObservationLevel", related_name="information_requests", blank=True
    )
    started_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="information_requests"
    )

    def __str__(self):
        return str(self.slug)

    class Meta:
        db_table = "information_request"
        verbose_name = "Information Request"
        verbose_name_plural = "Information Requests"
        ordering = ["slug"]


class Entity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.slug)

    class Meta:
        db_table = "entity"
        verbose_name = "Entity"
        verbose_name_plural = "Entities"
        ordering = ["slug"]


class ObservationLevel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    entity = models.ForeignKey(
        "Entity", on_delete=models.CASCADE, related_name="observation_levels"
    )
    columns = models.ManyToManyField(
        "Column", related_name="observation_levels", blank=True
    )

    def __str__(self):
        return str(self.entity)


class TemporalCoverage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    slug = models.SlugField(unique=True)
    start_year = models.IntegerField()
    start_semester = models.IntegerField(blank=True, null=True)
    start_quarter = models.IntegerField(blank=True, null=True)
    start_month = models.IntegerField(blank=True, null=True)
    start_day = models.IntegerField(blank=True, null=True)
    start_hour = models.IntegerField(blank=True, null=True)
    start_minute = models.IntegerField(blank=True, null=True)
    start_second = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField()
    end_semester = models.IntegerField(blank=True, null=True)
    end_quarter = models.IntegerField(blank=True, null=True)
    end_month = models.IntegerField(blank=True, null=True)
    end_day = models.IntegerField(blank=True, null=True)
    end_hour = models.IntegerField(blank=True, null=True)
    end_minute = models.IntegerField(blank=True, null=True)
    end_second = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.slug)

    def clean(self) -> None:
        errors = {}
        # This validation is not necessary, as Django handles it
        # if self.start_year is None or self.end_year is None:
        #     errors[""] = ["Start year and end year are required"]
        #     raise ValidationError("Start year and end year are required")

        if (self.start_year and self.end_year) and self.start_year > self.end_year:
            errors["start_year"] = ["Start year cannot be greater than end year"]
            # raise ValidationError("Start year cannot be greater than end year")

        try:
            start_datetime = datetime(
                self.start_year,
                self.start_month or 1,
                self.start_day or 1,
                self.start_hour or 0,
                self.start_minute or 0,
                self.start_second or 0,
            )
            end_datetime = datetime(
                self.end_year,
                self.end_month or 1,
                self.end_day or 1,
                self.end_hour or 0,
                self.end_minute or 0,
                self.end_second or 0,
            )
            if start_datetime > end_datetime:
                errors["start_year"] = ["Start datetime cannot be greater than end datetime"]
                # raise ValidationError("Start year cannot be greater than end year")

        except TypeError:
            errors["start_year"] = ["Start year or end year are invalid"]

        if self.start_day:
            max_day = calendar.monthrange(self.start_year, self.start_month)[1]
            if self.start_day > max_day:
                errors["start_day"] = [
                    f"{self.start_month} does not have {self.start_day} days in {self.start_year}"
                ]
                # raise ValidationError(
                #     f"{self.start_month} does not have {self.start_day} days in {self.start_year}"
                # )

        if self.end_day:
            max_day = calendar.monthrange(self.end_year, self.end_month)[1]
            if self.end_day > max_day:
                errors["end_day"] = [
                    f"{self.end_month} does not have {self.end_day} days in {self.end_year}"
                ]
                # raise ValidationError(
                #     f"{self.end_month} does not have {self.end_day} days in {self.end_year}"
                # )

        if self.start_semester:
            if self.start_semester > 2:
                errors["start_semester"] = ["Semester cannot be greater than 2"]
                # raise ValidationError("Semester cannot be greater than 2")

        if self.end_semester:
            if self.end_semester > 2:
                errors["end_semester"] = ["Semester cannot be greater than 2"]
                # raise ValidationError("Semester cannot be greater than 2")

        if self.start_quarter:
            if self.start_quarter > 4:
                errors["start_quarter"] = ["Quarter cannot be greater than 4"]
                # raise ValidationError("Quarter cannot be greater than 4")

        if self.end_quarter:
            if self.end_quarter > 4:
                errors["end_quarter"] = ["Quarter cannot be greater than 4"]
                # raise ValidationError("Quarter cannot be greater than 4")

        if self.start_month:
            if self.start_month > 12:
                errors["start_month"] = ["Month cannot be greater than 12"]
                # raise ValidationError("Month cannot be greater than 12")

        if self.end_month:
            if self.end_month > 12:
                errors["end_month"] = ["Month cannot be greater than 12"]
                # raise ValidationError("Month cannot be greater than 12")

        if errors:
            raise ValidationError(errors)

        return super().clean()

    class Meta:
        db_table = "temporal_coverage"
        verbose_name = "Temporal Coverage"
        verbose_name_plural = "Temporal Coverages"
        ordering = ["slug"]
