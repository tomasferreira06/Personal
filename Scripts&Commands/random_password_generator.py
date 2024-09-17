import random
import sys

# Define the basic words to use for password creation, these will be simple and similar to the rockyou file.
basic_words = [
    'password', '123456', 'guest', 'labuser', 'hello', 'name', 'nome', 'Password', 'Guest', 'Labuser'
]

def simplify_password(password):
    password = list(password)

    # Randomly uppercase 1 character
    num_upper = random.randint(1, 2)  # Randomly decide to uppercase 1 or 2 characters
    upper_positions = random.sample(range(len(password)), num_upper)
    for pos in upper_positions:
        password[pos] = password[pos].upper()

    # Randomly insert 1 special character
    special_characters = "!?%*"
    num_special = 1
    special_positions = random.sample(range(len(password)), num_special)
    for pos in special_positions:
        password.insert(pos, random.choice(special_characters))

    return ''.join(password)

def generate_uppercase_password(password):
    # Simply uppercase the entire password
    return password.upper()

# Check if a file name argument was provided
if len(sys.argv) != 2:
    print("Usage: python password_generator.py <output_file>")
    sys.exit(1)

output_file = sys.argv[1]

# Generate the list of simpler passwords
simpler_password_list = set()
while len(simpler_password_list) < 1000:
    # Randomly pick a base word and modify it
    base_password = random.choice(basic_words) + str(random.randint(0, 99))
    
    # Simplify the password
    modified_password = simplify_password(base_password)
    simpler_password_list.add(modified_password)
    
    # Also add the fully uppercase version of the password
    uppercase_password = generate_uppercase_password(base_password)
    simpler_password_list.add(uppercase_password)

# Save the passwords to the specified file
with open(output_file, 'w') as f:
    for password in simpler_password_list:
        f.write(password + '\n')

print(f"Generated {len(simpler_password_list)} passwords and saved to {output_file}")