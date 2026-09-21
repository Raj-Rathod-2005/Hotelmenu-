# 1 - Import the random module
import random

# 2 - Create subjects
subjects = [ 
    "Shahrukh Khan",
    "Virat Kohli",
    "Rathod Raj",
    "A Mumbai Cat",
    "A Group of Monkeys"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai local",
    "a plate of samosa",
    "inside Parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

# 3 - Start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"

    print("\n" + headline)

    user_input = input(
        "\nDo you want another headline? (yes/no): "
    ).strip().lower()

    if user_input == "no":
        break

# Print goodbye message
print("\nThanks for using Fake News Headline Generator. Have a fun day!")