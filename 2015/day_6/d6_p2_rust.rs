use std::fs;

/// Toggle treats the incoming array as a wrapped array
/// and toggles the elements between (x1, y1) and (x2, y2)
/// according to the instruction

const DIM: usize = 1000;

fn toggle(x1: i32,
          y1: i32,
          x2: i32,
          y2: i32,
          light_array: &mut[i32],
          instruction: &str) -> () {
    
    // This is incredible inefficient, as it changes the elements
    // one at a time.
    for y in y1..y2+1 {
        for x in x1..x2+1 {
            match instruction {
                "on " => {light_array[DIM * y as usize + x as usize] += 1},
                "off " => {
                    if light_array[DIM * y as usize + x as usize] > 0 {
                        light_array[DIM * y as usize + x as usize] -= 1
                    }
                },
                "toggle " => {light_array[DIM * y as usize + x as usize] += 2},
                _ => (),
            }
        }
    }
}

fn main() {
    
    // -1 means off, 1 means on. This coding makes toggling on/off
    // as easy as multiplying by -1.
    let mut light_array = [0; DIM*DIM];
    
    fs::read_to_string("./d6_input.txt")
    .expect("Should have been able to read line.")
    .as_str()
    .trim()
    .lines()
    .for_each(|line| {
        // Find the light instruction
        let mut instruction = "placeholder";
        if line.contains("off") {instruction = "off "}
        else if line.contains("on") {instruction = "on "}
        else if line.contains("toggle") {instruction = "toggle "}
        else {println!("Invalid instruction found!")}
        
        // Use basic &str methods to extract the two coordinates
        let line2 = line.split(instruction).collect::<Vec<&str>>()[1];
        let coords = line2.split(" through ").collect::<Vec<&str>>();
        let left = coords[0];
        let right = coords[1];
        let left = left.split(",").collect::<Vec<&str>>();
        let right = right.split(",").collect::<Vec<&str>>();
        let x1 = left[0].parse::<i32>().unwrap();
        let y1 = left[1].parse::<i32>().unwrap();
        let x2 = right[0].parse::<i32>().unwrap();
        let y2 = right[1].parse::<i32>().unwrap();
        
        // Call the toggle function to update the light_array
        // according to the coordinates and instruction
        toggle(x1, y1, x2, y2, &mut light_array, instruction);
    });

    // Finally, sum up the number of elements that == 1 and print it
    let on_lights: i32 = light_array.iter().sum();
    println!("The total brightness is {}!", on_lights);
    
}
