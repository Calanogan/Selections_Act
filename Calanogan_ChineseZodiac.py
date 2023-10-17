signs = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
year = int(input(" Enter a year "))
formula = (year- 1900) % 12
zodiac = signs[formula]
print(f"The Chinese zodiac of the year {year} is {zodiac}. ")