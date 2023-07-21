use std::fs;


fn flanked(s: &str) -> bool {
    s.chars()
     .collect::<Vec<char>>()
     .windows(3)
     .any(|w| w[0] == w[2])
}


fn has_duplicate_pair(s: &str) -> bool {
    let char_vec = s.to_lowercase()
                    .chars()
                    .collect::<Vec<char>>();
                    
    for i in 0..char_vec.len()-1 {
        let mut left_ref = char_vec[..i].windows(2);
        let mut right_ref = char_vec[i+2..].windows(2);
        let pair = &char_vec[i..i+2];
        if left_ref.any(|w| w == pair) || right_ref.any(|w| w == pair) {
            return true
        }
    }
    false
}


fn main() {

    let mut nice_strings = 0;
    fs::read_to_string("./d5_input.txt")
        .expect("Expected to be able to read line.")
        .as_str()
        .lines()
        .for_each(|i| {
            if has_duplicate_pair(i) && flanked(i) { nice_strings += 1}
        });
    println!("There are {} nice strings.", nice_strings);
}
