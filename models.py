from django.db import models

from dwarf.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    utc_offset = models.SmallIntegerField(null=True, blank=True)
    
    # every Dwarf Model must define this Meta class
    class Meta:
        app_label = 'dwarf'
