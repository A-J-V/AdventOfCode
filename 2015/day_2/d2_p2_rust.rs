use std::fs;
use std::cmp;

fn ribbon_calc(dimensions: &str) -> i32 {
    let mut dims = Vec::new();
    
    dimensions.split("x")
    .for_each(|i| dims.push(i.parse::<i32>().unwrap()));
    
    let p1 = 2 * (dims[0] + dims[1]);
    let p2 = 2 * (dims[1] + dims[2]);
    let p3 = 2 * (dims[2] + dims[0]);
    
    let bow = dims[0] * dims[1] * dims[2];
    let wrapping = cmp::min(cmp::min(p1, p2), p3);
    wrapping + bow
}
fn main() {

    let mut ribbon = 0;
    fs::read_to_string("./d2_input.txt")
        .expect("Should have been able to read line.")
        .as_str()
        .lines()
        .for_each(|i| {
            ribbon += ribbon_calc(i)
        });
    println!("The elves need {} feet of ribbon.", ribbon);
}
