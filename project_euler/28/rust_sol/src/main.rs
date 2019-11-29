struct DiagonalIterator {
    interval: u32,
    num_remaining_at_interval: u32,
    last: u32,
}
impl DiagonalIterator {
    fn new() -> DiagonalIterator {
        DiagonalIterator {
            interval: 0,
            num_remaining_at_interval: 1,
            last: 1,
        }
    }
}
impl Iterator for DiagonalIterator {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        if self.num_remaining_at_interval == 0 {
            self.interval += 2;
            self.num_remaining_at_interval = 4;
        }

        self.num_remaining_at_interval -= 1;
        self.last += self.interval;
        Some(self.last)
    }
}

fn diagonal_sum(side_len: u32) -> u32 {
    let num_diagonals = ((side_len - 1) / 2) * 4 + 1;
    let diagonal_iter = DiagonalIterator::new();
    diagonal_iter.take(num_diagonals as usize).sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_diagonal_iterator() {
        let iter = DiagonalIterator::new();
        let first_nine: Vec<u32> = iter.take(9).collect();
        assert_eq!(first_nine, [1, 3, 5, 7, 9, 13, 17, 21, 25]);
    }

    #[test]
    fn test_diagonal_sum() {
        assert_eq!(diagonal_sum(1), 1);
        assert_eq!(diagonal_sum(3), 25);
        assert_eq!(diagonal_sum(5), 101);
    }
}

// num diagonals: 500*4 + 1 = 2001
fn main() {
    let sum = diagonal_sum(1001);
    println!("{}", sum);
}
