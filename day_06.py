with open("day_06_input.txt") as f:
    input = list(f.read())

    # Find start of packet
    for pos in range(4, len(input)):
        sublist = input[pos-4:pos]
        if (len(sublist) == len(set(sublist))):
            print("Start of packet: ",pos)
            break
        
    # Find start of message
    for pos in range(14, len(input)):
        sublist = input[pos-14:pos]
        if (len(sublist) == len(set(sublist))):
            print("Start of message: ",pos)
            break