from datetime import datetime
from django.http import JsonResponse
from pytz import UTC

from .models import Readout

# Create your views here.
def index(request):
    current_time = datetime.utcnow()
    timestamp = datetime(2018, 1, 1, current_time.hour, current_time.minute, current_time.second, 0, UTC)
    return JsonResponse(list(Readout.objects.filter(time=timestamp).all().values()), safe=False)

def readouts(request):
    return JsonResponse(list(Readout.objects.order_by('time')[:50].values()), safe=False)

def readouts_time(request, hour, minute, second):
    timestamp = datetime(2018, 1, 1, int(hour), int(minute), int(second), 0, UTC)
    return JsonResponse(list(Readout.objects.filter(time=timestamp).all().values()), safe=False)