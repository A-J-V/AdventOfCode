use std::fs;
use std::cmp;

fn paper_calc(dimensions: &str) -> i32 {
    let mut dims = Vec::new();
    
    dimensions.split("x")
    .for_each(|i| dims.push(i.parse::<i32>().unwrap()));
    
    let s1 = dims[0] * dims[1];
    let s2 = dims[1] * dims[2];
    let s3 = dims[2] * dims[0];
    
    let surface = (2 * s1) + (2 * s2) + (2 * s3);
    let slack = cmp::min(cmp::min(s1, s2), s3);
    surface + slack
}
fn main() {

    let mut paper = 0;
    fs::read_to_string("./d2_input.txt")
        .expect("Should have been able to read line.")
        .as_str()
        .lines()
        .for_each(|i| {
            paper += paper_calc(i)
        });
    println!("The elves need {} sqft of wrapping paper.", paper);
}
