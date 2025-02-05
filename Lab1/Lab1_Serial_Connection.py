import serial
baudrates = [9600, 19200, 115200]
parities = [serial.PARITY_NONE, serial.PARITY_EVEN, serial.PARITY_ODD]

def read_block(ser_conn, num_lines):
    for line in range(num_lines):
        print(ser_conn.readline())

def query(ser_conn, message):
    ser_conn.write(message.encode())
    read_block(ser_conn, 10)

# Comment out this block and uncomment bottom section after being modified
for baudrate_for_loop in baudrates:
    for parity_for_loop in parities:
        print(baudrate_for_loop, parity_for_loop)
        serial_conn = serial.Serial('COM3', baudrate=baudrate_for_loop, parity=parity_for_loop, timeout=0.1)
        # Hit the enable (EN) on the ESP32 before this read_block finishes
        read_block(serial_conn, 50)
        serial_conn.close()
exit()  
    
# To connect to the board and input the password:
'''
serial_conn = serial.Serial('<Enter Correct Connection Port>', baudrate=<Enter Correct Baudrate>, parity=<Enter Correct Parity>, timeout=0.1)
read_block(serial_conn, 100)
passwd = '<Enter Password Here>' + '\r'
query(serial_conn, passwd)
# Retrieve Secret Info if password is correct
query(serial_conn, "wifi_info\r")
'''