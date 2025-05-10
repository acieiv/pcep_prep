# PCEP §1.4 – bitwise & << >>
# Bit-mask flagging – sample packed flag: packed = 0b1101 (13).
# Unpack four 1-bit sensors A-D and report which fired.


# Feeback: not sure of bitwise at all 
# an area that needs to be studied more

packed = 0b1101  # Sample packed flag (binary 1101, decimal 13)

# Define masks for each sensor
# Sensor A is at bit position 0 (rightmost bit)
mask_a = 1 << 0  # 0b0001

# Sensor B is at bit position 1
mask_b = 1 << 1  # 0b0010

# Sensor C is at bit position 2
mask_c = 1 << 2  # 0b0100

# Sensor D is at bit position 3
mask_d = 1 << 3  # 0b1000

# Check each sensor using bitwise AND and print if it fired
print(f"Packed flag (binary): {bin(packed)}")
print("Checking sensors:")

if packed & mask_a:
    print("Sensor A fired")
else:
    print("Sensor A did not fire")

if packed & mask_b:
    print("Sensor B fired")
else:
    print("Sensor B did not fire")

if packed & mask_c:
    print("Sensor C fired")
else:
    print("Sensor C did not fire")

if packed & mask_d:
    print("Sensor D fired")
else:
    print("Sensor D did not fire")
