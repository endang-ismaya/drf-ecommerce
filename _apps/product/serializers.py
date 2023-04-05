from rest_framework import serializers
from _apps.product import models


class DynamicFieldsCategorySerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop("fields", None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class CategorySerializer(DynamicFieldsCategorySerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class BrandSerializer(DynamicFieldsCategorySerializer):
    class Meta:
        model = models.Brand
        fields = "__all__"


class ProductSerializer(DynamicFieldsCategorySerializer):
    brand = BrandSerializer(fields=("name",))
    category = CategorySerializer(fields=("name",))

    class Meta:
        model = models.Product
        fields = "__all__"
