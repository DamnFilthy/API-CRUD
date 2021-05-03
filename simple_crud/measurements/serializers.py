from measurements.models import Project, Measurement
from rest_framework import serializers
import base64


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'latitude', 'longitude', 'created_at', 'updated_at']


class MeasurementSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(
        max_length=None,
        use_url=True,
        allow_empty_file=True
    )

    class Meta:
        model = Measurement
        fields = ['value', 'project', 'img', 'created_at', 'updated_at']
