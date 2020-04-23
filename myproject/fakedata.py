import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myproject.settings')
import django
django.setup()

import random
from myapp.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def addTopic():
    t = Topic.objects.get_or_create(topname=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = addTopic()
        fakeurl = fakegen.url()
        fakedate = fakegen.date()
        fakename = fakegen.company()
        webpge = Webpage.objects.get_or_create(topic=top,url=fakeurl,name=fakename)[0]
        accreq = AccessRecord.objects.get_or_create(name=webpge,date=fakedate)[0]

if __name__ == '__main__':
    print('Populating Script!')
    populate(20)
    print('Populating complete!')