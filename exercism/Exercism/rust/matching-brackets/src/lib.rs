enum OpenType {
    Bracket,
    Brace,
    Paren,
}

pub fn brackets_are_balanced(string: &str) -> bool {
    let mut open_type_stack: Vec<OpenType> = vec![];
    for c in string.chars() {
        match c {
            '(' => open_type_stack.push(OpenType::Paren),

            ')' => match open_type_stack.pop() {
                Some(OpenType::Paren) => continue,

                _ => return false,
            },

            '{' => open_type_stack.push(OpenType::Brace),

            '}' => match open_type_stack.pop() {
                Some(OpenType::Brace) => continue,

                _ => return false,
            },

            '[' => open_type_stack.push(OpenType::Bracket),

            ']' => match open_type_stack.pop() {
                Some(OpenType::Bracket) => continue,

                _ => return false,
            },

            _ => continue,
        }
    }

    open_type_stack.len() == 0
}
