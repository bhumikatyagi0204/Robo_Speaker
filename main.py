import win32com.client
def robo_speaker(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

if __name__ == '__main__':
    print("Welcome to Robo Speaker 1.1 Created By Bhumika Tyagi")
    while True:
        text = input("Enter what you want me to speak :- ")
        if text == "q":
            robo_speaker("Bye Bye friend")
            break
        robo_speaker(text)

""" 1.def robo_speaker(text):: This line defines a function named robo_speaker that takes one parameter, text. This function is designed to speak out the provided text.

2.speaker = win32com.client.Dispatch("SAPI.SpVoice"): This line creates a Dispatch object using the win32com.client module. This object represents an instance of the Windows Speech API (SAPI) voice. By specifying "SAPI.SpVoice" as the argument to Dispatch, we are telling Python to create an instance of the SAPI voice.

3.speaker.Speak(text): This line calls the Speak method on the speaker object, passing the text parameter as an argument. This method causes Windows to speak out the provided text using its built-in text-to-speech capabilities.

In summary, the robo_speaker function encapsulates the logic for speaking out the provided text using the Windows Speech API. It first creates an instance of the SAPI voice and then calls the Speak method on that instance to make Windows speak the text. """
