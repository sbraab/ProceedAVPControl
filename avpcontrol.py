#!/usr/bin/python

import serial, string, binascii, sys, array, struct, os
output = " "

os.system("touch /tmp/avplastrun")
ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)

commands = dict()
commands['Path_Both']="\x02\x02\x28\x7E\x01"
commands['Path_Main']="\x02\x02\x26\xBA\x80"
commands['Path_Toggle']="\x02\x02\x0F\x64\x41"
commands['Path_Remote']="\x02\x02\x27\x7A\x41"
commands['Disc1']="\x02\x02\x04\xA3\x00"
commands['Video_Next']="\x02\x02\x5A\x5B\x81"
commands['Video_Prev']="\x02\x02\x4B\x57\x41"
commands['Satellite']="\x02\x02\x01\xA0\xC0"
commands['TV']="\x02\x02\x0D\xA5\xC0"
commands['VCR1']="\x02\x02\x0C\x65\x01"
commands['VCR2']="\x02\x02\x14\x6F\x01"
commands['Aux']="\x02\x02\x15\xAF\xC0"
commands['CD']="\x02\x02\x02\xA1\x80"
commands['More_Toggle']="\x02\x02\x06\x62\x81"
commands['Aux1']="\x02\x02\x5B\x9B\x40"
commands['Aux2']="\x02\x02\x5C\x59\x01"
commands['Aux3']="\x02\x02\x5D\x99\xC0"
commands['Aux4']="\x02\x02\x5E\x98\x80"
commands['Aux5']="\x02\x02\x5F\x58\x41"
commands['Aux6']="\x02\x02\x60\x48\x01"
commands['Aux7']="\x02\x02\x61\x88\xC0"
commands['Aux8']="\x02\x02\x62\x89\x80"
commands['Audio_Next']="\x02\x02\x96\x0E\x81"
commands['Audio_Prev']="\x02\x02\x87\x02\x41"
commands['Tape']="\x02\x02\x05\x63\xC1"
commands['Tuner']="\x02\x02\x0E\xA4\x80"
commands['BALANCE']="\x02\x02\x10\xAC\x00"
commands['CENTER']="\x02\x02\x19\xAA\xC0"
commands['Volume1']="\x02\x02\x36\x76\x81"
commands['Volume2']="\x02\x02\x37\xB6\x40"
commands['Volume3']="\x02\x02\x38\xB2\x00"
commands['Volume4']="\x02\x02\x39\x72\xC1"
commands['Volume5']="\x02\x02\x3A\x13\x80"
commands['LEVEL']="\x02\x02\x0A\x67\x81"
commands['MASTER']="\x02\x02\x08\xA6\x00"
commands['MUTE']="\x02\x02\x1A\xAB\x80"
commands['REAR']="\x02\x02\x09\x66\xC1"
commands['Volume_Down']="\x02\x03\xC3\xA1\x40"
commands['Volume_Up']="\x02\x03\xD2\xAD\x80"
commands['DualDrive_Toggle']="\x02\x02\x63\x49\x41"
commands['LateNight_Off']="\x02\x02\x2E\x7C\x81"
commands['LateNight_On']="\x02\x02\x2D\x7D\xC1"
commands['Mute_Off']="\x02\x02\x2C\xBD\x00"
commands['Mute_On']="\x02\x02\x2B\x7F\x41"
commands['Operate']="\x02\x02\x29\xBE\xC0"
commands['Projector_Off']="\x02\x02\x43\x91\x40"
commands['Projector_On']="\x02\x02\x42\x51\x81"
commands['Standby']="\x02\x02\x2A\xBF\x80"
commands['Sub_Toggle']="\x02\x02\x4C\x95\x00"
commands['Trigger1_Off']="\x02\x02\x33\x75\x41"
commands['Trigger1_On']="\x02\x02\x32\xB5\x80"
commands['Trigger2_Off']="\x02\x02\x35\x77\xC1"
commands['Trigger2_On']="\x02\x02\x34\xB7\x00"
commands['LateNight_Toggle']="\x02\x02\x50\x5C\x01"
commands['DTSFilm']="\x02\x02\x64\x8B\x00"
commands['DTSMusic']="\x02\x02\x66\x4A\x81"
commands['DTSTHX']="\x02\x02\x65\x4B\xC1"
commands['MODE']="\x02\x02\x16\xAE\x80"
commands['Mono']="\x02\x02\x25\xBB\xC0"
commands['MonoSurround']="\x02\x02\x23\xB9\x40"
commands['ProLogic']="\x02\x02\x21\x78\xC1"
commands['ProLogicTHX']="\x02\x02\x20\xB8\x00"
commands['StereoSurround']="\x02\x02\x22\x79\x81"
commands['SurroundOff']="\x02\x02\x24\x7B\x01"
commands['THX_Off']="\x02\x02\x31\xB4\xC0"
commands['THX_On']="\x02\x02\x30\x74\x01"
commands['THX_Toggle']="\x02\x02\x51\x9C\xC0"
commands['DELAY']="\x02\x02\x12\x6D\x81"
commands['DisplayIntensity']="\x02\x02\x07\xA2\x40"
commands['MENU']="\x02\x02\x3C\x71\x01"
commands['RECALL']="\x02\x02\x17\x6E\x41"
commands['Special']="\x02\x02\x69\x4E\xC1"
commands['Standby_Toggle']="\x02\x02\x18\x6A\x01"
commands['Status']="\x02\x02\x4F\x94\x40"
commands['SUB']="\x02\x02\x11\x6C\xC1"
commands['ENTER']="\x02\x02\x78\x42\x01"

source=["", "VCR1", "DISC1", "VCR2", "TV", "SAT", "CD", "TAPE", "AUX",
 "TUNER", "MORE1", "MORE2", "MORE3", "MORE4", "MORE5", "MORE6", "MORE7", "MORE8"]
volume=[0, 1, 3, 5, 7, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
 25, 26, 27, 28, 29, 30, 31, 31.5, 32, 32.5, 33, 33.5, 34, 34.5, 35, 35.5, 36, 36.5,
 37, 37.5, 38, 38.5, 39, 39.5, 40, 40.5, 41, 41.5, 42, 42.5, 43, 43.5, 44, 44.5, 45,
 45.5, 46, 46.5, 47, 47.5, 48, 48.5, 49, 49.5, 50, 50.5, 51, 51.5, 52, 52.5, 53, 53.5,
 54, 54.5, 55, 55.5, 56, 56.5, 57, 57.5, 58, 58.5, 59, 59.5, 60, 60.5, 61, 61.5, 62,
 62.5, 63, 63.5, 64, 64.5, 65, 65.5, 66, 66.5, 67, 67.5, 68, 68.5, 69, 69.5, 70, 70.5,
 71, 71.5, 72, 72.5, 73, 73.5, 74, 74.5, 75, 75.5, 76, 76.5, 77, 77.5, 78, 78.5, 79,
 79.5, 80, 80.5, 81, 81.5, 82, 82.5, 83, 83.5, 84, 84.5, 85, 85.5, 86, 86.5, 87, 87.5,
 88, 88.5, 89, 89.5, 90, 90.5, 91, 91.5, 92]
application=["PCM", "AC-3", "DTS", "MPEG", "96k_PCM"]
surround=["Discrete", "ProLogic", "ProLogicTHX", "Stereo_Surround", "Mono_Surround", "Stereo", "Mono"]

logf = open('/tmp/avplog', 'a')
logf.write(sys.argv[1]+'\n')
logf.close()


if str(sys.argv[1])=="status":
    ser.write("\x02\x02\x76\x86\x80")
    status=array.array("B")
    output=ser.read(size=35)    
    result =  "src:"+source[struct.unpack('B', output[6])[0]]+" "
    result += "vol:"+ str(volume[struct.unpack('B', output[9])[0]]) + " "
    if output[13]=='\xff':
        result += "app:No_Signal "
    else:
        result += "app:"+application[struct.unpack('B', output[13])[0]]+" "
    result +=  "sur:"+surround[struct.unpack('B', output[15])[0]]+" "
    result += "fp:" + output[20]+ output[21]+ output[22]+ output[23]+ output[24]+ output[25]+ output[26]+ output[27]+ output[28]+ output[29]+ output[30]+ output[31]
    print result
else:
    ser.write(commands[str(sys.argv[1])])
    output = ser.read(size=4)
    if output == "\x01\x55\x3f\xc0":
        print "OK"
    else:
	print "ERROR"

