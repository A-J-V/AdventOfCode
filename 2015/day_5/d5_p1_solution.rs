use std::fs;

const VOWELS: &str = "aeiou"

fn is_vowel(c: &char) -> bool {

    return VOWELS.contains(c.to_lowercase())
    
}

fn three_vowels(s: &str) -> bool {
   
    let mut num_vowels = 0;
    for c in s.to_lowercase().chars() {
        if is_vowel(c) {num_vowels += 1}
    }
    num_vowels >= 3
   
}

fn has_double(s: &str) -> bool {

    for i, c in enumerate(s[:-1]):
        if c == s[i+1]:
            return True
    return False
    
}

fn main() {

    let mut nice_strings = 0;
    fs::read_to_string("./d5_input.txt")
        .expect("Should have been able to read line.")
        .as_str()
        .lines()
        .for_each(|i| {
            paper += paper_calc(i)
        });
    println!("The elves need {} sqft of wrapping paper.", paper);
}
