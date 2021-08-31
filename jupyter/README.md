# Lacework Jupyter Helper

**laceworkjupyter** is a community developed Python library for interacting with the Lacework APIs in a
Jupyter notebook environment.

The purpose of this library is to simplify using the Lacework SDK in a Jupyter notebook environment. This allows
users to more easily work with the output of all API calls to the SDK in a notebook environment.

To get a data frame with the events within a time range one can simply write this code:

```
from laceworkjupyter import LaceworkJupyterHelper

with LaceworkJupyterHelper() as helper:
    df = helper.events.get_for_date_range('2021-08-25T00:00:00', '2021-08-27T23:59:23')
```

And to get events from the last 5 days:

```
from laceworkjupyter import LaceworkJupyterHelper
from laceworkjupyter import utils

with LaceworkJupyterHelper() as helper:
    start_time, end_time = utils.parse_date_offset('LAST 5 DAYS')

    df = helper.events.get_for_date_range(start_time=start_time, end_time=end_time)
```


## Requirements

- Python 3.6 or higher
- Lacework API Credentials
  - Account Name
  - API Key
  - API Secret
- Lacework Python SDK
- Pandas version 1.0.1 or higher

## How-To

More to come here.
