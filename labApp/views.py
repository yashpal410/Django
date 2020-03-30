'''
    writing views to send json data as HttpResponse
    '''
import json
from django.http import HttpResponse
from .models import User, ActivityPeriod

# Create your views here.
def my_view(request):
    ''' function to send HttpResponse '''
    users = User.objects.all()
    items = []
    file = {}

    for row in users:
        activity = ActivityPeriod.objects.filter(idm=row.id)
        list1 = []
        dict1 = {}
        dict2 = {}
        for col in activity:
            dict2["start_time"] = str(col.start_time.strftime("%b %d %Y %I:%M%p"))
            dict2["end_time"] = str(col.end_time.strftime("%b %d %Y %I:%M%p"))
            list1.append(dict2)
        dict1["id"] = row.id
        dict1["real_name"] = row.real_name
        dict1["tz"] = row.tz
        dict1["activity_periods"] = list1
        items.append(dict1)

    file["ok"] = True
    file["members"] = items
    y_str = json.dumps(file, indent=4, separators=(",\n", " : "))
    z_json = json.loads(y_str)
    html = "<html><body> %s </body></html>" %z_json
    return HttpResponse(html)
