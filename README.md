# ProgrammingChallenge
This is the programmed tasked by Durr Dental to test the programming skills of their candidates.
 1. Create a websocket connection to the echo server at "ws://echo.websocket.org"
 2. Can sent data to the echo server and received the data back
 3. The program can send integer, string and json file to the  echo server
 4. The program was written to run on Python3
 
# How it works
Download both scripts and save them into a single file.

To run the program, user must install the following library in your PC:
1. Websocket-client
2. Pathlib 

Then, open command prompt or any command line interface and run the following 
> python websocket_lsg.py

If users want to replace the pre-set parameters, the following command can be used.  
The input can be **in any order** and **no quotation marks ("") needed**:
 > python websocket_lsg.py int string json_file_name   
 >> Example : python websocket_lsg.py testing 1103 another.json 

[Note!] Make sure all the json files are in the same folder as the script!

# Testing the program using TDD and pytest
Make sure you have the **pytest** library installed first.
To test the pogram, users can run websocket_test.py
>> py.test websocket_test.py

The purpose of this test is to check that the functions in the program are working properly.  You will some passed test and failed test.

## Have fun trying!
