import os
generator_poly_file_name = "generator_polynom"
input_poly_file_name = "input_polynom"

def intify(string_list):
    """Takes list of string and turns it into ints"""
    return [int(s) for s in string_list]

with open(generator_poly_file_name, "r") as generator_poly_file:
    division_polynom = intify(generator_poly_file.read().split())

with open(input_poly_file_name, "r") as input_poly_file:
    input_list = intify(input_poly_file.read().split())

# input_list = [1] + [0 for i in range(1, 16)]
# division_polynom = [1, 1, 1, 0, 0]

num_regs = len(division_polynom)
# change till here

def poly_xor(a, feedback, poly):
    """Accepts two numbers to xor. a is the value of the last register. Feedback comes from the the division
    XOR gets only done, when poly is 1, else we just return a."""
    if poly:
        return (a + feedback) % 2
    else:
        return a

def list_xor(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists have differing length")
    ret_list = []
    for i in range(len(list1)):
        ret_list.append(poly_xor(list1[i], list2[i], 1))
    return ret_list


registers = [0 for i in range(num_regs)]
takt = 0

output_list = []
for input_number in input_list:
    if takt != 0:
        output_list += registers
    takt += 1
    feedback = registers[0]
    new_registers = [None] * len(registers)
    new_registers[-1] = poly_xor(input_number, feedback, division_polynom[-1])
    for i in range(0, len(division_polynom) - 1):
        new_registers[i] = poly_xor(registers[i+1], feedback, division_polynom[i])

    test_scheme = list_xor(registers, new_registers)
    # print("Prüfschema-Spalte: %s" % "".join([str(i) for i in test_scheme]))
    registers = new_registers

print(output_list.reverse())

output_file_identifier = open("output.tex", "w+")
for i in range(0, len(division_polynom)):
    for k in range(0, len(input_list) - 1):
        index = len(division_polynom) - 1 - i + len(division_polynom)*k
        print(index)
        output_file_identifier.write(str(output_list[index]))
        if k != len(input_list) - 1:
            output_file_identifier.write(" & ")
    if i != len(division_polynom) - 1:
        output_file_identifier.write("\\\\ \n")
output_file_identifier.close()

