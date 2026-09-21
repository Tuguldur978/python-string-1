# You can remove 'pass' if you written code in the function 
# Exercise 1
def count_characters(text):
    return len(text)
print(count_characters("Hello World"))
    
# Exercise 2
def remove_spaces(text):
    return text.replace(" ", "")
print(remove_spaces("Python is fun")

# Exercise 3
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for letter in text.lower():
        if letter in vowels :
            count += 1
    return count
print(count_vowels("Python is amazing"))
