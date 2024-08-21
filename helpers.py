from datetime import datetime

def stptime(timestamp):
    if timestamp is None:
        return None
    if isinstance(timestamp, str):
        return datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    else:
        return timestamp