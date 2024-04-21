fn get_digit(num: u32, digit: u32) -> u32 {
    println!("get_digit({}, {})", num, digit);
    // get the specified digit from the number left to right
    let digit_char = num.to_string().as_bytes()[digit as usize] as char;
    return digit_char as u32 - '0' as u32;
}

fn d_n(n: u32) -> u32 {
    let mut radix = 0;
    let mut remaining = n;

    while remaining > 9 * 10u32.pow(radix) {
        println!("radix: {}, remaining: {}", radix, remaining);
        remaining -= 9 * 10u32.pow(radix);
        radix += 1;
    }
    println!("radix: {}, remaining: {}", radix, remaining);

    let num_digits = radix + 1;
    let number = 10u32.pow(radix) + remaining / num_digits;

    // digit should be rotated if 0
    let digit = if (remaining % num_digits) == 0 {
        num_digits - 1
    } else {
        (remaining % num_digits) - 1
    };

    return get_digit(number, digit);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_digit() {
        let res = get_digit(12345, 3);
        assert_eq!(res, 4);

        let res = get_digit(948293819, 4);
        assert_eq!(res, 9);
    }

    // TODO: fix
    #[test]
    fn test_dn() {
        let res = d_n(1);
        assert_eq!(res, 1);

        // let res = d_n(12);
        // assert_eq!(res, 1)
    }
}

fn main() {
    println!("Hello, world!");
}
