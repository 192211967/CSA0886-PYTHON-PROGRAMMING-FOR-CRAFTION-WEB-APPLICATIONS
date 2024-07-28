def length_of_last_word(s):
    words = s.split()
    return len(words[-1]) if words else 0
print(length_of_last_word("Hello World"))
print(length_of_last_word(" fly me to the moon ")) 
