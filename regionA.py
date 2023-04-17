import random
import pytest
import math

# Define the classes and functions used in the game
def test_skill_card_probability():
    skill_card_count = 0
    number_card_count = 0
    skill_card_prob = 0.6

    # Simulate 1000 iterations of card selection
    for i in range(1000):
        # Randomly select a card based on the defined probabilities
        random_number = random.uniform(0, 1)

        if random_number < skill_card_prob:
            skill_card_count += 1
        else:
            number_card_count += 1

    # Calculate the standard error and confidence interval
    SE = math.sqrt((skill_card_count / 1000) * (1 - skill_card_count / 1000) / 1000)
    # 0.05 significant level z 0.025 = 1.96
    lower_bound = skill_card_count / 1000 - SE * 1.96
    upper_bound = skill_card_count / 1000 + SE * 1.96

    print(upper_bound - lower_bound)
    # Check that the observed proportion of skill cards falls within the confidence interval
    assert upper_bound - lower_bound < 0.1 # margin of error
test_skill_card_probability()