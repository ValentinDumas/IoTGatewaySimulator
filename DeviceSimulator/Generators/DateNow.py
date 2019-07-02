from datetime import date
from datetime import time
from datetime import datetime

def format_date(datetime_now):
    return datetime_now.strftime("%Y-%m-%dT%H:%M:%SZ[CET]")
