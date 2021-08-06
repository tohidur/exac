from __future__ import absolute_import
from __future__ import print_function

from sqlalchemy import create_engine
from locust import Locust, between, TaskSet, task, events
import time


def create_conn(conn_string):
    return create_engine("mysql+pymysql://" + conn_string).connect()


def execute_query(conn_string, query):
    _conn = create_conn(conn_string)
    rs = _conn.exeucte(query)
    return rs


class MySqlClient:
    def __getattr__(self, name):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                res = execute_query(*args, **kwargs)
                events.request_success.fire(
                    request_type="mysql",
                    name=name,
                    response_time=int((time.time() - start_time) * 1000),
                    response_length=res.rowCount)
            except Exception as e:
                events.request_failure.fire(
                    request_type="mysql",
                    name=name,
                    response_time=int((time.time() - start_time) * 1000),
                    exception=e)
        return wrapper


class CustomTaskSet(TaskSet):
    conn_string = "employee-metrics:employee-metrics@emp1-emtrics-db-1/emp"

    @task(1)
    def execute_query(self):
        self.client.execute_query(
            self.conn_string,
            "select * from employees limit 1")


class MySqlLocust(Locust):
    min_wait = 0
    max_wait = 0
    task_set = CustomTaskSet
    wait_time = between(min_wait, max_wait)

    def __init__(self):
        super()
        self.client = MySqlClient()

