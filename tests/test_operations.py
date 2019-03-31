import pytest
from hypothesis import given

from accrual.operations import accrue_data
from tests.strategies import some_rows


@pytest.mark.usefixture("spark_session")
class TestAccrueData():
    @given(some_rows)
    def test_cohort_data(self, spark_session, some_rows):
        df = spark_session.sparkContext.parallelize(some_rows).toDF()
        df.show()
        accruals = accrue_data(
            df,
            id="id",
            timestamp="timestamp",
            cohort_size="days",
            vals="vals",
            agg="agg",
        )
        assert accruals.count() > 0
