"""
There are six characters in the game Cluedo (Miss Scarlett, Professor Plum, Mrs Peacock, Reverend
Green, Colonel Mustard and Dr Orchid).
Create a list with these names in it.
Use a FOR loop to go through the list, displaying for each name in turn the prompt “Do you find the
accused, <character name>, guilty or not guilty?”. The user should enter “Guilty” or “Not Guilty”.
Create a fully commented program to do this.
"""
band = ["Miss Scarlett", "Professor Plum", "Mrs Peacock", "Reverend Green","Colonel Mustard", "Dr Orchid"]
for member in band:
    print("Do you find the accused,", member, ", guilty or not guilty?")
    n = str(input())
