from django.contrib.admin.models import LogEntry

logs = LogEntry.objects.all()

for i in range(2000,len(logs)):
	logs[i].delete()