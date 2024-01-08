========================================
Lacework Python SDK Timestamp Generation
========================================

For all "search" methods Lacework requires ``start_time`` and ``end_time`` arguments which
are used to specify the search window. Additionally some "get" methods also require them.
These must be specified as strings in the following format:

    ``"%Y-%m-%dT%H:%M:%S%z"``

For example:

    ``"2024-01-08T22:34:10+0000"``

You are free to generate these strings however you like but you may find it useful to
use the following function (or something similar.)

..  code-block::
    :caption: Timestamp Generation Function

    from datetime import datetime, timedelta, timezone

    def generate_time_string(delta_days=0, delta_hours=0, delta_minutes=0, delta_seconds=0) -> str:
        return (datetime.now(timezone.utc) - timedelta(days=delta_days, hours=delta_hours, minutes=delta_minutes, seconds=delta_seconds)).strftime("%Y-%m-%dT%H:%M:%SZ")


This will allow you to generate time stamps relative to "now" easily. For Example:

..  code-block::
    :caption: Generating Timestamp

    right_now = generate_time_string()

    twelve_hours_ago = generate_time_string(delta_hours=12)

    one_day_ago = generate_time_string(delta_days=1)

    thirty_six_and_a_half_hours_ago = generate_time_string(delta_days=1,
                                                           delta_hours=12,
                                                           delta_minutes=30)
