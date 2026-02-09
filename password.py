import random
import string

# Length of password
length = 10

# Characters to use
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Generate password
password_list = random.sample(characters, length)

# Shuffle password
random.shuffle(password_list)

# Convert list to string
password = ''.join(password_list)

print("Generated Password:", password)
