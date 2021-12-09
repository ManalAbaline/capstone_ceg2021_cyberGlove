# capstone_ceg2021_cyberGlove

## Members: 
#### Ali El Achkar  
#### Lamya Abaline
#### Manal Abaline
#### Raïssa Mohamed
#### Vergenie Howayek 

## Description
Repository for Capstone project - cyber glove
- The folder "flex_sensors" has the code that allows us to acquire the data from the flex sensors and display it in the Arduino serial monitor for verification
- The folder " analysis " contain the python script that we used to analyse the bend values received from the aduino, this script is run in the Raspberry Pi and the result of it is displayed in the monitor linked to it
- The folder " SpeechToText " contain the file that has the implementation of the speech to text feature 

### Installation guidelines and step by step instructions to run the code
- Plug the Arduino Nano into the board, and upload the code.
- Once the code is uploaded, open the Serail Monitor, and The data from the flex sensors will then be displayed
- To analyse the acquired data, open a new terminal, and navigate to the python script
- run the following command: " Python analysis.py " and the analysis output will be displayed on the terminal ina continous fashion as the user is expressing the letters using their hand gestures
- For the Speech to text functionality, navigate to the script and run the following command: " python  speech-to-text.py "
