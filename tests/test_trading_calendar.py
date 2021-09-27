from pandas_market_calendars.exchange_calendars_mirror import TradingCalendar
import pandas_market_calendars as mcal

import exchange_calendars as ecal

from pytz import timezone
from datetime import time

mcal_iepa = mcal.get_calendar("IEPA")
ecal_iepa = ecal.get_calendar("IEPA")


def test_mirror():

    assert not hasattr(mcal_iepa, "aliases")

    assert not isinstance(ecal_iepa, mcal_iepa.__class__)

    assert isinstance(ecal_iepa, mcal_iepa._tc.__class__)

def test_basic_information():

    assert mcal_iepa.tz == timezone("America/New_York")
    assert mcal_iepa.open_offset == -1
    assert mcal_iepa.open_time == time(20)
    assert mcal_iepa.close_time == time(18)





