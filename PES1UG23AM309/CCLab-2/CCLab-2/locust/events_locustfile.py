from locust import HttpUser, task, between
import random

class EventsUser(HttpUser):
    wait_time = between(1, 3)

    # Default headers (more realistic)
    headers = {
        "User-Agent": "LocustLoadTest/1.0",
        "Accept": "application/json"
    }

    @task(3)  # higher weight = more frequent
    def view_events(self):
        user_id = random.randint(1, 1000)

        with self.client.get(
            f"/events?user={user_id}",
            headers=self.headers,
            timeout=5,
            catch_response=True
        ) as response:

            if response.status_code != 200:
                response.failure(f"Failed with status {response.status_code}")
            elif not response.text:
                response.failure("Empty response")
            else:
                response.success()
