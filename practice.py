name ="MuskanAkhtar"
print (name.isupper()) #checks if the string is in uppercase if not then it return false
print (name.isalnum()) #check if the string contains a space if not then return true bcz it doesnot allow any special characters or space between string...


name="   MuskanAkhtar   "
print (name.strip()) #removes all the extra spaces from strats to end in the string

name="MuskanAkhtar"
print(" ".join(name)) #it joins whatever u give it to join with a string

name="Muskan Akhtar" #two methods of splitting
print (name.split()) #string in seperate square braces 
print (name.split('/')) #all string in 1 square bracket

name="Muskan Akhtar"
print (name.index('h')) #checks the index of the given character

name="Muskan Akhtar"
print (name.replace('Muskan','Shaheer')) #replaces the given strings

name ="muskan akhtar"
print (name.islower()) #checks if all characters of string are lower

count="Muskan Akhtar"
print (count.count('a')) #checks how many times the character appears in the given string

searching="Muskan Akhtar"
print (searching.find('kan')) #it is the finding method which helps to find the desired characters in the texts/stings