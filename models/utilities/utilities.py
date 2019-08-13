from datetime import datetime
import json


class DateTimeEncoder(json.JSONEncoder):
    """Convert datetime object to json'.


    :param size (str): Datetime python object.

    :return: Return json representation of datetime object.
    """

    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


def boolean_to_binary(is_grid_valid):
    """
    Converts boolean to binary

    :param is_grid_valid(boolean):  Boolean value
    :return: Binary representation od boolean value
    """
    return bin(int(is_grid_valid))
