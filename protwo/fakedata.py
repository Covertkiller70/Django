import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','protwo.settings')
import django
django.setup()

import random
from proapp.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fname = fakegen.first_name()
        lname = fakegen.last_name()
        email = fakegen.free_email()
        User.objects.get_or_create(firstname=fname, lastname=lname, email=email)[0]
        
if __name__ == "__main__":
    print('Populating...')
    populate(20)
    print('Done!')