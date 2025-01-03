from faker import Faker

from ray import serve


@serve.deployment
def create_fake_email():
    return Faker().email()


app = create_fake_email.bind()