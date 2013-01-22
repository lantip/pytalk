import sys
import pyttsx
import time

TXT_WHITE = "\033[1;37m"
TXT_GRAY = "\033[0;37m"
TXT_CYAN = "\033[0;36m"
TXT_PURPLE = "\033[0;35m"
TXT_BLUE = "\033[0;34m"
TXT_YELLOW = "\033[0;33m"
TXT_BOLD_GREEN = "\033[1;32m"
TXT_BOLD_RED = "\033[0;31m"
TXT_DEFAULT = "\033[0m"
TXT_BOLD_DEFAULT = "\033[1;39m"

print "****************************************************"
print "* *                                              * *"
print "*                                                  *"
print "*              Welcome to  SolusiSpeak             *"
print "*                  by " + TXT_YELLOW + "lantip" + TXT_DEFAULT + "                       *"
print "*             " + TXT_BLUE + "http://lantip.net/" + TXT_DEFAULT + "                   *"
print "*                                                  *"
print "**                                                **"
print "****************************************************"

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)
INPUT = raw_input('What did you want me to say:')
# if you want to try all the voices you have in your computer, just uncomment this lines
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice',voice.id)
#    engine.say(INPUT)

engine.say(INPUT)
engine.runAndWait()
