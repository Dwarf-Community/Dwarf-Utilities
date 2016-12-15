from django.db import models

from dwarf.models import User

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    utc_offset = models.SmallIntegerField(null=True, blank=True)
