pub struct PascalsTriangle {
    rows: Vec<Vec<u32>>,
}

impl PascalsTriangle {
    pub fn new(row_count: u32) -> Self {
        let mut rows: Vec<Vec<u32>> = vec![];

        for i in 0..row_count {
            match i {
                0 => rows.push(vec![1]),

                _ => {
                    let last_row: &Vec<u32> = rows.last().unwrap();

                    let mut next_row: Vec<u32> = vec![1];
                    for i in 0..(last_row.len() - 1) {
                        next_row.push(last_row[i] + last_row[i + 1]);
                    }
                    next_row.push(1);

                    rows.push(next_row);
                }
            }
        }

        PascalsTriangle { rows }
    }

    pub fn rows(&self) -> Vec<Vec<u32>> {
        self.rows.clone()
    }
}
