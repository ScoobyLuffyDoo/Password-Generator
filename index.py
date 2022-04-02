
import random
from tokenize import Special
import numpy as np

character_set ='abcdefghijklmnopqrstuvwxyz'
upper_character_set = character_set.upper()
numbers_set = "0123456789"
special_character='!@#$%^&*()_+=|?<>/'
all_characters = character_set + upper_character_set + numbers_set + special_character
tempset= random.sample(all_characters,10)
password= "".join(tempset)
print(password)