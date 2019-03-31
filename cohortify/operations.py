"""Operations to cohort data; also map, filter, and transform cohorted data"""

import pyspark.sql.functions as psf
from pyspark.ml import Pipeline
from pyspark.sql import DataFrame, SparkSession


def accrue_data(
    spark_session: SparkSession,
    df: DataFrame,
    id: str,
    timestamp: str,
    today: str,
    cohort_size: str,
    vals: str,
    agg: str,
) -> DataFrame:
    """Acrrue data and aggregate vals by cohort.

    Args:
        spark_session (SparkSession): spark session
        df (DataFrame): dataframe to cohort on
        id (str): name of id field
        timestamp (str): name of timestamp field
        cohort_size (str): size of cohort relative to time (e.g. days, weeks, months, etc...)
        vals (str): name of column to aggregate in cohorts
        agg (str): aggregation method to apply (e.g. count, sum, nunique, etc...)

    Returns:
        cohort_df (DataFrame): cohorted dataframe
    """
    # 0. calculate lag (e.g. time between today and timestamp)
    # today - df.select("timestamp")

    # 1. calculate cohort_id
    # f(timestamp, step_size) => cohort_id

    # 2. pivot by cohort_id
    # df.select(agg_column, cohort_id).groupby(cohort_id).apply(agg)

    # 3. format cohort_df
    # df....
    return df
