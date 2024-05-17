# YouTuber Trading Card Generator

This project generates personalized trading cards for YouTubers by fetching their channel data, avatar, and quotes using web scraping and the YouTube Data API, and then composes the information into an image.

## Features

- Fetch YouTuber data such as channel statistics, avatar, and quotes.
- Create a trading card image with the fetched data.
- Rank YouTubers based on their statistics.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/youtuber-trading-card-generator.git
    cd youtuber-trading-card-generator
    ```

2. Install the required Python libraries:
    ```sh
    pip install -r requirements.txt
    ```

    Make sure your `requirements.txt` includes:
    ```
    requests
    beautifulsoup4
    google-api-python-client
    oauth2client
    pillow
    lxml
    ```

3. Add your YouTube Data API key to the code:
    Replace `'YOUR_API_KEY'` with your actual YouTube Data API key in the `get_stats` function.

## Usage

1. Run the script:
    ```sh
    python main.py
    ```

2. Enter the YouTuber's username when prompted.

3. The script will generate a trading card image and save it in the current directory.

## Functions

### `get_quote(name)`

Fetches a quote about the YouTuber from their fandom wiki page.

### `filter_sentences(text)`

Filters out unwanted links from the text.

### `get_image(name)`

Fetches the YouTuber's channel logo image and saves it locally.

### `get_channel_id(name)`

Fetches the YouTuber's channel ID.

### `get_stats(channel_id)`

Fetches the YouTuber's channel statistics using the YouTube Data API.

### `load_image()`

Creates a blank image with the desired dimensions and loads a card template.

### `add_text(image, quote, channel_data)`

Adds text, including the quote and channel statistics, to the image.

### `add_avatar(base_image, name)`

Adds the YouTuber's avatar to the image.

### `add_rank(image_with_avatar, channel_data)`

Calculates and adds a rank to the image based on the channel statistics.
