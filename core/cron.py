from django_cron import CronJobBase, Schedule
from core.incident.models import Incident
from core.dht.models import DHT


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 10  # Run every 10 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = "core.my_cron_job"  # Unique code for your job

    def do(self):
        # Your logic here
        print("Running scheduled task")
        # close automaticlly the opened incident if the temp and humidity are back to normal
        incident = Incident.objects.filter(resolved=False).first()
        print(f"incident temperature : {str(incident.temperature)}")
        print(f"incident humidity : {str(incident.humidity)}")
        if (
            incident.temperature > 20
            and incident.temperature < 32
            and incident.humidity > 30
            and incident.humidity < 70
        ):
            incident.resolved = True
            incident.save()
            print("Incident closed by cron job.")
