#!python3
 
"""
Assignment 5:
Make a Mad Lib

Ask the user to enter a number of words, one for each of the underscored words in the following paragraph.  Once they have finished, display the following story to them with the replacements made in the Mad Lib

Today we picked apple from _PERSON_'s Orchard. I had no idea there were so many different varieties of apples. I ate _ADJECTIVE_ apples straight off the tree that tasted like _FOOD_. Then there was a _ADJECTIVE_ apple that looked like a _NOUN_.  When our bag was full, we went on a free hay ride to _PLACE_ and back. It ended at a hay pile where we got to _VERB_ _ADVERB_. I can hardly wait to get home and cook with the apples. We are going to make apple _FOOD_ and _THINGS_ pies!
"""

from typing import DefaultDict


PERSON =(input("enter a name")).strip
ADJECTIVE=(input("enter a adjective")).strip
FOOD=(input("enter a food")).strip
ADJECTIVE2=(input("enter a adjective")).strip
NOUN=(input("enter a noun")).strip
PLACE=(input("enter a place")).strip
VERB=(input("enter a verb")).strip
ADVERB=(input("enter a adverb")).strip
FOOD2=(input("enter a food")).strip
THINGS=(input("enter a thing")).strip


print(f"Today we picked apple from {PERSON}'s Orchard. I had no idea there were so many different varieties of apples. I ate {ADJECTIVE} apples straight off the tree that tasted like {FOOD}. Then there was a {ADJECTIVE2} apple that looked like a {NOUN}.  When our bag was full, we went on a free hay ride to {PLACE} and back. It ended at a hay pile where we got to {VERB} {ADVERB}. I can hardly wait to get home and cook with the apples. We are going to make appple {FOOD2} and {THINGS} pies!")