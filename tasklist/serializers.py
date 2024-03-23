from rest_framework import serializers
from .models import Tasklist

class TasklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasklist
        fields = "__all__"