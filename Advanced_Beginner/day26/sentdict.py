"""
create a dictionary called result that takes each word in a given
sentence and calculates the number of letters in each word
"""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}

print(result)