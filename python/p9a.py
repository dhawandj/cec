# 9 Aim: Demonstration of working with excel spreadsheets and web scraping
# a) Write a python program to download the all XKCD comics
import requests
import os
def download_xkcd_comics():
        # Create a directory to store the comics
        os.makedirs('xkcd', exist_ok=True)
        # Start from the first comic
        url = 'https://xkcd.com/1/info.0.json'
        while True:
                # Fetch the comic metadata
                response = requests.get(url)
                response.raise_for_status()
                comic_data = response.json()
                # Extract the image URL
                image_url = comic_data['img']
                # Download the image
                response = requests.get(image_url)
                response.raise_for_status()
                # Save the image to the xkcd directory
                image_name = image_url.split('/')[-1]
                image_path = os.path.join('xkcd', image_name)
                with open(image_path, 'wb') as image_file:
                        image_file.write(response.content)
                # Print the comic title and number
                print(f"Downloaded: {comic_data['title']} - #{comic_data['num']}")
                # Check if there's a next comic
                if comic_data['num'] == 1:
                        break
                else:
                # Get the URL of the previous comic

                        url = f"https://xkcd.com/{comic_data['num'] - 1}/info.0.json"
                
print('All XKCD comics downloaded successfully!')
# Run the program
download_xkcd_comics()

# Output:
# Downloaded: Barrel - Part 1 - #1
# All XKCD comics downloaded successfully!