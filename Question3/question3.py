import random
import string
def get_password(ranged):
    # get random password pf length 8 with letters, digits, and symbols
    # string.ascii_letters: To include letters from a-z and A-Z
    # string.digits: To include digits from 1 to 10
    # string.punctuation: to get special symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    # range argument is for the length of the password
    password = ''.join(random.choice(characters) for i in range(ranged))
    return password