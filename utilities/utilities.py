from datetime import datetime
import json


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


def boolen_to_binary(is_grid_valid):
    if is_grid_valid:
        return '0b0'
    else:
        return '0b1'
