"""
This is a more efficient solution.

The strategy below is to create a dictionary that maps every wire to it's input values and input gate.
We can then directly evaluate any target wire by passing it to a recursive function.
The recursive function has the following flow:
Is the target a digit? If so, return it.
Is the target a wire with a known value? If so, return that value.
Otherwise, evaluate the target's inputs by recursively passing each to this function.
Evaluate the target by passing its inputs through its gate. Update the circuit_dict with this value & return it.

"""

# Define circuit_dict to hold all of the information about each
circuit_dict = {}

# Read in the instructions.
with open(r'./d7_input.txt', 'r') as f:
    lines = f.read().strip().splitlines()
        
# Define the gate operations as lambda functions for convenience
AND = lambda inc1, inc2: inc1 & inc2
OR = lambda inc1, inc2: inc1 | inc2
LSHIFT = lambda inc1, inc2: inc1 << inc2
RSHIFT = lambda inc1, inc2: inc1 >> inc2
NOT = lambda inc1, inc2: 65536 + ~inc2
IDENTITY = lambda inc1, inc2: inc1


# Use dictionary to map gate name to gate function
gate_dict = {'AND': AND,
             'OR': OR,
             'LSHIFT': LSHIFT,
             'RSHIFT': RSHIFT,
             'NOT': NOT,
             '': IDENTITY
            }
        

# Read in the input lines to determine the inputs and gate of each wire
for line in lines:
    # Extract the output first by splitting on ->
    first_split = line.split(" -> ")
    outgoing_wire_name = first_split[1]
    
    # Get the input and gate
    input_and_gate = first_split[0]
    
    # Extract the gate string and get the correct gate type
    # Exploiting the fact that logic gates are in ALLCAPS
    # but wires are lowercase or integer signals
    gate_string = ''.join([i for i in input_and_gate if i.isupper()])
    gate_type = gate_dict[gate_string]
    
    # Extract signal(s), wire(s) or number of shifts
    if gate_string in ['AND', 'OR', 'LSHIFT', 'RSHIFT']:
        components = input_and_gate.split(" " + gate_string + " ")

    elif gate_string == "NOT":
        components = ["0", input_and_gate.split(gate_string + " ")[1]]

    elif gate_string == "":
        # This is either a live wire or wire-to-wire with no gate
        components = [input_and_gate, "0"]
    else:
        raise Exception("Gate not recognized!")

    # Add the outgoing wire as a key in the circuit dict, with a dict of values for input and gate
    circuit_dict[outgoing_wire_name] = {"gate_name": gate_string,
                                        "gate": gate_type,
                                        "inp1": components[0],
                                        "inp2": components[1],
                                        "value": None
                                        }

def get_signal(target):
    # If the target is a digit, it is either a signal or a shift. Return it as int immediately.
    if target.isdigit():
        return int(target)
        
    # If the value is already known, return it immediately
    elif circuit_dict[target]["value"]:
        return circuit_dict[target]["value"]
        
    # If the value is unknown, calculate it by passing its inputs through its gate.
    # If its inputs are unknown, find them by recursively calling this function
    else:
        func = circuit_dict[target]["gate"]
        inp1 = circuit_dict[target]["inp1"]
        inp2 = circuit_dict[target]["inp2"]
        value = func(get_signal(inp1), get_signal(inp2))
        circuit_dict[target]["value"] = value
        return value
        
target = get_signal("a")
print(f"The final value of 'a' is {target}.")
