from rest_framework import viewsets, filters
from .models import StrikeReport
from .serializers import StrikeReportSerializer

class StrikeReportViewSet(viewsets.ModelViewSet):
    queryset = StrikeReport.objects.all().order_by("-index_nr")
    serializer_class = StrikeReportSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["airport", "state", "species", "damage_level"]
    ordering_fields = ["index_nr", "airport", "state", "species"]
