from locust import HttpUser, task, between

class HelloWorldUser(HttpUser):
    @task
    def login(self):
        self.client.post("login//", json={"email":"andres@example.com", "password":"abc"})