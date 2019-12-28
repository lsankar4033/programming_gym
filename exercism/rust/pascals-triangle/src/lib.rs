pub struct PascalsTriangle {
    rows: Vec<Vec<u32>>,
}

impl PascalsTriangle {
    pub fn new(row_count: u32) -> Self {
        unimplemented!("create Pascal's triangle with {} rows", row_count);
    }

    pub fn rows(&self) -> Vec<Vec<u32>> {
        self.rows
    }
}
