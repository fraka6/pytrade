__docformat__ = 'restructuredtext'

__version__ = '0.0.14.0'

from datetime import datetime

import numpy as np
import pandas as pd
pd.options.display.mpl_style = 'default'  # make nicer plots


from .lib.functions import *
from .lib.csvDatabase import HistDataCsv
from .lib.backtest import Backtest
