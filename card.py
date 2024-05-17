from PIL import Image, ImageDraw, ImageFont
import textwrap

# Create a blank image with desired dimensions
def load_image():
    width, height = 1080, 1920
    background_color = (255, 255, 255)  
    image = Image.new("RGB", (width, height), background_color)
    card_image = Image.open("card_template.png")  
    card_image = card_image.resize((width, height))
    image.paste(card_image, (0, 0))
    return image

# Add text to the card
def add_text(image, quote, channel_data):
    draw = ImageDraw.Draw(image)

    # Title
    title_font = ImageFont.truetype("Impact", 80)
    title_text = channel_data["title"]
    title_position = (380, 140)
    draw.text(title_position, title_text, font=title_font)

    # Quote
    quote_font = ImageFont.truetype("Impact", 40)
    quote_width = 45
    wrapped_quote = textwrap.fill(quote, width=quote_width)
    quote_position = (140, 1130)
    draw.text(quote_position, '"'+wrapped_quote+'"', font=quote_font)

    # Subscribers
    subscribers_font = ImageFont.truetype("Impact", 30)
    subscribers_text = f"{channel_data['subscribers']} SUBS"
    subscribers_position = (145, 1450)
    draw.text(subscribers_position, subscribers_text, fill=(255, 255, 255), font=subscribers_font)

    # Video Count
    video_count_font = ImageFont.truetype("Impact", 30)
    video_count_text = f"{channel_data['video_count']} VIDEOS"
    video_count_position = (440, 1450)
    draw.text(video_count_position, video_count_text, fill=(255, 255, 255), font=video_count_font)

    # Total Views
    views_font = ImageFont.truetype("Impact", 25)
    views_text = f"{channel_data['views']} VIEWS"
    views_position = (715, 1450)
    draw.text(views_position, views_text, font=views_font)

    # Channel Description
    description_font = ImageFont.truetype("Impact", 20)
    description_width = 95
    description_text = channel_data["description"].replace("\n\n", "\n")
    wrapped_description = textwrap.fill(description_text, width=description_width)
    description_position = (145, 1600)
    draw.text(description_position, wrapped_description, font=description_font)

    image_with_text = image
    return image_with_text

def add_avatar(base_image, name):

    filepath = str(name) + "_thumbnail.jpg"

    if base_image is None:
        raise ValueError("The base image cannot be None.")
    try:
        avatar_image = Image.open(filepath)
    except Exception as e:
        raise ValueError(f"Failed to load the avatar image from {filepath}. Error: {e}")
    new_size = (800, 806)
    resized_image = avatar_image.resize(new_size)
    position = (140, 290)
    base_image.paste(resized_image, position)    
    return base_image


def add_rank(image_with_avatar, channel_data):
    # Define your ranking criteria
    subscribers_criteria = 1000000  # Example: 1 million subscribers for SSS rank
    views_criteria = 1000000000  # Example: 1 billion views for SSS rank
    videos_criteria = 1000  # Example: 1000 videos for SSS rank
    
    # Calculate the ranking based on subscribers, views, and videos
    total_score = (int(channel_data["subscribers"]) / subscribers_criteria) + (int(channel_data["views"]) / views_criteria) + (int(channel_data["video_count"]) / videos_criteria)
    
    # Assign letter ranking based on the total score
    if total_score >= 2.5:
        rank =  "SSS"
    elif total_score >= 2.0:
        rank = "SS"
    elif total_score >= 1.5:
        rank = "S"
    elif total_score >= 1.0:
        rank = "A"
    elif total_score >= 0.5:
        rank = "B"
    elif total_score >= 0.25:
        rank = "C"
    elif total_score >= 0.1:
        rank = "D"
    elif total_score >= 0.05:
        rank = "E"
    else:
        rank = "F"

    draw = ImageDraw.Draw(image_with_avatar)

    rank_font = ImageFont.truetype("Impact", 80)
    rank_position = (155, 130)
    draw.text(rank_position, rank, font=rank_font)
    image_with_avatar.save(channel_data['title'] + "_tradingcard.png")