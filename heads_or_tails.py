import random

coin_value = random.randint(0, 1)

usr_guess = input('Heads or Tails?\n').lower()
print(coin_value)
if coin_value == 0 and usr_guess == 'heads':
    print("You were right! Its Heads!")
elif coin_value == 1 and usr_guess == 'tails':
    print("You were right! Its Tails!")
else:
    print('Sorry you were wrong!')