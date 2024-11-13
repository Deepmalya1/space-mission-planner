import numpy as np
from datetime import datetime , timedelta
def generate_mission_timeline(start_date,duration_days):
    events = {
        'Launch' : start_date,
        'Orbit Insertion' : start_date+timedelta(days=duration_days*0.2),
        'Flyby' : start_date+timedelta(days=duration_days*0.5),
        'Arrival':start_date+timedelta(days=duration_days)
    }
    return events
# mission_start_date = datetime.now()
# print(generate_mission_timeline(mission_start_date, 100))