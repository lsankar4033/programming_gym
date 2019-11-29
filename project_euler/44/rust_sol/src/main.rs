fn is_pentagonal(n: u64) -> bool {
    let sr: f64 = (((n * 24) + 1) as f64).sqrt();
    if sr.fract() != 0.0 {
        return false;
    }

    ((sr as u64) + 1) % 6 == 0
}

fn pentagonal(n: u64) -> u64 {
    (n * (3 * n - 1) / 2)
}

struct PairAcc {
    last_n: u64,
    pents: Vec<u64>,
    best_pair: Option<(u64, u64)>,
}
impl PairAcc {
    fn inc(&mut self) {
        let next_pent = pentagonal(self.last_n + 1);
        for pent in self.pents.iter() {
            let sum = *pent + next_pent;
            let diff = next_pent - *pent;

            if is_pentagonal(sum) && is_pentagonal(diff) {
                match self.best_pair {
                    Some((i, j)) => {
                        let old_diff = j - i;

                        if diff < old_diff {
                            self.best_pair = Some((*pent, next_pent))
                        }
                    }

                    None => self.best_pair = Some((*pent, next_pent)),
                }
            }
        }

        self.last_n += 1;
        self.pents.push(next_pent);
    }

    fn finished(&self) -> bool {
        if self.pents.len() < 2 {
            return false;
        }

        let last = self.pents[self.pents.len() - 1];
        let second_last = self.pents[self.pents.len() - 2];
        match self.best_pair {
            None => false,
            Some((i, j)) => j - i <= last - second_last,
        }
    }
}

fn find_closest_pentagonal_pair() -> (u64, u64) {
    let mut acc = PairAcc {
        last_n: 0,
        pents: vec![],
        best_pair: None,
    };
    loop {
        acc.inc();

        if acc.last_n % 10000 == 0 {
            println!("Last n: {}", acc.last_n);
        }

        if acc.finished() {
            break;
        }
    }

    acc.best_pair.unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_pentagonal() {
        assert!(is_pentagonal(1));
        assert!(!is_pentagonal(2));
        assert!(!is_pentagonal(3));
        assert!(!is_pentagonal(4));
        assert!(is_pentagonal(5));
        assert!(!is_pentagonal(6));
        assert!(!is_pentagonal(7));
        assert!(!is_pentagonal(8));
        assert!(!is_pentagonal(9));
        assert!(!is_pentagonal(10));
        assert!(!is_pentagonal(11));
        assert!(is_pentagonal(12));
        assert!(is_pentagonal(22));
        assert!(is_pentagonal(35));
    }
}

fn main() {
    println!("starting");
    let best_pair = find_closest_pentagonal_pair();
    println!("{} {}", best_pair.0, best_pair.1);
}
