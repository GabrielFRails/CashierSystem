#
# Copyright (c) 2023 Gabriel Freitas <gabriel.estudy.reis@gmail.com>
#

import datetime
import uuid

def utils_unixtimestamp_get():
# {
    presentDate = datetime.datetime.now()
    unix_timestamp = datetime.datetime.timestamp(presentDate)
    
    return str(unix_timestamp)
# }

def utils_generate_id():
# {
    return str(uuid.uuid4()).split("-")[0].upper()
# }