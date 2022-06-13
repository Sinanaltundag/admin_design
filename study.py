# >>> from patients.models import Patient
# >>> from faker import Faker
# >>> faker = Faker()

# >>> for i in range(1,50):
# ...     patient = Patient(name=faker.name(), birthday=faker.date_between('-70y'), email=faker.ascii_email(),phone=faker.phone_number(),address=faker.address(),city=faker.city(),state=faker.country(), zipcode=faker.postcode(), slug=faker.slug())
# ...     patient.save()
# ................ double enter to run the code .................