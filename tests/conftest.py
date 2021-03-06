import logging
import os
import shutil

import findspark
import pytest
from pyspark.sql import SparkSession

findspark.init()


def quiet_py4j():
    """ turn down spark logging for the test context """
    logger = logging.getLogger("py4j")
    logger.setLevel(logging.WARN)


@pytest.fixture(scope="session")
def spark_session(request):
    """fixture for creating a spark context
    Args:
        request: pytest.FixtureRequest object
    """
    try:
        os.remove("./derby.log")
        shutil.rmtree("./metastore_db")
    except OSError:
        pass

    session = (
        SparkSession.builder.appName("pytest-pyspark-local-testing")
        .master("local[2]")
        .enableHiveSupport()
        .getOrCreate()
    )
    request.addfinalizer(lambda: session.stop())

    quiet_py4j()
    return session
