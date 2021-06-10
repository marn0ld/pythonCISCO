
secret_number = 777

print(
    """
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
user_number = int(input('Im choosing number...'))
while secret_number != user_number:
    if secret_number == user_number:
        print("Well done, muggle! You are free now")

    else:
        print("Ha ha! Youre stuck in my loop")

    user_number = int(input('Im choosing number again...'))
