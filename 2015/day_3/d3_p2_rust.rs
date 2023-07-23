use std::fs;
use std::collections::HashSet;

fn main() {
    // Use a set and add visited houses. We don't care how many times they're visited.
    // Set will ensure we only add unique houses.   
    let mut visited = HashSet::new();
    
    // Initiate starting location and add it to the visited list.
    let mut sx = 0;
    let mut sy = 0;
    let mut rx = 0;
    let mut ry = 0;
    visited.insert((0, 0));
    
    // Define a variable used to decide whether instruction goes to santa or robo
    let mut i = 0;
    
    // For every token in the puzzle input, move x, y coords and add location to set
    fs::read_to_string("./d3_input.txt")
              .expect("Should have read input.")
              .as_str()
              .chars()
              .collect::<Vec<char>>()
              .iter()
              .for_each(|token| {
                  
                  let (x, y) = if i % 2 == 0 {
                      let x = &mut sx;
                      let y = &mut sy;
                      (x, y)
                  } else {
                      let x = &mut rx;
                      let y = &mut ry;
                      (x, y)
                  };
                  match token {
                      '^' => *y -= 1,
                      'v' => *y += 1,
                      '<' => *x -= 1,
                      '>' => *x += 1,
                      _ => ()
                  }
              visited.insert((*x, *y));
              i += 1;
              });
    
    println!("Santa has visited {} houses.", visited.len())
}
