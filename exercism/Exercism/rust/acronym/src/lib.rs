pub fn abbreviate(phrase: &str) -> String {
    phrase
        .split(|c: char| c == ' ' || c == '-')
        .map(|w| {
            w.chars().filter(|c| c.is_ascii_alphabetic())
        })
        .flat_map(|cs| {
            let mut cs_clone = cs.clone();
            if cs_clone.all(|c| c.is_ascii_uppercase()) || cs_clone.all(|c| c.is_ascii_lowercase())
            {
                cs.take(1).collect::<Vec<char>>()
            } else {
                cs.filter(|c| c.is_ascii_uppercase()).collect::<Vec<char>>()
            }
        })
        .map(|c| c.to_ascii_uppercase())
        .collect()
}
