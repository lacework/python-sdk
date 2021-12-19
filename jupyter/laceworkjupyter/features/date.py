"""
A simple class to wrap the date parsing function in the utilities lib.
"""
from laceworkjupyter import manager
from laceworkjupyter import utils


@manager.register_feature
def parse_date_offset(offset_string, ctx=None):
    """
    Parse date offset string and return a start and end time.

    :param str offset_string: The offset string describing the time period.
    :param obj ctx: The Lacework context object.
    :raises ValueError: If not able to convert the string to dates.
    :return: A tuple with start and end time as ISO 8601 formatted strings.
    """
    start_time, end_time = utils.parse_date_offset(offset_string)
    ctx.add("start_time", start_time)
    ctx.add("end_time", end_time)
    return start_time, end_time
