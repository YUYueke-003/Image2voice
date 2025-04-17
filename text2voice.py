from transformers import pipeline
from datasets import load_dataset
import soundfile as sf
import torch

def text2voice(text):
    """
    Convert text to voice using a pre-trained TTS model.
    
    :param text: The text to convert to speech.
    :return: None
    """
    # Load the TTS model
    synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")

    # Load the speaker embedding dataset
    embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
    
    # Select a specific speaker embedding
    speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
    
    # Generate speech
    speech = synthesiser(text, forward_params={"speaker_embeddings": speaker_embedding})
    
    # Save the generated speech to a file
    sf.write("speech.wav", speech["audio"], samplerate=speech["sampling_rate"])

if __name__ == "__main__":
    # Example text to convert to speech
    text = "Hello, this is a text-to-speech conversion example."
    
    # Convert text to voice
    text2voice(text)
    
    print("Speech generated and saved as 'speech.wav'.")

