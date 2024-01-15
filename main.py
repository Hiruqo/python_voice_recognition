import speech_recognition as sr     # pip library
import re

# recognize speech function
def recognize_speech():
    recognizer = sr.Recognizer()    # 'recognizer' object start

    with sr.Microphone() as source:     # set microphone peripherial as audio source
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source, duration=1)     # set the environmental (sound) settings
        audio = recognizer.listen(source)   # start listening to user's microphone

    try:
        text = recognizer.recognize_google(audio)   # google cloud tries to detect words
        print("You said:", text)    # print what user said
        return text
    except sr.UnknownValueError:    # unknown text
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:    # Error code print
        print(f"Google Speech Recognition request failed: {e}")
        return None

# make a calculation
def calculate(expression):
    try:
        # Remove non-alphanumeric characters except '*', '/', '+', and '-'
        expression = re.sub(r'[^0-9+\-*/. ]', '', expression)
        result = eval(expression)
        print("Result:", result)
    except Exception as e:
        print("Error during calculation:", e)

# main function
def main():
    while True:
        input_text = recognize_speech()

        if input_text:
            if "exit" in input_text.lower():
                print("Exiting...")
                break
            else:
                calculate(input_text)

# executing main function
if __name__ == "__main__":
    main()