import requests

# URL for the online English dictionary
url = "https://www.english-dictionary.org/{}"

# Open the file for writing
with open("words.txt", "w") as f:
    # Query for each letter of the alphabet
    for letter in "abcdefghijklmnopqrstuvwxyz":
        # Send a GET request to the URL
        response = requests.get(url.format(letter))
        # If the request was successful
        if response.status_code == 200:
            # Parse the response as HTML
            html = response.text
            # Split the HTML into words
            words = html.split()
            # Write each word to the file
            for word in words:
                f.write(word + "\n")
