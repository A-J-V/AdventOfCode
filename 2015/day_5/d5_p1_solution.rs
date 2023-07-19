use std::fs;

const VOWELS: &str = "aeiou";
const NAUGHTIES: [[char; 2]; 4] = [['a', 'b'],
                                   ['c', 'd'],
                                   ['p', 'q'],
                                   ['x', 'y']];

fn is_vowel(c: char) -> bool {

    return VOWELS.contains(c)
    
}

fn three_vowels(s: &str) -> bool {
   
    let mut num_vowels = 0;
    for c in s.to_lowercase().chars() {
        if is_vowel(c) {num_vowels += 1}
    }
    num_vowels >= 3
   
}

fn has_double(s: &str) -> bool {
    s.chars()
     .collect::<Vec<char>>()
     .windows(2)
     .any(|w| w[0] == w[1])
}

fn has_naughty(s: &str) -> bool {
    s.to_lowercase()
     .chars()
     .collect::<Vec<char>>()
     .windows(2)
     .any(|i| NAUGHTIES.contains(&[i[0], i[1]]))
}

fn main() {

    let mut nice_strings = 0;
    fs::read_to_string("./d5_input.txt")
        .expect("Should have been able to read line.")
        .as_str()
        .lines()
        .for_each(|i| {
            if three_vowels(&i) & has_double(&i) & !has_naughty(&i) { nice_strings += 1}
        });
    println!("There are {} nice strings.", nice_strings);
}
