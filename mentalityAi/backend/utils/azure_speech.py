import azure.cognitiveservices.speech as speechsdk
from typing import Optional

class AzureSpeechService:
    def __init__(self, speech_key: str, service_region: str):
        """
        Initialize Azure Speech Service with credentials.
        
        Args:
            speech_key (str): Azure Speech Service API key
            service_region (str): Azure region (e.g., 'centralindia')
        """
        self.speech_config = speechsdk.SpeechConfig(
            subscription=speech_key, 
            region=service_region
        )
        self.audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        self.output_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

        # Set default language for speech recognition and synthesis
        self.speech_config.speech_recognition_language = "en-US"
        self.speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"

        # Initialize recognizer and synthesizer
        self.speech_recognizer = speechsdk.SpeechRecognizer(
            speech_config=self.speech_config,
            audio_config=self.audio_config
        )
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=self.speech_config, 
            audio_config=self.output_config
        )

    def recognize_speech(self) -> Optional[str]:
        """
        Perform speech recognition from microphone input.
        
        Returns:
            Optional[str]: Recognized text or None if recognition failed
        """
        print("Listening... Speak into your microphone.")
        
        try:
            result = self.speech_recognizer.recognize_once()
            
            if result.reason == speechsdk.ResultReason.RecognizedSpeech:
                print(f"Recognized: {result.text}")
                return result.text
            elif result.reason == speechsdk.ResultReason.NoMatch:
                print("No speech could be recognized.")
            elif result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = result.cancellation_details
                print(f"Speech Recognition canceled: {cancellation_details.reason}")
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    print(f"Error details: {cancellation_details.error_details}")
            return None
            
        except Exception as e:
            print(f"Error during speech recognition: {str(e)}")
            return None

    def synthesize_speech(self, text: str) -> bool:
        """
        Convert text to speech.
        
        Args:
            text (str): Text to convert to speech
            
        Returns:
            bool: True if synthesis was successful, False otherwise
        """
        if not text:
            print("No text provided for synthesis.")
            return False
            
        print("Converting text to speech...")
        
        try:
            result = self.speech_synthesizer.speak_text_async(text).get()
            
            if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                print("Speech synthesis completed successfully.")
                return True
            elif result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = result.cancellation_details
                print(f"Speech synthesis canceled: {cancellation_details.reason}")
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    print(f"Error details: {cancellation_details.error_details}")
            return False
            
        except Exception as e:
            print(f"Error during speech synthesis: {str(e)}")
            return False

    def save_synthesized_speech(self, text: str, output_file: str) -> bool:
        """
        Save synthesized speech to an audio file.
        
        Args:
            text (str): Text to convert to speech
            output_file (str): Path to save the output audio file
            
        Returns:
            bool: True if synthesis and saving were successful, False otherwise
        """
        if not text:
            print("No text provided for synthesis.")
            return False

        print(f"Saving synthesized speech to {output_file}...")
        
        try:
            audio_config = speechsdk.audio.AudioOutputConfig(filename=output_file)
            synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=audio_config)
            result = synthesizer.speak_text_async(text).get()

            if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                print("Speech synthesis saved successfully.")
                return True
            elif result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = result.cancellation_details
                print(f"Speech synthesis canceled: {cancellation_details.reason}")
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    print(f"Error details: {cancellation_details.error_details}")
            return False
            
        except Exception as e:
            print(f"Error during speech synthesis: {str(e)}")
            return False

def main():
    # Replace with your Azure Speech Service API Key and Region
    SPEECH_KEY = "4UKXPpnOGIwfOYVcSJ6pDqQ9TkT9hmn2ghpB9YZZXSeaLw0BuBszJQQJ99BAACGhslBXJ3w3AAAYACOGKP8h"
    SERVICE_REGION = "centralindia"
    
    # Initialize speech service
    speech_service = AzureSpeechService(SPEECH_KEY, SERVICE_REGION)
    
    # Perform speech-to-text
    recognized_text = speech_service.recognize_speech()
    
    # If text was recognized, perform text-to-speech
    if recognized_text:
        speech_service.synthesize_speech(recognized_text)
        # Optionally, save the synthesized speech to a file
        speech_service.save_synthesized_speech(recognized_text, "output_audio.wav")

if __name__ == "__main__":
    main()