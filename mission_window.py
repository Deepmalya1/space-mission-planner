from datetime import datetime,timedelta
import numpy as np

def optimal_launch_window(orbital_period_1,orbital_period_2,current_date):
    synodic_period = 1/abs(1/orbital_period_1 - 1/orbital_period_2)
    optimal_launch_date = current_date+timedelta(days=synodic_period*365)
    return optimal_launch_date
current_date = datetime.now()
print(optimal_launch_window(1, 1.88, current_date))