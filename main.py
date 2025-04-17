from image2text import generate_caption
from text2voice import text2voice

def image_to_voice(image_url):
    """
    Generate a caption for an image and convert it to speech.
    
    :param image_url: URL or path to the image.
    :return: None
    """
    # Generate a caption for the image
    caption = generate_caption(image_url)

    #Debugging output
    print(f"Generated Caption: {caption}")
    
    # Convert the caption to speech
    text2voice(caption)
    print("Speech generated and saved as 'speech.wav'.")

if __name__ == "__main__":
    # Example image URL or path
    image_url = "https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg"
    
    # Perform image-to-voice conversion
    image_to_voice(image_url)