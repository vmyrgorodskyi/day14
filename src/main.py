#Display art
from art import logo, vs
#import info data
from game_data import data
#import random module
import random

print(logo)
#condition
game_continue = True
#counter for correct answers
counter = 0

#to keep the B asnwer as an A answer
next_choice = random.choice(data)

while game_continue:

    previous_choice = next_choice
    next_choice = random.choice(data)
    previous_name = previous_choice.get("name")
    A = previous_choice.get("follower_count")
    previous_description = previous_choice.get("description")
    previous_country = previous_choice.get("country")
    print(f"Compare A: {previous_name}, a {previous_description}, from {previous_country}")
    print(vs)

    next_name = next_choice.get("name")
    B = next_choice.get("follower_count")
    next_description = next_choice.get("description")
    next_country = next_choice.get("country")

    print(f"Against B: {next_name}, a {next_description}, from {next_country}")
    user_choice = input("Who has more follower? Type 'A' or 'B': ")

    if user_choice == "A" and A > B:
        counter += 1
        print(f"You are right. Current score is: {counter}")

    elif user_choice == "B" and B > A:
        counter += 1
        print(f"You are right. Current score is: {counter}")

    else:
        print(f"Sorry, that's wrong. Your score is {counter}")
        break
