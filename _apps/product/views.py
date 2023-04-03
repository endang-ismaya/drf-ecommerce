from rest_framework import viewsets
from _apps.product import models, serializers
from rest_framework.response import Response


class CategoryView(viewsets.ViewSet):
    """
    A simple ViewSet for Viewing categories
    """

    queryset = models.Category.objects.all()

    def list(self, request):
        serializer = serializers.CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
