"""All of this is just "pseudo-code". It will not actually work just yet."""

from dwarf.core.api import CoreAPI

import datetime.time


core = CoreAPI()


def get_utc_offset(local_time, dst=False):
    """Gets UTC offset by local time.
    
    Parameters
    ----------
    local_time : str
        A local time in HH:MM format (e.g. '09:52')
        or as a dict with 'hour' and 'minute' keys.
    dst : bool
        Whether the current `local_time` is affected by Daylight Saving Time.
    """
    
    if isinstance(local_time, dict):
        local_time = [local_time['hour'], local_time['minute']]
    else if isinstance(local_time, str):
        local_time = local_time.split(':')
    utc_time = datetime.time.utc_now()
    hour_difference = local_time[0] - utc_time['hour']
    minute_difference = local_time[1] - utc_time['minute'],
    if dst:
        hour_difference -= 1
    time_difference = {
        'hour': hour_difference,
        'minute': minute_difference,
    }
    
    return time_difference
