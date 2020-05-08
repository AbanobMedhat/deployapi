from rest_framework import serializers
from .models import Uploadfile

# serializer part
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uploadfile
        fields = "__all__"