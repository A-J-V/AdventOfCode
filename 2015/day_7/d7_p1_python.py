"""
This puzzle is solved with the following strategy:

Use a Gate class that can hold inputs, a function, and an output.
Hold Gate instances in a list.
Consider wires to be key:value pairs.
Hold wires in a dictionary.

1) Read in a line and split it on "->".
2) The right side is the output. It is always a named wire. Add to wire_dict with value None.
3) The left side is input and gates. Gates are always ALLCAPS. Extract ALLCAPS to find gate.
4) Use dictionary to map the extracted gate type to the correct gate function.
5) If gate name is AND, OR, LSHIFT, or RSHIFT, split on " <gate_name> ".
5) If gate name is "NOT", split on "<gate_name> " (notice no space on the left).
5) If no gate name was found (no CAPS), this is a signal-to-wire or wire-to-wire. Don't split.
6) For every component found in 5), check if it is a signal (digit). If not, add to wire_dict w/ value None.
7) Append a new Gate instance to list using gate_type, input components, and output found in 2, 5, and 6.
8) For every gate in the gate list, find the subset of gates with input values that are not None
   (meaning each input is a signal or it's value in wire_dict is not None), but with an output value
   that IS None in the wire_dict. These are the gates that can fire and have not yet fired.
9) Activate every gate found in 8 by passing the inputs through the gate function and updating the
   gate's output wire in the wire_dict.
10) Is the target's value known? If yes, finish and print the target wire's value. If no, go to 8.

"""

# Define wire_dict and gates to hold the data of all wires and all gates.
wire_dict = {}
gates = []

# Read in the instructions.
with open(r'./d7_input.txt', 'r') as f:
    lines = f.read().strip().splitlines()


class Gate:
    """ A Gate. Always contains two inputs, one output, and one gate function. """

    def __init__(self, name, func, components, out):
        self.name = name
        self.func = func
        self.out = out
        self.inc1 = components[0]
        self.inc2 = components[1] if len(components) == 2 else None
        
    def __repr__(self):
        return f"Gate: {self.name}, inc1: {self.inc1}, inc2: {self.inc2}, out: {self.out}."
        
    def prep_incoming(self):
        """ Translate the gate's named inputs to values usable in determining readiness & firing. """
        
        if self.inc1:
            inc1 = int(self.inc1) if self.inc1.isdigit() else wire_dict[self.inc1]
        else:
            inc1 = True
        if self.inc2:
            inc2 = int(self.inc2) if self.inc2.isdigit() else wire_dict[self.inc2]
        else:
            inc2 = True
        
        return inc1, inc2
        
    def ready(self):
        """ Check if the gate can fire but has not yet fired. """
        inc1, inc2 = self.prep_incoming()
            
        if (inc1 != None and inc2 != None) and wire_dict[self.out] == None:
            return True
        else:
            return False
        
    def propagate(self):
        """ Pass gate's inputs through gate's function and update the output in wire_dict. """
        inc1, inc2 = self.prep_incoming()
        out = self.func(inc1, inc2)
        print(f"Updating {self.out} to equal {out}!")
        wire_dict[self.out] = out
        
# Define the gate's operations as lambda functions for convenience
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
        

# Read in the input lines to build all of the gates and initialize all of the wires.
for line in lines:
    # Extract the output first by splitting on ->
    first_split = line.split(" -> ")
    outgoing_wire_name = first_split[1]
    
    # Add this wire's name to the wire dict
    wire_dict[outgoing_wire_name] = None
    
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
        components = input_and_gate.split(gate_string + " ")

    elif gate_string == "":
        # This is either a live wire or wire-to-wire with no gate
        components = [input_and_gate]
    else:
        raise Exception("Gate not recognized!")

    for component in components:
        # If the component is a wire, add it to the wire_dict
        # Don't add raw signals (digits)
        if not component.isdigit():
            wire_dict[component] = None
            
    # Add a gate to the gate list based on the extracted information
    gates.append(Gate(gate_string, gate_type, components, outgoing_wire_name))

# While the target wire 'a' has no signal, loop through all gates and fire the ones that are ready.
while wire_dict['a'] == None:
    ready_gates = []
    for gate in gates:
        if gate.ready():
            ready_gates.append(gate)
            
    for gate in ready_gates:
        print(f"Sending {gate.inc1} and {gate.inc2} through {gate.name} to get {gate.out}")
        gate.propagate()

# All gates have been activated. Print the final value of the target wire. 
print(f"The final value of 'a' is {wire_dict['a']}.")
