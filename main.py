# --- change this
# Prüfmatrix bestimmen
# input_list = [1 for i in range(0, 16)]
# Prüfmatrix besser bestimmen
input_list = [1] + [0 for i in range(1, 16)]
# aufgabe 4.1.2 nutzwort
# input_list = [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]
# aufgabe 4.1.4 Codewort original
# input_list = [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0]
# aufgabe 4.1.4 Codewort korrigiert
# input_list = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0]
# Aufgabe 4.2.2. Nutzwort
# input_list = [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]
# Aufgabe 4.2.4 Test
# input_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0]

# Test Input
# input_list = [1, 1, 0, 1, 1, 1, 0, 0]
# input_list = [1 for i in range(0, 8)]

# polynom Aufgabe 8.5 (nicht primitiv)
division_polynom = [1, 1, 1, 0, 0]

# polynom Aufgabe 4.1
# division_polynom = [1, 0, 1, 0, 1]

# polynom Aufgabe 4.2
# division_polynom = [1, 0, 0, 1]

# polynom Test
#division_polynom = [0, 1, 1]

num_regs = len(division_polynom)
# change till here

def poly_xor(a, feedback, poly):
    """Accepts two numbers to xor. a is the value of the last register. Feedback comes from the the division
    XOR gets only done, when poly is 1, else we just return a."""
    if poly:
        return (a + feedback) % 2
    else:
        return a

# -------------------------------------------

def list_xor(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists have differing length")
    ret_list = []
    for i in range(len(list1)):
        ret_list.append(poly_xor(list1[i], list2[i], 1))
    return ret_list

registers = [0 for i in range(num_regs)]
takt = 0
for input_number in input_list:
    print(str(takt) + " " + str(registers) + " " + str(input_number))
    takt += 1
    feedback = registers[0]
    new_registers = [None] * len(registers)
    new_registers[-1] = poly_xor(input_number, feedback, division_polynom[-1])
    for i in range(0, len(division_polynom) - 1):
        new_registers[i] = poly_xor(registers[i+1], feedback, division_polynom[i])

    test_scheme = list_xor(registers, new_registers)
    # print("Prüfschema-Spalte: %s" % "".join([str(i) for i in test_scheme]))
    registers = new_registers

