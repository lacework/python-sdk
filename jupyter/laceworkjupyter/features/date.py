"""
A simple class to wrap the date parsing function in the utilities lib.
"""
from laceworkjupyter import helper
from laceworkjupyter import manager
from laceworkjupyter import utils


def parse_date_offset(offset_string):
    """
    Parse date offset string and return a start and end time.

    :param str offset_string: The offset string describing the time period.
    :raises ValueError: If not able to convert the string to dates.
    :return: A tuple with start and end time as ISO 8601 formatted strings.
    """
    return utils.parse_date_offset(offset_string)


manager.LaceworkManager.add_feature(parse_date_offset, 'parse_date_offset')
