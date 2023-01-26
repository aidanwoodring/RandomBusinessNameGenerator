# This code uses the Datamuse API (https://www.datamuse.com/api/) to search for related words 
# based on the keyword input by the user. It then selects a random word from the search results 
# and combines it with the keyword to create a random business name. In this example, it is using "Co" 
# as the company's name, you can change it as per your requirement.

import random
import requests

def generate_name(keywords, num_results):
    # Use the keyword to search for related words on the internet
    keywords_list = keywords.split(",")
    search_results = []
    for keyword in keywords_list:
        search_url = "https://api.datamuse.com/words?rel_jjb=" + keyword
        search_results += requests.get(search_url).json()
    
    # Create a list to store the generated names
    names_list = []
    for i in range(num_results):
        # Choose a random word from the search results
        adj = random.choice(search_results)['word']
        # Use the keyword and chosen word to create a random business name
        name = adj + " " + keyword + " " + "Co"
        names_list.append(name)
    return names_list

# Get input from the user
keywords = input("Enter a comma separated keywords for your business name: ")
num_results = int(input("Enter the number of results you want to generate: "))

# Generate and print the business names
names_list = generate_name(keywords, num_results)
print("Generated Business names:")
for name in names_list:
    print(name)

# Menu interaction to generate new list
while True:
    regenerate = input("Do you want to generate new names? (y/n): ")
    if regenerate.lower() == "y":
        keywords = input("Enter a comma separated keywords for your business name: ")
        num_results = int(input("Enter the number of results you want to generate: "))
        names_list = generate_name(keywords, num_results)
        print("Generated Business names:")
        for name in names_list:
            print(name)
    elif regenerate.lower() == "n":
        break
    else:
        print("Invalid input. Please enter y or n.")