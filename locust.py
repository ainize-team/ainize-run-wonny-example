import contextlib
import io
import os
import random
import time
import uuid
import urllib

import requests
from locust import HttpLocust, TaskSet, task, between

TARGET_IMAGE_FILES = [
    # XXX: from https://randomuser.me/photos
    *[f"https://randomuser.me/api/portraits/men/{idx}.jpg" for idx in range(100)],
    *[f"https://randomuser.me/api/portraits/women/{idx}.jpg" for idx in range(100)],
    # XXX: from https://tinyfac.es/
]
FETCHED_IMAGE_FILES = {}




class UserTaskSet(TaskSet):
    @task
    def send(self):
        req_id = str(uuid.uuid4())  # XXX: Just for tracing
        picked_image = random.choice(TARGET_IMAGE_FILES)
        taskname = 'eval/image'
        started = time.time()
        response = self.client.get(f"{taskname}?url={picked_image}")
        ended = time.time()

        duration = ended - started
        print(
            (
                "out",
                req_id,
                taskname,
                duration,
                response.status_code,
                len(response.content),
            )
        )


TARGET_RPS = 10


class User(HttpLocust):
    task_set = UserTaskSet

    def wait_time(self):
        target_wait = between(0, 1 / TARGET_RPS)(self)
        print(("wait", target_wait))
        return target_wait

if __name__ == "__main__":
    ts = UserTaskSet()
    ts.client = requests
    ts.send()
