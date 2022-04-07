from faker import Faker

faker = Faker('zh-TW')


def get_all_users():
    users = [faker.name() for _ in range(5)]
    return users