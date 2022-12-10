from bs4 import BeautifulSoup
import requests

# Set the base URL for the website
base_url = "https://www.dictionary.com/browse/"

# Open the words.txt file in write mode
with open("words.txt", "w") as f:
    # Loop through the letters of the alphabet
    for letter in range(ord("a"), ord("z") + 1):
        # Set the URL for the current letter
        url = base_url + chr(letter)

        # Make a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, "html.parser")

            # Get the list of words on the page
            words = soup.find("h1", {"class": "css-1sprl0b e1wg9v5m5"}).find_all("li")

            # Write each word to the file
            for word in words:
                f.write(word.text + "\n")
