from locust import HttpUser, task


class NumericalIntegrationUser(HttpUser):
    @task
    def test_service(self):
        # Test the numerical integration service
        self.client.get("/numericalintegralservice/0/3.14159")
