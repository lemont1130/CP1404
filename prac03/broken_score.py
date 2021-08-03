"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
import random
def main():
    score_check(random_socre())
    random_socre()
    print(random_socre())
    print(score_check(random_socre()))
def score_check(score):
    if score < 0 or score > 100:
        return"Invalid score"
    elif score >= 50 and score < 90:
        return"Passable"
    elif score >= 90 and score <= 100:
        return"Excellent"
    else:
        return"Bad"
def random_socre():
    return random.randint(0,100)
main()
