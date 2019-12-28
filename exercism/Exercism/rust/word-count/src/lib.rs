use std::collections::HashMap;

/// Count occurrences of words.
pub fn word_count(words: &str) -> HashMap<String, u32> {
    let mut word_map: HashMap<String, u32> = HashMap::new();
    for word in words
        .to_lowercase()
        .split(|c: char| !c.is_alphanumeric() && c != '\'')
        .filter(|w| !w.is_empty())
        .map(|w| w.trim_matches('\''))
    {
        *word_map.entry(word.to_owned()).or_insert(0u32) += 1u32;
    }

    word_map
}
