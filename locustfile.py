from locust import HttpUser, task


# Task 2 & 3

# class NumericalIntegrationUser(HttpUser):
#    @task
#    def test_service(self):
#        # Test the numerical integration service
#        self.client.get("/numericalintegralservice/0/3.14159")


# Task 4


class NumericalIntegrationUser(HttpUser):
    @task
    def test_service(self):
        # Update the endpoint to match your Azure Function URL
        self.client.get("/api/numericalintegralservice?lower=0&upper=3.14159")
