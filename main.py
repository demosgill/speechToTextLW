import speech_recognition as sr
import sys
import os

"""
Main function for transcribing audio into text format.
Parameters are:
- Duration of the audio one wants to transcribe: Seconds
- Filename of the resulting .txt file: Default is ./default.txt
"""

def writeFile(fname, text):
    file = open(fname, "w")
    file.write(text)
    file.close()

def main(audioDuration, fileName):
    # Instantiate object
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # read audio data from default microphone
        print("Listening ...")
        audio_data = r.record(source, duration=int(audioDuration))

        print("Recognizing ...")
        text = r.recognize_google(audio_data)

    print("Saving output ...")
    # Save file
    writeFile(fileName, text)

    print("Done.")


#------------------------------------------------
if __name__ == "__main__":
    """
    DESCRIPTION:    
    In order to save a 5 second audio into text format, run the following:
    
    python main.py 5 default.txt
     
    The method will listen the audio and translate it into text format. 
    File will be saved as defined by the second input argument, i.e. default.txt
    """
    main(sys.argv[1], sys.argv[2])


