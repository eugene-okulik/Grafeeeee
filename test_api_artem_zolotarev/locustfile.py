import random
from locust import task, HttpUser


class ObjectUser(HttpUser):

    @task(1)
    def get_all_object(self):
        self.client.get('object')

    @task(3)
    def get_one_object(self):
        self.client.get(f'object/{random.choice([1146, 1147, 1, 1149, 1150])}')
