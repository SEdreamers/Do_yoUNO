import random
import pytest

def test_card_distribution():
    num_trials = 1000
    expected_skill_card_proportion = 0.6
    margin_of_error = 0.05
    actual_skill_card_count = 0

    for _ in range(num_trials):
        if random.random() < expected_skill_card_proportion:
            actual_skill_card_count += 1

    actual_skill_card_proportion = actual_skill_card_count / num_trials
    print(abs(actual_skill_card_proportion - expected_skill_card_proportion))
    assert abs(actual_skill_card_proportion - expected_skill_card_proportion) <= margin_of_error
test_card_distribution()