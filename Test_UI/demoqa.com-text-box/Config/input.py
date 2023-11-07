from faker import Faker
fake = Faker()


def split_in_string(strings, symbol=' '):
    """Merge multiline text into one line"""
    one_str = strings.split()
    return symbol.join(one_str)


full_name = fake.name()
email = fake.email()
cur_address = split_in_string(fake.address())
per_address = split_in_string(fake.address())
