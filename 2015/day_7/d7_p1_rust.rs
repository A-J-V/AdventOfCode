use std::collections::HashMap;
use std::fs;

// Define some helper functions for the gate operations
fn and(inc1: i32, inc2: i32) -> i32 {
    inc1 & inc2
}
fn or(inc1: i32, inc2: i32) -> i32 {
    inc1 | inc2
}
fn lshift(inc1: i32, inc2: i32) -> i32 {
    inc1 << inc2
}
fn rshift(inc1: i32, inc2: i32) -> i32 {
    inc1 >> inc2
}
fn not(_: i32, inc2: i32) -> i32 {
    !inc2
}
fn identity(inc1: i32, _: i32) -> i32 {
    inc1
}

/// Holds all of the information about a wire.
#[derive(Debug)]
struct Components {
    gate: fn(i32, i32) -> i32,
    inp1: String,
    inp2: String,
    value: String,
}

/// Helper function that maps a gate name from the instructions to a gate function
fn get_gate(name: &str) -> fn(i32, i32) -> i32 {
    match name {
        "AND" => return and,
        "OR" => return or,
        "LSHIFT" => return lshift,
        "RSHIFT" => return rshift,
        "NOT" => return not,
        "" => return identity,
        _ => return identity,
    }
}

/// Recursively determines the signal of a wire
fn get_signal(target: &str, circuit_dict: &mut HashMap<&str, Components>) -> i32 {
    if target.chars().all(|i| i.is_ascii_digit()) {
        return target.parse::<i32>().unwrap();
    } else if circuit_dict
        .get(target)
        .unwrap()
        .value
        .chars()
        .all(|i| i.is_ascii_digit())
    {
        return circuit_dict
            .get(target)
            .unwrap()
            .value
            .parse::<i32>()
            .unwrap();
    } else {
        let func = circuit_dict.get(target).unwrap().gate;
        let inp1 = circuit_dict.get(target).unwrap().inp1.clone();
        let inp2 = circuit_dict.get(target).unwrap().inp2.clone();
        let inp1_sig = get_signal(inp1.as_str(), circuit_dict);
        let inp2_sig = get_signal(inp2.as_str(), circuit_dict);
        let value = func(inp1_sig, inp2_sig);
        circuit_dict.get_mut(target).unwrap().value = value.to_string();
        return value;
    }
}

fn main() {
    let mut circuit_dict = HashMap::new();
    let inputs = fs::read_to_string("./d7_input.txt").expect("Should have been able to read line.");

    inputs.as_str().trim().lines().for_each(|line| {
        // Split on -> to separate input & gate on left, output on right
        let first_split = line.split(" -> ").collect::<Vec<&str>>();
        // Get the output wire name
        let outgoing_wire_name = first_split[1];
        // Get the input and gate
        let input_and_gate = first_split[0];
        // Extract the name of the gate
        let gate_read = input_and_gate
            .chars()
            .filter(|i| i.is_uppercase())
            .collect::<String>();
        let gate_name = gate_read.as_str();
        // Extract signals, wires, or number of shifts
        let components;
        match gate_name {
            "AND" | "OR" | "LSHIFT" | "RSHIFT" => {
                let splits = input_and_gate.split(gate_name).collect::<Vec<&str>>();

                components = Components {
                    gate: get_gate(gate_name),
                    inp1: splits[0].to_string().trim().to_string(),
                    inp2: splits[1].to_string().trim().to_string(),
                    value: "None".to_string(),
                }
            }

            "NOT" => {
                let splits = input_and_gate.split(gate_name).collect::<Vec<&str>>();

                components = Components {
                    gate: not,
                    inp1: String::from("0"),
                    inp2: splits[1].to_string().trim().to_string(),
                    value: "None".to_string(),
                }
            }

            "" => {
                components = Components {
                    gate: identity,
                    inp1: input_and_gate.to_string(),
                    inp2: String::from("0"),
                    value: "None".to_string(),
                }
            }

            _ => {
                components = Components {
                    gate: and,
                    inp1: "butt!".to_string(),
                    inp2: "butt!".to_string(),
                    value: "None".to_string(),
                }
            }
        }
        circuit_dict.insert(outgoing_wire_name, components);
    });
    let target_value = get_signal("a", &mut circuit_dict);
    println!("The final value of 'a' is {target_value}.");
}
