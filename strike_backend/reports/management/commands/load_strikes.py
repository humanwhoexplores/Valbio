import csv
from pathlib import Path
from django.core.management.base import BaseCommand
from reports.models import StrikeReport

class Command(BaseCommand):
    help = "Load sample CSV into strike_reports table."

    def add_arguments(self, parser):
        parser.add_argument("--path", required=True, help="Path to CSV file")

    def handle(self, *args, **opts):
        path = Path(opts["path"])
        if not path.exists():
            self.stderr.write(f"File not found: {path}")
            return

        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                try:
                    StrikeReport.objects.update_or_create(
                        index_nr=int(row["INDEX_NR"]),
                        defaults={
                            "incident_date": row.get("INCIDENT_DATE"),
                            "airport": row.get("AIRPORT"),
                            "state": row.get("STATE"),
                            "species": row.get("SPECIES"),
                            "damage_level": row.get("DAMAGE_LEVEL"),
                        },
                    )
                    count += 1
                except Exception as e:
                    self.stderr.write(f"Error: {e}")
            self.stdout.write(self.style.SUCCESS(f"Loaded {count} rows"))
