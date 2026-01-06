from faker import Faker

fake = Faker()

def get_random_int(min_value: int, max_value: int):
    return fake.random_int(min=min_value, max=max_value)
    
# Personal info
# print(fake.name())        # John Doe
# print(fake.address())     # 123 Main St
# print(fake.email())       # john@example.com
# print(fake.phone_number())

# # Company info
# print(fake.company())
# print(fake.job())

# # Internet / misc
# print(fake.ipv4())
# print(fake.date_this_year())
# print(fake.ssn())
# Generate multiple fake users:
# python
# Copy code
