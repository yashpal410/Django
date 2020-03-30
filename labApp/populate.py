from faker import Faker
from .models import User, ActivityPeriod

fake = Faker()

count = 10

def populateData():
    for _ in range(count):
        real_name = fake.name()
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        str = ''
        def populateId():
            for i in range(8):
                char = random.choice(alpha)
                str = str + char
            str = 'W' + str
            id = str
            return id
        country = fake.country()
        city = fake.city()
        tz = country + '/' + city
        while(True):
            id = populateId()
            if User.objects.filter(id=id).exists():
                continue
            else:
                user = User(id = id, real_name = real_name, tz = tz)
                user.save()

        for i in range(3):
            start_time = fake.date_time_this_century()
            end_time = fake.date_time_this_century()
            while(start_time >= end_time):
                end_time = fake.date_time_this_century()
            activityperiod = ActivityPeriod(id = id, start_time = start_time, end_time = end_time)
            activityperiod.save()
