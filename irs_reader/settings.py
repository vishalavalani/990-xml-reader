import sys
import os
from .dir_utils import mkdir_p

IRS_READER_ROOT = os.path.abspath(os.path.dirname(__file__))

# This is the URL to amazon's bucket, could use another synced to it
IRS_XML_HTTP_BASE = "https://s3.amazonaws.com/irs-form-990"

# It can be hard to locate this.
IRSX_SETTINGS_LOCATION = (os.path.join(IRS_READER_ROOT, "settings.py"))

# Defaults to the same directory as this settings file, but you can override
# with the `IRSX_CACHE_DIRECTORY` environment variable
IRSX_CACHE_DIRECTORY = os.environ.get("IRSX_CACHE_DIRECTORY", IRS_READER_ROOT)

# The directory we put files in while we're processing them
WORKING_DIRECTORY = os.environ.get(
    "IRSX_WORKING_DIRECTORY", os.path.join(IRSX_CACHE_DIRECTORY, "XML"))
# Helpful to keep these around for lookup purposes
INDEX_DIRECTORY = os.environ.get(
    "IRSX_INDEX_DIRECTORY", os.path.join(IRSX_CACHE_DIRECTORY, "CSV"))

IRS_INDEX_BASE = "https://apps.irs.gov/pub/epostcard/990/xml/%s/index_%s.csv"

KNOWN_SCHEDULES = [
                "IRS990", "IRS990EZ", "IRS990PF", "IRS990ScheduleA",
                "IRS990ScheduleB", "IRS990ScheduleC", "IRS990ScheduleD",
                "IRS990ScheduleE", "IRS990ScheduleF", "IRS990ScheduleG",
                "IRS990ScheduleH", "IRS990ScheduleI", "IRS990ScheduleJ",
                "IRS990ScheduleK", "IRS990ScheduleL", "IRS990ScheduleM",
                "IRS990ScheduleN", "IRS990ScheduleO", "IRS990ScheduleR",
                "ReturnHeader990x"
]

# these could get pushed to metadata directory? 


ALLOWED_VERSIONSTRINGS = [
    '2013v3.0', '2013v3.1', '2013v4.0', 
    '2014v5.0', '2014v6.0',
    '2015v2.0', '2015v2.1', '2015v3.0', 
    '2016v3.0', '2016v3.1',
    '2017v2.0', '2017v2.1', '2017v2.2', '2017v2.3', 
    '2018v3.0', '2018v3.1', '2018v3.2', '2018v3.3',
    '2019v5.0', '2019v5.1', '2019v5.2', 
    '2020v1.0', '2020v1.1','2020v1.2','2020v1.3', '2020v2.0', '2020v3.0', '2020v4.0','2020v4.1', '2020v4.2',
    '2021v4.0','2021v4.1','2021v4.2','2021v4.3',
    '2022v4.0','2022v4.1','2022v5.0',
    '2022v6.0','2022v7.0','2022v7.1',
    # these are guesses for future 2023 schemas; they might not actually exist
    '2023v1.0',
    '2023v2.0',
    '2023v3.0','2023v3.1','2023v3.2','2023v3.3',
    '2023v4.0','2023v4.1','2023v4.2','2023v4.3',
    '2023v5.0','2023v5.1','2023v5.2','2023v5.3',
    '2023v6.0','2023v6.1','2023v6.2','2023v6.3',
    '2023v7.0','2023v7.1','2023v7.2','2023v7.3',
]

# 2020 is experimental
# see https://www.irs.gov/charities-non-profits/ty2020-xml-schemas-and-business-rules-for-exempt-organizations-modernized-e-file

# We can capture the group structure for these so it doesn't break
# but these versions ARE NOT supported and aren't mapped to IRSx variables
CSV_ALLOWED_VERSIONSTRINGS = ALLOWED_VERSIONSTRINGS + [
    '2010v3.2', '2010v3.4', '2010v3.6', '2010v3.7', '2011v1.2', '2011v1.3',
    '2011v1.4', '2011v1.5', '2012v2.0', '2012v2.1', '2012v2.2', '2012v2.3', 
    '2012v3.0'
]

METADATA_DIRECTORY = (os.path.join(IRS_READER_ROOT, "metadata"))

KEYERROR_LOG = os.path.join(IRS_READER_ROOT, "keyerrors.log")
LOG_KEY = 'xml'

mkdir_p([WORKING_DIRECTORY, INDEX_DIRECTORY])

try:
    from .local_settings import *
except ImportError:
    pass
