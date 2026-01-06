from faker import Faker

fake = Faker()

def get_random_int(min_value: int, max_value: int):
    return fake.random_int(min=min_value, max=max_value)