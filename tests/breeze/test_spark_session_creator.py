from src.breeze.spark_session_creator import *
import pytest


@pytest.mark.skip(reason="tested and working")
def test_spark_session():
    creator = SparkSessionCreator(app_name="test_app")
    spark = creator.create_spark_session()
    assert spark
