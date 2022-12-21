# -*- coding: utf-8 -*-
from rest_framework import permissions, viewsets

from basedosdados_api.api.v1.models import (
    Organization,
    Dataset,
    Table,
    InformationRequest,
    RawDataSource,
    BigQueryTypes,
    Column,
    CloudTable,
)
from basedosdados_api.api.v1.serializers import (
    OrganizationPublicSerializer,
    OrganizationSerializer,
    DatasetPublicSerializer,
    DatasetSerializer,
    TablePublicSerializer,
    TableSerializer,
    InformationRequestPublicSerializer,
    InformationRequestSerializer,
    RawDataSourcePublicSerializer,
    RawDataSourceSerializer,
    BigQueryTypesPublicSerializer,
    BigQueryTypesSerializer,
    ColumnPublicSerializer,
    ColumnSerializer,
    CloudTablePublicSerializer,
    CloudTableSerializer,
)


class OrganizationReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationPublicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrganizationViewSet(viewsets.ModelViewSet, OrganizationReadOnlyViewSet):
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]


class DatasetReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DatasetPublicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Dataset.objects.all()
        organization = self.request.query_params.get("organization", None)
        if organization is not None:
            queryset = queryset.filter(organization__id=organization)
        return queryset


class DatasetViewSet(viewsets.ModelViewSet, DatasetReadOnlyViewSet):
    serializer_class = DatasetSerializer
    permission_classes = [permissions.IsAuthenticated]


class TableReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TablePublicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Table.objects.all()
        dataset = self.request.query_params.get("dataset", None)
        organization = self.request.query_params.get("organization", None)
        if dataset is not None:
            queryset = queryset.filter(dataset__id=dataset)
        if organization is not None:
            queryset = queryset.filter(dataset__organization__id=organization)
        return queryset


class TableViewSet(viewsets.ModelViewSet, TableReadOnlyViewSet):
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticated]


class InformationRequestReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = InformationRequestPublicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = InformationRequest.objects.all()
        dataset = self.request.query_params.get("dataset", None)
        organization = self.request.query_params.get("organization", None)
        if dataset is not None:
            queryset = queryset.filter(dataset__id=dataset)
        if organization is not None:
            queryset = queryset.filter(dataset__organization__id=organization)
        return queryset


class InformationRequestViewSet(
    viewsets.ModelViewSet, InformationRequestReadOnlyViewSet
):
    serializer_class = InformationRequestSerializer
    permission_classes = [permissions.IsAuthenticated]


class RawDataSourceReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RawDataSourcePublicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = RawDataSource.objects.all()
        dataset = self.request.query_params.get("dataset", None)
        organization = self.request.query_params.get("organization", None)
        if dataset is not None:
            queryset = queryset.filter(dataset__id=dataset)
        if organization is not None:
            queryset = queryset.filter(dataset__organization__id=organization)
        return queryset


class RawDataSourceViewSet(viewsets.ModelViewSet, RawDataSourceReadOnlyViewSet):
    serializer_class = RawDataSourceSerializer
    permission_classes = [permissions.IsAuthenticated]


class BigQueryTypesReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BigQueryTypes.objects.all()
    serializer_class = BigQueryTypesPublicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BigQueryTypesViewSet(viewsets.ModelViewSet, BigQueryTypesReadOnlyViewSet):
    serializer_class = BigQueryTypesSerializer
    permission_classes = [permissions.IsAuthenticated]


class ColumnReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ColumnPublicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Column.objects.all()
        table = self.request.query_params.get("table", None)
        cloud_table = self.request.query_params.get("cloud_table", None)
        dataset = self.request.query_params.get("dataset", None)
        organization = self.request.query_params.get("organization", None)
        if table is not None:
            queryset = queryset.filter(table__id=table)
        if cloud_table is not None:
            # Column has a many-to-many relationship with CloudTable
            # related_name is set to "cloud_tables"
            queryset = queryset.filter(cloud_tables__id=cloud_table)
        if dataset is not None:
            queryset = queryset.filter(table__dataset__id=dataset)
        if organization is not None:
            queryset = queryset.filter(table__dataset__organization__id=organization)
        return queryset


class ColumnViewSet(viewsets.ModelViewSet, ColumnReadOnlyViewSet):
    serializer_class = ColumnSerializer
    permission_classes = [permissions.IsAuthenticated]


class CloudTableReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CloudTablePublicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = CloudTable.objects.all()
        table = self.request.query_params.get("table", None)
        dataset = self.request.query_params.get("dataset", None)
        organization = self.request.query_params.get("organization", None)
        if table is not None:
            queryset = queryset.filter(table__id=table)
        if dataset is not None:
            queryset = queryset.filter(table__dataset__id=dataset)
        if organization is not None:
            queryset = queryset.filter(table__dataset__organization__id=organization)
        return queryset


class CloudTableViewSet(viewsets.ModelViewSet, CloudTableReadOnlyViewSet):
    serializer_class = CloudTableSerializer
    permission_classes = [permissions.IsAuthenticated]
