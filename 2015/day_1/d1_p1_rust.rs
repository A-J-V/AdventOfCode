use std::fs;

fn main() {
    // Initiate the journey of Kringle on the [European] ground floor.
    let mut floor = 0;

    // We don't even need to store what we read, just update the floor
    // on the fly based on contents of the input string.
    fs::read_to_string("./d1_input.txt")
        .expect("Should have been able to read the file.")
        .as_str()
        .chars()
        .collect::<Vec<char>>()
        .iter()
        .for_each(|i| if *i == '(' {
            floor += 1
        } else if *i == ')' {
            floor -= 1
        }
        );
    println!("Mr. Claus must go to floor {}.", floor);
}
