from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from _apps.product import models, serializers


class CategoryView(viewsets.ViewSet):
    """
    A simple ViewSet for Viewing all categories
    """

    queryset = models.Category.objects.all()

    @extend_schema(responses=serializers.CategorySerializer)
    def list(self, request):
        serializer = serializers.CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandView(viewsets.ViewSet):
    """
    A simple ViewSet for Viewing all brands
    """

    queryset = models.Brand.objects.all()

    @extend_schema(responses=serializers.BrandSerializer)
    def list(self, request):
        serializer = serializers.BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
