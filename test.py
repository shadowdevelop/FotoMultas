from time import sleep
import datetime
import sys
import serial
os = sys.platform
print("Current OS: ", os)


TARGET_MIN_SPEED_ALLOWED = 10   # min speed to be tracked; anything slower is ignored
OPS24X_SAMPLING_FREQUENCY = 'SI'    # 10Ksps
OPS24X_TRANSMIT_POWER = 'PX'        # max power
OPS24X_MAGNITUDE_MIN = 'M>20\n'     # Magnitude must be > this
OPS24X_DECIMAL_DIGITS = 'F3'        # F-zero for no decimal reporting
OPS24X_MIN_REPORTABLE = f'R>{TARGET_MIN_SPEED_ALLOWED}\n'       # Report only > this speed
OPS24X_MAX_REPORTABLE = 'R<200\n'   # Report only < than this speed
OPS24X_UNITS_PREF = 'UC'  # "UC" for cm/s
OPS24X_BLANKS_PREF = 'BZ'           # Blanks pref: send 0's not silence
OPS24X_LIVE_SPEED = 'O1OS'          # OS cancels 9243 mode, enables no-delay speeds.  O1 only one speed
OPS24X_INBOUND_ONLY  = "R+"


serial_port = serial.Serial()  # we will initialize it in main_init()


def send_ops24x_cmd(logging_prefix,ops24x_command):
    """
    send commands to the OPS24x module

    Note regarding debug print: console_msg_prefix is printed out prior to printing the command

    """
    global serial_port
    data_for_send_str = ops24x_command
    data_for_send_bytes = str.encode(data_for_send_str)    
    serial_port.write(data_for_send_bytes)
    # Initialize message verify checking
    ser_message_start = '{'
    ser_write_verify = False
    # Print out module response to command string
    while not ser_write_verify:
        data_rx_bytes = serial_port.readline()
        data_rx_length = len(data_rx_bytes)
        #logger.info(logging_prefix + str(data_rx_bytes))
        print("Comando:" + str(ops24x_command))
        print(logging_prefix + ":" + str(data_rx_bytes))
        
        if data_rx_length != 0:
            data_rx_str = str(data_rx_bytes)
            if data_rx_str.find(ser_message_start):
                #logger.info(data_rx_str)
                ser_write_verify = True
    return ser_write_verify




serial_port = serial.Serial(            
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1,
            writeTimeout=2
        )
serial_port.port = "COM8"
serial_port.open()
serial_port.flushInput()
serial_port.flushOutput()



# send_ops24x_cmd("Send Sampling Frequency: ", OPS24X_SAMPLING_FREQUENCY)
# send_ops24x_cmd("Send Transmit Power: ", OPS24X_TRANSMIT_POWER)
# send_ops24x_cmd("Send Magnitude Control: ", OPS24X_MAGNITUDE_MIN)
# send_ops24x_cmd("Send Decimal digits: ", OPS24X_DECIMAL_DIGITS)
# send_ops24x_cmd("Send line of Min Speed To Report:", OPS24X_MIN_REPORTABLE)
# send_ops24x_cmd("Send line of Max Speed To Report: ", OPS24X_MAX_REPORTABLE)
# send_ops24x_cmd("Send Units Preference: ", OPS24X_UNITS_PREF)
# send_ops24x_cmd("Send Zeros Preference: ", OPS24X_BLANKS_PREF)
# send_ops24x_cmd("Send Force Instantaneous speeds: ", OPS24X_LIVE_SPEED)
# send_ops24x_cmd("Send Directional Preference: ", OPS24X_INBOUND_ONLY)
# send_ops24x_cmd("Send Reported Range Filter : ", "r>0")
# send_ops24x_cmd("test: ", "OT")
# send_ops24x_cmd("test: ", "OM")
# send_ops24x_cmd("test: ", "O3")
# send_ops24x_cmd("test: ", "?P")
# send_ops24x_cmd("range actualk: ", "u?")
# send_ops24x_cmd("range unit: ", "r?")

send_ops24x_cmd("range unit: ", "??")
send_ops24x_cmd("range unit: ", "??")
send_ops24x_cmd("range unit: ", "??")




# while 1==1:
#     ops24x_rx_bytes = serial_port.readline()
#     print("lectura")
#     print( str.rstrip(str(ops24x_rx_bytes.decode('utf-8', 'strict'))))