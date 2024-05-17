import scrape
import card

def main():
    name = input('Enter YouTuber Username\n').lower().strip()  # Get and process username
    avatar = scrape.get_image(name)  # Fetch avatar
    quote = scrape.get_quote(name)  # Fetch quote
    channel_id = scrape.get_channel_id(name)  # Fetch channel ID
    channel_data = scrape.get_stats(channel_id)  # Fetch channel stats
    image = card.load_image()  # Load base image
    image_with_text = card.add_text(image, quote, channel_data)  # Add text to image
    image_with_avatar = card.add_avatar(image_with_text, name)  # Add avatar to image
    final_image = card.add_rank(image_with_avatar, channel_data)  # Add rank to image

if __name__ == "__main__":
    main()  # Run main function if script is executed directly
