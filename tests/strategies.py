"""Search strategies for generating arbitrary pre-cohorted data"""

import datetime

from hypothesis import strategies as st

############################################################################
#                      Strategies for Generating Fields                    #
############################################################################

# ids
some_id = st.from_regex(regex="^[0-9]{9}$", fullmatch=True)
some_ids = st.lists(elements=some_id, min_size=50, max_size=50)

# timestamp
min_datetime = datetime.datetime(2016, 1, 1, 0, 0, 0)
max_datetime = datetime.datetime(2016, 12, 31, 0, 0, 0)
some_datetime = st.datetimes(min_datetime, max_datetime)
some_datetimes = st.lists(elements=some_datetime, min_size=50, max_size=50)

# today
min_today = datetime.datetime(2016, 4, 1, 0, 0, 0)
max_today = datetime.datetime(2016, 8, 31, 0, 0, 0)
some_today = st.datetimes(min_today, max_today)

# decimal values
some_val = st.decimals(
    min_value=0.00, max_value=100.0, allow_nan=False, allow_infinity=False, places=2
)
some_vals = st.lists(elements=some_val, min_size=50, max_size=50)


# account class
account_classes = ["LATAM", "SEA", "NA"]
some_account_class = st.sampled_from(account_classes)


# admission dates
@st.composite
def some_admission_date(draw):
    some_year = draw(some_ids)
    some_month = draw(some_datetimes)
    some_day = draw(some_vals)
    return some_year + some_month + some_day


# one joned claim, e.g. one record in the joined claim header / claim line
some_row = st.fixed_dictionaries({
    "id": some_id,
    "datetime": some_datetime,
    "val": some_val
})

# more than one joined claim, e.g. more one record in the joined claim header / claim line
some_rows = st.lists(elements=some_row, min_size=10, max_size=20)
