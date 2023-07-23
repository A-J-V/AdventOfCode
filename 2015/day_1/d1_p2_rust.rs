use std::fs;

fn main() {

    let mut floor = 0;
    let mut pos = 0;

    let input_vec = fs::read_to_string("./d1_input.txt")
    .expect("Failed to read input.")
    .as_str()
    .chars()
    .collect::<Vec<char>>();

    for i in input_vec {
        pos += 1;
        if i == '(' {
            floor += 1;
        } else if i == ')' {
            floor -= 1;
        }
        
        if floor == -1 {
            let solution = pos;
            println!("Mr. Claus first entered the basement at position {}.",
                     solution);
            break;
        }
    }
}
