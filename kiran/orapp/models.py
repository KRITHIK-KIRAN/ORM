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