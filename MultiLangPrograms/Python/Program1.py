"""Write a program to count the number of integers and characters 
in a given string. Input: "nAJh4837sj"""

def count_integers_and_characters(input_string):
    integer_count = 0
    character_count = 0

    for c in input_string:
        if c.isdigit():
            integer_count += 1
        elif c.isalpha():
            character_count += 1

    print(f"Number of integers: {integer_count}")
    print(f"Number of characters: {character_count}")

count_integers_and_characters("nAJh4837sj")