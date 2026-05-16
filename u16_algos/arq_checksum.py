
###########################################################
# Network Message Verification Using Checksum
#
# A computer receives network packets from another computer.
# The packets are stored in a text file called input.txt.
#
# Each line in input.txt stores one packet in this format:
#
# [3 digit length][message][checksum]
#
# Example:
#
# 010thisislong56
#
# This means:
# - "010" is the message length
# - "thisislong" is the message
# - "56" is the checksum sent with the message
#
# The checksum is calculated using this algorithm:
# 1. Convert each character in the message into its ASCII value.
# 2. Add up all the ASCII values.
# 3. Calculate the total modulo 256.
#
# Checksum = total ASCII value % 256
#
# A packet is valid if the calculated checksum is the same as the
# checksum provided in the packet.
#
# If the packet is valid, the receiver should reply "ACK".
# If the packet is invalid, the receiver should reply "NACK".
#
# Write a Python program to read the packets from input.txt,
# verify each message, and write the result into output.txt.
#
# The output file should store each result in this format:
#
# message -> ACK
#
# or
#
# message -> NACK
#
# Total: 25 marks
###########################################################


###########################################################
# Part (a) [4 marks]
#
# Write a function called read_file(filename).
#
# The function should read all packets from the file and return them
# as a list of strings.
#
# Example:
# read_file("input.txt")
#
# returns:
# [
#     "066Network node alpha reports stable connection after routing update.27",
#     "063Client terminal sent login request with session token attached.228"
# ]
###########################################################


def read_file(filename):
    str_list = []
    with open(filename,"r") as file:
        list = file.readlines()
    for str in list:
        str_list.append(str.strip("\n"))
    return str_list
###########################################################
# Part (b) [5 marks]
#
# Write a function called extract_messages(packet_list).
#
# The function should extract the message and checksum from each packet.
# It should return a dictionary where each message is mapped to its
# provided checksum.
#
# Example:
#
# {
#     "Network node alpha reports stable connection after routing update.": 27,
#     "Client terminal sent login request with session token attached.": 228
# }
###########################################################
def extract_messages(packet_list):
    dictionary = {}
    for packet in packet_list:
        length = int(packet[:3])
        string = packet[3:3+length]
        check_sum = int(packet[length+3:])
        dictionary[string] = check_sum
    return dictionary

###########################################################
# Part (c) [6 marks]
#
# Write a function called verify_messages(message_dict).
#
# The function should calculate the checksum of each message and compare
# it with the provided checksum.
#
# It should return a dictionary where each message is mapped to either
# "ACK" or "NACK".
#
# Example:
#
# {
#     "Network node alpha reports stable connection after routing update.": "ACK",
#     "Sensor gateway forwarded temperature readings to the main server.": "NACK"
# }
###########################################################


def verify_messages(message_dict):
    dictionary = {}


    for message,checksum in  message_dict.items():
        total = 0
        for character in message:
            total += ord(character)
        check = total % 256
        if checksum == check:
            dictionary[message] = "ACK"
        else:
            dictionary[message] = "NACK"
    return dictionary

###########################################################
# Part (d) [3 marks]
#
# Write a function called write_output(result_dict, filename).
#
# The function should write the ACK/NACK results into the output file.
#
# Each line in the output file should follow this format:
#
# message -> ACK
#
# or
#
# message -> NACK
###########################################################


def write_output(result_dict, filename):
    dictionary = result_dict
    with open(filename, "w") as file:
        for sentence, acknowledgement in dictionary.items():
            file.write(f"{sentence} -> {acknowledgement}\n")
    return file


###########################################################
# Part (e) [3 marks]
#
# Write the main program.
#
# The main program should use the functions written above to:
# - read input.txt
# - extract the messages and checksums
# - verify the messages
# - write the results into output.txt
###########################################################
file_str = read_file("input.txt")
dictionary = extract_messages(file_str)
verified_msg = verify_messages(dictionary)
write_output(verified_msg,"output.txt")
# Write your main program here
# test = 'Printer queue received document from staff laptop over wireless LAN.'
# total = 0
# for char in test:
#     total += ord(char)
# print(total % 256)

###########################################################
# Code quality [4 marks]
#
# Award marks for:
# - meaningful variable names
# - clear comments
# - proper indentation
# - appropriate use of functions
###########################################################


###########################################################
# CONTENT FOR input.txt
#
# Copy the following 10 lines into a text file called input.txt.
###########################################################

# 066Network node alpha reports stable connection after routing update.27
# 063Client terminal sent login request with session token attached.228
# 065Sensor gateway forwarded temperature readings to the main server.180
# 064Backup service completed file transfer without detecting errors.127
# 062User device requested access to the shared project repository.116
# 063Router detected packet delay during evening traffic congestion.229
# 064Payment terminal transmitted encrypted transaction data to bank.132
# 065Monitoring system raised alert after repeated failed connections.200
# 068Printer queue received document from staff laptop over wireless LAN.90
# 066Database server confirmed record update from remote office client.191


###########################################################
# EXPECTED CONTENT FOR output.txt
###########################################################

# Network node alpha reports stable connection after routing update. -> ACK
# Client terminal sent login request with session token attached. -> ACK
# Sensor gateway forwarded temperature readings to the main server. -> NACK
# Backup service completed file transfer without detecting errors. -> ACK
# User device requested access to the shared project repository. -> NACK
# Router detected packet delay during evening traffic congestion. -> ACK
# Payment terminal transmitted encrypted transaction data to bank. -> ACK
# Monitoring system raised alert after repeated failed connections. -> NACK
# Printer queue received document from staff laptop over wireless LAN. -> ACK
# Database server confirmed record update from remote office client. -> NACK



