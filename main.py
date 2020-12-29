from jarvis import Jarvis

# my jarvis object
my_jarvis = Jarvis()

my_jarvis.init()

# loop
while my_jarvis.Listening:
    text = my_jarvis.listen()

""" install all dependies
    pip install -r requirement.txt"""
