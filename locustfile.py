# pip3 install locust
# locust

from locust import HttpUser, task

class GetRequestUser(HttpUser):
    @task
    def get_request(self):
        self.client.get("/")
