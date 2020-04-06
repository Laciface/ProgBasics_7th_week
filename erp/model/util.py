import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
                
                random_str = ""
                random_str_lower = (random.choice(string.ascii_lowercase) for _ in range(number_of_small_letters))
                random_str_upper = (random.choice(string.ascii_uppercase) for _ in range(number_of_capital_letters)) 
                random_str_digits =  (random.choice(string.digits) for _ in range(number_of_digits)) 
                random_str_special = random.choice(allowed_special_chars) 
                random_str = ''.join(random_str_lower).join(random_str_upper).join(random_str_digits)
                random_str = random_str[:3] + random_str_special + random_str[3:]
                random_str_special = random.choice(allowed_special_chars)
                random_str = random_str[:5] + random_str_special + random_str[5:]

                return random_str           