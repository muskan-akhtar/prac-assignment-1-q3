#UNDERSTANDING STRING LITERALS#
full_name = "Muskan Akhtar"
print(full_name.upper())
print(full_name.lower())
print(full_name.title())

"""
OUTPUT 
MUSKAN AKHTAR
muskan akhtar
Muskan Akhtar

"""


messy_text = "  Python programming is fun!  "
print(messy_text.strip(), "All the extra spaces at the biggening and the end has been removed successfully!")
print(messy_text.replace("fun" , "amazing"))
print(messy_text.count("i") ,"....i's in the sentence")

"""
OUTPUT = 
Python programming is fun! All the extra spaces at the biggening and the end has been removed successfully!
  Python programming is amazing!
2 ....i's in the sentence
"""

sentence = "The quick brown fox jumps over the lazy dog!"
print("_".join(sentence.split()))
print(sentence.startswith("The")) #check if the sentence startswith the or not#
print(sentence.find("fox"))


"""
OUTPUT=
The_quick_brown_fox_jumps_over_the_lazy_dog!
True
16
"""

name = input("What is your name?")
age = int(input("What is your age?"))
favoriteprogramminglan = input("What's your favorite programming language?")

sentence1 = f"My name is {name} and I am {age} years old."
sentence2 = f"I enjoy programming in {favoriteprogramminglan}, it's my favorite programming language!"
sentence3 = f"In 6 years, I will be {age + 6} years old."

print(sentence1, sentence2, sentence3)


"""
OUTPUT= 
What is your name?muskan
What is your age?20
What's your favorite programming language?python
My name is muskan and I am 20 years old. I enjoy programming in python, it's my favorite! In 6 years, I will be 26 years old.

"""


first_name = input("What is your first name?")
last_name = input("what is your last name?")
birth_year = int(input("What is your birth year?"))
current_year = 2025

print(first_name.capitalize())
print(last_name.capitalize())

age = current_year - birth_year
username = f"{first_name[0].lower()}{last_name.lower()}{birth_year}"


profilemessage = f"Profile:{first_name} {last_name}, Age:{age}, Username:{username}"

print(profilemessage)


"""
OUTPUT=
What is your first name?m
what is your last name?a
What is your birth year?2005
M
A
Profile:m a, Age:20, Username:ma2005
"""