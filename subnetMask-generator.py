from random import randint

# Choose subnet bytes at random
def pick_num():
    # list of valid subnet bytes
    list = [0, 128, 192, 224, 240, 248, 252, 254, 255]

    random = randint(0,8)
    num = list[random]
    return num

# Return a random subnet mask as a string
def generate_netmask():
    current_byte = 0
    submask_mask = ""
    count = 1
    while count <= 4:
        current_byte = pick_num()
        if current_byte == 255:
            submask_mask += str(current_byte) + "."
            count += 1
        else:
            submask_mask += str(current_byte) + "."
            count += 1
            break

# This will make sure there is no period after the last octet
    while count != 5:
        if count != 4:
            submask_mask += "0."
            count += 1
        elif count == 4:
            submask_mask += "0"
            count += 1

    return submask_mask


print(generate_netmask())
