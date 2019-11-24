// t := 0
// for k = 1 up to k = 500500:
//     t := (615949*t + 797807) modulo 220
//     sk := t−219
use std::collections::HashMap;

fn generate_triangle(size: usize) -> Vec<i64> {
    let mut triangle: Vec<i64> = Vec::new();

    // Lol, not great names
    let base: i64 = 2;
    let high: i64 = base.pow(20);
    let low: i64 = base.pow(19);

    let mut t: i64 = 0;
    for i in 0..size {
        t = ((615949 * t) + 797807) % high;
        triangle.push(t - low);
    }

    triangle
}

// also rows might not be the best name
fn generate_rows(size: usize) -> Vec<u32> {
    let mut rows: Vec<u32> = Vec::new();
    let mut row_num = 0;
    let mut row_counter = 1;
    for i in 0..size {
        rows.push(row_num);

        row_counter -= 1;
        if row_counter == 0 {
            row_num += 1;
            row_counter = row_num + 1;
        }
    }

    rows
}

fn generate_cols(size: usize) -> Vec<u32> {
    let mut cols: Vec<u32> = Vec::new();

    let mut row_size = 1;
    let mut col_idx = 0;
    for i in 0..size {
        cols.push(col_idx);
        col_idx += 1;
        if col_idx == row_size {
            row_size += 1;
            col_idx = 0;
        }
    }

    cols
}

fn generate_row_col_map(rows: &Vec<u32>, cols: &Vec<u32>) -> HashMap<(u32, u32), usize> {
    let mut row_col_map: HashMap<(u32, u32), usize> = HashMap::new();

    for i in 0..rows.len() {
        row_col_map.insert((rows[i], cols[i]), i);
    }

    row_col_map
}

struct Problem {
    triangle: Vec<i64>,
    rows: Vec<u32>,
    cols: Vec<u32>,

    row_col_map: HashMap<(u32, u32), usize>,
}

fn generate_problem(size: usize) -> Problem {
    let triangle = generate_triangle(size);
    let rows = generate_rows(size);
    let cols = generate_cols(size);
    let row_col_map = generate_row_col_map(&rows, &cols);

    Problem {
        triangle,
        rows,
        cols,
        row_col_map,
    }
}

#[cfg(test)]
mod test {
    // Note this useful idiom: importing names from outer (for mod tests) scope.
    use super::*;

    #[test]
    fn test_generate_problem_1() {
        let problem = generate_problem(1);

        assert_eq!(problem.triangle, [273519]);
        assert_eq!(problem.rows, [0]);
        assert_eq!(problem.cols, [0]);
        assert_eq!(problem.row_col_map.get(&(0, 0)).unwrap(), &0);
    }

    #[test]
    fn test_generate_problem_3() {
        let problem = generate_problem(3);

        assert_eq!(problem.triangle, [273519, -153582, 450905]);
        assert_eq!(problem.rows, [0, 1, 1]);
        assert_eq!(problem.cols, [0, 0, 1]);
        assert_eq!(problem.row_col_map.get(&(0, 0)).unwrap(), &0);
        assert_eq!(problem.row_col_map.get(&(1, 0)).unwrap(), &1);
        assert_eq!(problem.row_col_map.get(&(1, 1)).unwrap(), &2);
    }
}

// exactly 1000 rows
struct Solutions {
    map: [[i64; 500500]; 1000],
}

// NOTE: getting references to work here ain't gonna be trivial :/. *That* is the learning I'll gather by solving this
fn find_solution(problem: Problem, solutions: Solutions, i: u16, j: u16) {
    // go find i, j-1 if not already found
    // add P(i, j-1) to appropriate set of things in row j. might require getting column of each item?
    // ya, b/c if we have col(s), then that's also the col to start with in row j!
}

fn find_min_triangle(problem: Problem) -> i64 {
    // iterate through *all* solutions, find them, and keep track of the smallest one
    0
}

// NOTE: it took like no time to generate all the nums. Next, the dp problem to get smallest triangle!
// P(i, j) = sum of triangle rooted at i of side length j
// P(i, j) = P(i, j-1) + row j in triangle
// Total # of problems ~ Billions

// Ohh, stackoverflow is happening b/c I'm allocating these massive arrays on stack. I should probably just be
// allocating them on heap... i.e. vecs
fn main() {
    println!("Hello, world!");
    println!("Done!");
}
