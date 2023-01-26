import datetime

def utils_unixtimestamp_get():
# {
    presentDate = datetime.datetime.now()
    unix_timestamp = datetime.datetime.timestamp(presentDate)
    
    return str(unix_timestamp)
# }