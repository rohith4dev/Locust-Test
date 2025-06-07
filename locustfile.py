from locust import HttpUser, task, between
class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def index(self):
        self.client.get("/posts")

    @task
    def create_post(self):
        self.client.post("/posts", json=
                         { "title": "Rohith Test",
                           "body": "Test Body",
                           "userId" : 1})