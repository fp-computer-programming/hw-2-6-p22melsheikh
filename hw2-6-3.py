# Author MEE 9/26/21

freethrows_scored = input("How many free throws were made during the game? ")

twopoints = input("Two pointers? ")

threepoints = input("Three pointers? ")

overallpoints = (int(freethrows_scored)) + (int(twopoints) * 2) + (int(threepoints) * 3)

print("Overall Points scored this game is " + str(overallpoints))