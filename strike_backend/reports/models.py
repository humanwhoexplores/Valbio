from django.db import models

class StrikeReport(models.Model):
    class Meta:
        db_table = "strike_reports"
        managed = False

    index_nr = models.IntegerField(primary_key=True, db_column="index_nr")
    incident_date = models.CharField(max_length=50, null=True, blank=True)
    airport = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    species = models.CharField(max_length=100, null=True, blank=True)
    damage_level = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.index_nr} - {self.airport}"
