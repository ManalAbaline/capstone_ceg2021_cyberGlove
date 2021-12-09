import serial
import time
import schedule
from datetime import datetime

# define the bend values for each finger
# these values are gathered from the flex sensors
thumb_bend = 0               #corresponds to index 0
index_finger_bend = 0        #corresponds to index 1
middle_finger_bend = 0       #corresponds to index 2
ring_finger_bend = 0         #corresponds to index 3
pinky_bend = 0               #corresponds to index 4

counter = 1
current_word = ""
current_sentence = ""
bend_list = []

# define list of letters and corresponding bend values
alphabet_database = {
    "h": [[40,50], [0,5], [0,5], [85,95], [85,95]],         # estimated values: [45, 0, 0, 90, 90]
    "e": [[85,95], [40,50], [40,50], [40,50], [40,50]],     # estimated values: [90, 45, 45, 45, 45]
    "l": [[0,5], [0,5], [85,95], [85,95], [85,95]],         # estimated values: [0, 0, 90, 90, 90]
    "o": [[70,80], [70,80], [70,80], [70,80], [70,80]],     # estimated values: [75, 75, 75, 75, 75]
    "w": [[85,95], [0,5], [0,5], [0,5], [85,95]],           # estimated values: [90, 0, 0, 0, 90]
    "a": [[0,5], [85,95], [85,95], [85,95], [85,95]],       # estimated values: [0, 90, 90, 90, 90]
    "r": [[0,5], [0,5], [0,5], [85,95], [85,95]],           # estimated values: [0, 0, 0, 90, 90]
    "y": [[0,5], [85,95], [85,95], [85,95], [0,5]],         # estimated values: [0, 90, 90, 90, 0]
    "u": [[40,50], [0,5], [0,5], [40,50], [40,50]]          # estimated values: [45, 0, 0, 45, 45]
}


# function for bend values analysis
def bend_analysis(thumb_fb, index_fb, middle_fb, ring_fb, pinky_fb):
    for letter in alphabet_database:
        correspond_thumbfb = thumb_fb in range(alphabet_database[letter][0][0], alphabet_database[letter][0][1])
        correspond_indexfb = index_fb in range(alphabet_database[letter][1][0], alphabet_database[letter][1][1])
        correspond_middlefb = middle_fb in range(alphabet_database[letter][2][0], alphabet_database[letter][2][1])
        correspond_ringfb = ring_fb in range(alphabet_database[letter][3][0], alphabet_database[letter][3][1])
        correspond_pinkyfb = pinky_fb in range(alphabet_database[letter][4][0], alphabet_database[letter][4][1])
        if correspond_thumbfb and correspond_indexfb and correspond_middlefb and correspond_ringfb and correspond_pinkyfb:
            return letter


def perform_analysis(input_values):
	global current_word
    global current_sentence
	global counter
	global bend_list
	#If the bend_list changed, it means that new data was acquired 
	if bend_list != input_values:
		current_word += bend_analysis(input_values[0], input_values[1], input_values[2], input_values[3], input_values[4])
		bend_list = input_values
	#If the bend list does not change, it means that the user did not change their hand gestures
	#which implies that it is a new word
	else:
		current_sentence += " "
        current_sentence += current_word
		current_word = ""
		
	current_sentence += " "
        current_sentence += current_word
	
	print("current analysed word: ")
    print(current_word)
	print("current analysed sentence: ")
    print(current_sentence)
	
    counter += 1
    
    
    

def main_func():
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()
    
    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split('x')
    
    list_in_floats = []
    for item in list_values:
       list_in_floats.append(float(item))
        

    # perform analysis
    perform_analysis(list_in_floats)
    
    # reset values for next iteration
    arduino_data = 0
    list_in_floats = []
    list_values = []
    decoded_values = ""
    arduino.close()
    print("Connection closed")
    print('<--------------------------->')
    
# ------------------------- Main Code -------------------------
# Declare variables to be used
list_values = []
decoded_values = ""



print("Program started")

#setting up the arduino
schedule.every(5).seconds.do(main_func)

while True:
    schedule.run_pending()
    time.sleep(1)