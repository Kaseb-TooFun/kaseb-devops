# pip install locust
# locust -f locustfile.py
from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    def on_start(self):
        self.client.post("/api/v1/authenticate/login", 
        json={
            "username": "locust",
            "password": "locust"
        }
        , headers={"accept": "*/*", "Content-Type": "application/json"})

    @ task
    def index(self):
        self.client.get("/api/v1/websites/configs?websiteUrl=test.com")

    # @task
    # def about(self):
    #     self.client.get("/about/")
