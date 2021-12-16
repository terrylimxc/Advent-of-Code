from math import prod

def convert_packet(packet):
    hex2bin = {'0': "0000", '1': "0001", '2':"0010", '3':"0011", '4':"0100",
               '5':"0101", '6':"0110", '7':"0111", '8':"1000", '9':"1001",
               'A':"1010", 'B':"1011", 'C':"1100", 'D':"1101",
               'E':"1110", 'F':"1111"}
    temp = ""
    for i in packet:
        temp += hex2bin[i]
    return temp

def literal_value(pos, packet):
    val = ""
    flag = True
    while flag:
        if packet[pos] == '0': # Last Group
            flag = False
        pos += 1
        val += packet[pos:pos+4]
        pos += 4 # Move pos to the right by 4

    # Convert Binary to Decimal
    val = int(val,2)
    
    return val, pos

# Part 1
def decode(packet, pos):
    literal_val = 0
    
    # Obtain Packet Header (Version and type ID)
    ver, type_id = int(packet[pos:pos+3],2), int(packet[pos+3:pos+6],2)

    # Add Version
    global TOTAL
    TOTAL += ver
    
    # Packet with type ID 4 (Literal Value)
    if type_id == 4:
        val, pos = literal_value(pos+6, packet)
        literal_val += val
        
    else: # Packet type ID not 4 (Operator)
        length_type_id = packet[pos+6]
        values = []
        
        # Type 0
        if length_type_id == '0':
            total_length = int(packet[pos+7:pos+22],2)

            pos += 22
            pointer = pos
            while pos != pointer+total_length:
                pos, new_values = decode(packet,pos)
                values.append(new_values)
                
        # Type 1
        else:
            total_num = int(packet[pos+7:pos+18],2)
            pos += 18
            for _ in range(total_num):
                pos, new_values = decode(packet,pos)
                values.append(new_values)

        # Check Packet Type
        if type_id == 0:
            literal_val = sum(values)
        elif type_id == 1:
            literal_val = prod(values)
        elif type_id == 2:
            literal_val = min(values)
        elif type_id == 3:
            literal_val = max(values)
        elif type_id == 5:
            literal_val = 1 if values[0] > values[1] else 0
        elif type_id == 6:
            literal_val = 1 if values[0] < values[1] else 0
        elif type_id == 7:
            literal_val = 1 if values[0] == values[1] else 0

    return pos, literal_val

# Puzzle
with open('puzzle.txt') as f:
    for line in f:
        packet = line.strip()
        break
f.close()

# For Puzzle
TOTAL = 0 
# Convert packet from Hexadecimal to Binary
packet = convert_packet(packet)
pos, literal_val = decode(packet, 0)
print("Part 1: {}".format(TOTAL))
print("Part 2: {}".format(literal_val))
print("------------------------")

# For Test Cases
# Part 1
lines = []
with open('test1.txt') as f:
    for line in f:
        x = line.strip()
        lines.append(x)
f.close()
print("Part 1")
for i in range(3,7):
    TOTAL = 0
    packet = lines[i]
    packet = convert_packet(packet)
    decode(packet, 0)
    print(TOTAL)
print("------------------------")

# Part 2
lines = []
with open('test2.txt') as f:
    for line in f:
        x = line.strip()
        lines.append(x)
f.close()
print("Part 2")
for i in range(8):
    TOTAL = 0
    packet = lines[i]
    packet = convert_packet(packet)
    pos, literal_val = decode(packet,0)
    print(literal_val)
