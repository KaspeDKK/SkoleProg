import os
import speech_recognition as sr

def get_audio_files(directory):
    audio_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".wav"):  # adjust for your audio file format
                audio_files.append(os.path.join(root, file))
    return audio_files

def convert_speech_to_text(file_path):
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
        try:
            # Recognize audio using Google Cloud Speech API
            text = recognizer.recognize_google(audio_data, language="da-DK")  # Danish language
            return text
        except sr.UnknownValueError:
            return "Audio not understood"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"


def extract_date_from_filename(filename):
    # The file dates-title have the format VOC_YYMMDD-XXXX.wav
    base = os.path.basename(filename)
    date_part = base.split('_')[1]
    date = date_part.split('-')[0]
    # Convert date from YYMMDD to DD-MM-YY
    date_formatted = f"{date[4:6]}-{date[2:4]}-20{date[:2]}"
    return date_formatted


def main():
    directory = "Rasmus\\Audio"  # Corrected the path for Python format
    audio_files = get_audio_files(directory)

    for file_path in audio_files:
        # Get the full transcription of the audio file
        full_text = convert_speech_to_text(file_path)
        # Extract the date from the original file name and reformat it
        date_str = extract_date_from_filename(file_path)

        # Initialize the base for new file paths with formatted date
        new_file_base = os.path.join(os.path.dirname(file_path), "LYD_" + date_str)
        new_audio_file_path = new_file_base + ".wav"
        new_text_file_path = new_file_base + ".txt"

        # Ensure the new file name is unique
        index = 1
        while os.path.exists(new_audio_file_path) or os.path.exists(new_text_file_path):
            new_audio_file_path = f"{new_file_base}_{index}.wav"
            new_text_file_path = f"{new_file_base}_{index}.txt"
            index += 1

        # Rename the audio file if it's not the same as the target file path
        if file_path != new_audio_file_path:
            os.rename(file_path, new_audio_file_path)

        # Create a text file with the full transcription
        with open(new_text_file_path, "w", encoding='utf-8') as text_file:
            text_file.write(full_text)  # Write the full transcription to the text file

if __name__ == "__main__":
    main()