# This code uses the Datamuse API (https://www.datamuse.com/api/) to search for related words 
# based on the keyword input by the user. It then selects a random word from the search results 
# and combines it with the keyword to create a random business name. In this example, it is using "Co" 
# as the company's name, you can change it as per your requirement.

import random
import requests

def generate_name(keywords):
    # Use the keyword to search for related words on the internet
    keywords_list = keywords.split(",")
    search_results = []
    for keyword in keywords_list:
        search_url = "https://api.datamuse.com/words?rel_jjb=" + keyword
        search_results += requests.get(search_url).json()
    
    # Choose a random word from the search results
    adj = random.choice(search_results)['word']
    
    # Use the keyword and chosen word to create a random business name
    name = adj + " " + keyword + " " + "Co"
    return name

# Get input from the user
keywords = input("Enter a comma separated keywords for your business name: ")

# Generate and print the business name
print(generate_name(keywords))