pub fn is_armstrong_number(num: u32) -> bool {
    let as_str: String = num.to_string();
    let num_digits: usize = as_str.len();

    num == as_str
        .chars()
        .map(|c| c.to_digit(10).unwrap().pow(num_digits as u32))
        .sum()
}
