import requests
import bs4
from urllib.parse import quote
import re
import json
from googleapiclient.discovery import build

                                    

def get_quote(name):
    url = "https://youtube.fandom.com/wiki/" + name  
    result = requests.get(url)      
    soup = bs4.BeautifulSoup(result.text, "lxml")
    quote = soup.select('.blockquote td')[1].text
    quote = filter_sentences(quote)
    return quote

def filter_sentences(text):
    pattern = r'(https.*?)(?:\.ogg|\.mp3)'
    filtered_text = re.sub(pattern, '', text)
    return filtered_text

def get_image(name):
    urls = [
        "https://www.youtube.com/@" + name + "/featured",
        "https://www.youtube.com/c/" + name,
        "https://www.youtube.com/user/" + name
    ]

    for url in urls:
        try:
            response = requests.get(url, cookies={'CONSENT': 'YES+1'})
            response.raise_for_status()
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            data_match = re.search(r"var ytInitialData = ({.*});", str(soup.prettify()))

            if data_match:
                json_data = json.loads(data_match.group(1))
                channel_logo = json_data['header']['c4TabbedHeaderRenderer']['avatar']['thumbnails'][2]['url']
                file = requests.get(channel_logo)
                with open(str(name) + "_thumbnail.jpg", "wb") as thumbnail:
                    thumbnail.write(file.content)
                print("Thumbnail downloaded successfully.")
                return  # Exit the function if successful
            else:
                print("JSON data not found in the page:", url)

        except Exception as e:
            print(f"Error fetching data from {url}: {e}")
    
    print("Failed to retrieve channel logo for all URL formats.")

def get_channel_id(name):
    urls = [
        "https://www.youtube.com/@" + name + "/featured",
        "https://www.youtube.com/c/" + name,
        "https://www.youtube.com/user/" + name
    ]

    for url in urls:
        try:
            response = requests.get(url, cookies={'CONSENT': 'YES+1'})
            response.raise_for_status()
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            data_match = re.search(r"var ytInitialData = ({.*});", str(soup.prettify()))

            if data_match:
                json_data = json.loads(data_match.group(1))
                channel_id = json_data['header']['c4TabbedHeaderRenderer']['channelId']
                return channel_id  
            else:
                print("JSON data not found in the page:", url)
                return

        except Exception as e:
            print(f"Error fetching data from {url}: {e}")
            return
    
    print("Failed to retrieve channel id for all URL formats.")
    return

def get_stats(channel_id):
    #  API key
    api_key = 'AIzaSyBVTbXnEaxfXEu67yxe1Tdqe0bOWOaaFrc'

    # Initialize the YouTube Data API
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Call the channels.list method to retrieve channel information
    channel_info = youtube.channels().list(
        part='snippet,contentDetails,statistics',
        id=channel_id
    ).execute()

    # Check if 'items' exist and it's not empty
    if 'items' in channel_info and channel_info['items']:
        # Extract relevant information from the response
        channel_snippet = channel_info['items'][0]['snippet']
        channel_content_details = channel_info['items'][0]['contentDetails']
        channel_statistics = channel_info['items'][0]['statistics']
        
        # Create a dictionary with channel information
        channel_data = {
            'title': channel_snippet['title'],
            'description': channel_snippet['description'],
            'views': channel_statistics['viewCount'],
            'subscribers': channel_statistics['subscriberCount'],
            'video_count': channel_statistics['videoCount']
        }
        return channel_data

    else:
        # Return None
        return None


