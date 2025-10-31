from rest_framework import serializers
from .models import StrikeReport

class StrikeReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrikeReport
        fields = "__all__"
