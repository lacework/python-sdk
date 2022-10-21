"""This is an import file that runs on every startup of the Jupyter runtime."""
# flake8: noqa

import altair as alt
import pandas as pd
import numpy as np

import laceworkjupyter
from laceworkjupyter import utils

# Keeping for legacy reasons.
from laceworkjupyter.helper import LaceworkJupyterClient as LaceworkJupyterHelper

import snowflake.connector

# Import forensic tools designed for notebooks.
# TODO (kiddi): Re-enable once TS API has been fiex, see #2388 on Timesketch.
#from picatrix import notebook_init
import ds4n6_lib as ds

# Add in the accessors to pandas.
from laceworkjupyter import accessors

# Enable the Picatrix helpers.
# TODO (kiddi): Re-enable once TS is fixed, see above.
#notebook_init.init()

# Enable the LW object.
lw = laceworkjupyter.LaceworkHelper()
