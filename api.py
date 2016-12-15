"""Untested, use at own risk"""

from dwarf.core.api import CoreAPI
from .models import UserInfo

import time


core = CoreAPI()


class UtilitiesAPI:
    
    def calculate_utc_offset(local_time):
        """Calculates UTC offset using local time.
        Let's pretend this works as intended...
        
        Parameters
        ----------
        local_time
            A local time in HH:MM format (e.g. '09:52')
            or as a dict with 'hour' and 'minute' keys.
        """
        
        if isinstance(local_time, dict):
            local_time = [local_time['hour'], local_time['minute']]
        else if isinstance(local_time, str):
            local_time = local_time.split(':')
        utc_time = time.gmtime()
        
        hour_difference = local_time[0] - utc_time.tm_hour
        minute_difference = local_time[1] - utc_time.tm_minute
        
        time_difference = {
            'hour': hour_difference,
            'minute': minute_difference,
        }
        
       return time_difference
    
    def get_utc_offset(user):
        """Retrieves a user's UTC offset from the database.
        Returns `None` if no UTC offset was saved for the user.
        
        Parameters
        ----------
        user
            The user to retrieve the UTC offset of.
        """
        
        user = core.get_user(user)
        return user.userinfo.utc_offset
    
    def save_utc_offset(user, utc_offset):
        """Links the UTC offset to a `User` and stores it in the database.
        
        Parameters
        ----------
        user
            The user to assign the `utc_offset` to. Can be a `User` object or a `User` id.
        utc_offset : int
            The UTC offset.
        """
        
        user = core.get_user(user)
        userinfo = UserInfo(user=user.id, utc_offset=utc_offset)
        userinfo.save()
