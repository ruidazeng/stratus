# pip3 install locust
# locust
# http://localhost:8089/

from locust import HttpUser, task

class GetRequestUser(HttpUser):
    @task
    def get_request(self):
        self.client.get("/")
