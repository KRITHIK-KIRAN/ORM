# Ex02 Django ORM Web Application
## Date: 14.09.25

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import ferrari_DB,ferrari_DBAdmin
admin.site.register(ferrari_DB,ferrari_DBAdmin)

models.py

from django.db import models
from django.contrib import admin
class ferrari_DB(models.Model):
    Buyer_name=models.CharField(max_length=20)
    Model_no=models.IntegerField()
    Email=models.EmailField()
    Date_of_Buy=models.DateField()
    Cost=models.FloatField()

class ferrari_DBAdmin(admin.ModelAdmin):
    list_display=["Buyer_name","Model_no","Email","Date_of_Buy","Cost"]
```


## OUTPUT
![alt text](<Screenshot (1).png>)



## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
