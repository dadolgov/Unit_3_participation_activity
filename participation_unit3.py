"""
Dragon name generator
Author: Dmitrii Dolgov
Purpose: generates random dragon names from 2 lists
Date: 1/30/2026
"""
import random
#initializing name lists
dragon_names=["yse", "jinim","fraghinth","zathyd","ayndran","edyr",
             "grimmyn","paidacro","neikinoig","agocrem"]
dragon_titles=["the swift","longtail","braveheart","lord of the yellow",
              "the young one","the protective","the victorious","the deathlord"
              "the devourer", "the despoiler"]
#safeguard in case of different list lengths
if len(dragon_names)<len(dragon_titles):
    max_index=len(dragon_names)-1
else:
    max_index=len(dragon_titles)-1
#output_header
print("Here are the names of your dragons:")
#iterating and making names
for index in range(max_index+1):
    full_name=f"{dragon_names[random.randint(0,max_index)].title()} {dragon_titles[random.randint(0,max_index)].title()}."
    print(full_name)
