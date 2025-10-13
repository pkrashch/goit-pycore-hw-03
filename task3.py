import re
def normalize_phone(phone_number):
    phone_number = phone_number.strip() #remove spaces
    pattern = r"[^\d+]"
    cleared_phone = re.sub(pattern,"",phone_number) #remove all specific symbols except from +
    if cleared_phone.startswith('+38'):
        normalized_phone = cleared_phone
    elif cleared_phone.startswith('380'):
        normalized_phone = '+'+cleared_phone
    elif cleared_phone.startswith('0'):
        normalized_phone = '+38'+cleared_phone
    else:
        normalized_phone = '+380'+cleared_phone
    return normalized_phone

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
    