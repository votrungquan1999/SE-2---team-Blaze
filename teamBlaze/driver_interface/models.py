from django.db import models
from django.contrib.auth.models import User
from accounts.models import *

# Create your models here.
STATE_CHOICE = (("Alabama", "AL"),
                ("Alaska", 'AK'),
                ('Arizona', "AZ"),
                ('Arkansas', 'AR'),
                ('California', 'CA'),
                ('Colorado', 'CO'),
                ('Connecticut', 'CT'),
                ('Delaware', 'DE'),
                ('Florida', 'FL'),
                ('Georgia', 'GA'),
                ('Hawaii', 'HI'),
                ('Idaho', 'ID'),
                ('Illinois', 'IL'),
                ('Indiana', 'IN'),
                ('Iowa', 'IA'),
                ('Kansas', 'KS'),
                ('Kentucky', 'KY'),
                ('Louisiana', 'LA'),
                ('Maine', 'ME'),
                ('Maryland', 'MD'),
                ('Massachusetts', 'MA'),
                ('Michigan', 'MI'),
                ('Minnesota', 'MN'),
                ('Mississippi', 'MS'),
                ('Missouri', 'MO'),
                ('Montana', 'MT'),
                ('Nebraska', 'NE'),
                ('Nevada', 'NV'),
                ('New Hampshire', 'NH'),
                ('New Jersey', 'NJ'),
                ('New Mexico', 'NM'),
                ('New York', 'NY'),
                ('North Carolina', 'NC'),
                ('North Dakota', 'ND'),
                ('Ohio', 'OH'),
                ('Oklahoma', 'OK'),
                ('Oregon', 'OR'),
                ('Pennsylvania', 'PA'),
                ('Rhode Island', 'RI'),
                ('South Carolina', 'SC'),
                ('South Dakota', 'SD'),
                ('Tennessee', 'TN'),
                ('Texas', 'TX'),
                ('Utah', 'UT'),
                ('Vermont', 'VT'),
                ('Virginia', 'VA'),
                ('Washington', 'WA'),
                ('West Virginia', 'WV'),
                ('Wisconsin', 'WI'),
                ('Wyoming', 'WY'),
                ('American Samoa', 'AS'),
                ('District of Columbia', 'DC'),
                ('Federated States of Micronesia', 'FM'),
                ('Guam', 'GU'),
                ('Marshall Islands', 'MH'),
                ('Northern Mariana Islands', 'MP'),
                ('Palau', 'PW'),
                ('Puerto Rico', 'PR'),
                ('Virgin Islands', 'VI'),
)

class Post(models.Model):
    seats = models.IntegerField()
    destination_state = models.CharField(max_length=100, choices=STATE_CHOICE)
    city = models.CharField(max_length=100)
    price = models.FloatField()
    bags = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

class CarPoolPost(Post):
    car = Car()