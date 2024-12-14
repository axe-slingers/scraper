#A Web-Scraper for surfing Websites for information
#1.need an input url for surfing
#2.need a filtering system to narrow down the needed results(filter for :name, price, file-extension, etc...)
#3.write the output result in a file that should be named by user


#Extract the URLs .html file 

import requests
from bs4 import BeautifulSoup

import requests

def extract_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        html_content = response.text
        return html_content
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# URL to extract HTML content from
url = input("Enter URL: ")

# Extract HTML content from the URL
html_content = extract_html_content(url)

if html_content:
    # Ask the user for the file path to save the HTML content
    file_path = input("Enter the file path to save the extracted HTML content: ")

    # Save the extracted HTML content to the specified file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"HTML content saved to: {file_path}")
else:
    print("Failed to extract HTML content from the URL.")