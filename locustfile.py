from locust import HttpUser, task

class GetRequestUser(HttpUser):
    @task
    def get_request(self):
        self.client.get("/")
