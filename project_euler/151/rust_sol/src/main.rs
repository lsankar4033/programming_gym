use std::collections::HashMap;
use std::collections::HashSet;

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
    for _ in 0..size {
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

fn generate_row_sums(
    triangle: &Vec<i64>,
    row_col_map: &HashMap<(u32, u32), usize>,
    num_rows: u32,
) -> HashMap<(u32, u32), i64> {
    let mut row_sums: HashMap<(u32, u32), i64> = HashMap::new();

    for row in 0..num_rows {
        let mut row_sum = 0;
        for col in 0..(row + 1) {
            let i = row_col_map.get(&(row, col)).unwrap();
            row_sum += triangle[*i];
            row_sums.insert((row, col), row_sum as i64);
        }
    }

    row_sums
}

// NOTE: we can probably just have a row_col_val map instead of triangle, rows, cols
struct Problem {
    triangle: Vec<i64>,
    rows: Vec<u32>,
    cols: Vec<u32>,

    row_sums: HashMap<(u32, u32), i64>,
}
impl Problem {
    fn size(&self) -> usize {
        self.triangle.len()
    }

    fn num_rows(&self) -> usize {
        let mut unique_rows: HashSet<u32> = HashSet::new();
        for i in 0..self.rows.len() {
            unique_rows.insert(self.rows[i]);
        }
        unique_rows.len()
    }
}

fn generate_problem(size: usize) -> Problem {
    let triangle = generate_triangle(size);
    let rows = generate_rows(size);

    // NOTE: duplicated code...
    let mut unique_rows: HashSet<u32> = HashSet::new();
    for i in 0..rows.len() {
        unique_rows.insert(rows[i]);
    }
    let num_rows = unique_rows.len();

    let cols = generate_cols(size);
    let row_col_map = generate_row_col_map(&rows, &cols);
    let row_sums = generate_row_sums(&triangle, &row_col_map, num_rows as u32);

    Problem {
        triangle,
        rows,
        cols,
        row_sums,
    }
}

struct Solutions {
    map: HashMap<(usize, usize), i64>,
}

fn find_solution(problem: &Problem, solutions: &mut Solutions, i: usize, j: usize) -> i64 {
    match solutions.map.get(&(i, j)) {
        Some(solution) => {
            return *solution;
        }

        None => {
            let sol = if j == 0 {
                problem.triangle[i]
            } else {
                let prev_solution: i64 = find_solution(problem, solutions, i, j - 1);

                // NOTE: is there a way to avoid this casting?
                let start_col = problem.cols[i];
                let ju32 = j as u32;
                let row = problem.rows[i] + ju32;

                let row_sum = if start_col == 0 {
                    *problem
                        .row_sums
                        .get(&(row, start_col + (j as u32)))
                        .unwrap()
                } else {
                    let full_row = problem
                        .row_sums
                        .get(&(row, start_col + (j as u32)))
                        .unwrap();
                    full_row - problem.row_sums.get(&(row, start_col - 1)).unwrap()
                };
                prev_solution + row_sum
            };

            solutions.map.insert((i, j), sol);

            sol
        }
    }
}

fn find_min_triangle(problem: Problem) -> i64 {
    // iterate through *all* solutions, find them, and keep track of the smallest one
    let map: HashMap<(usize, usize), i64> = HashMap::new();
    let mut solutions = Solutions { map };

    let mut min_solution = std::i64::MAX;
    let num_rows = problem.num_rows();
    for i in 0..problem.size() {
        println!("Solving problems rooted at {}", i);
        let start_row = problem.rows[i] as usize;
        for j in 0..(num_rows - start_row) {
            let solution = find_solution(&problem, &mut solutions, i, j);
            solutions.map.insert((i, j), solution);
            if solution < min_solution {
                min_solution = solution;
            }
        }
    }

    min_solution
}

#[cfg(test)]
mod test {
    // Note this useful idiom: importing names from outer (for mod tests) scope.
    use super::*;

    #[test]
    fn test_generate_problem_1() {
        let problem = generate_problem(1);

        assert_eq!(problem.size(), 1);
        assert_eq!(problem.num_rows(), 1);
        assert_eq!(problem.triangle, [273519]);
        assert_eq!(problem.rows, [0]);
        assert_eq!(problem.cols, [0]);
        assert_eq!(problem.row_sums.get(&(0, 0)).unwrap(), &273519);
    }

    #[test]
    fn test_generate_problem_3() {
        let problem = generate_problem(3);

        assert_eq!(problem.size(), 3);
        assert_eq!(problem.num_rows(), 2);
        assert_eq!(problem.triangle, [273519, -153582, 450905]);
        assert_eq!(problem.rows, [0, 1, 1]);
        assert_eq!(problem.cols, [0, 0, 1]);
        assert_eq!(problem.row_sums.get(&(0, 0)).unwrap(), &273519);
        assert_eq!(problem.row_sums.get(&(1, 0)).unwrap(), &-153582);
        assert_eq!(problem.row_sums.get(&(1, 1)).unwrap(), &297323);
    }

    #[test]
    fn test_find_solution_3() {
        let problem = generate_problem(3);

        let map: HashMap<(usize, usize), i64> = HashMap::new();
        let mut solutions = Solutions { map };
        let sol = find_solution(&problem, &mut solutions, 0, 1);
        assert_eq!(sol, 570842)
    }

    #[test]
    fn test_find_solution_10() {
        let problem = generate_problem(10);

        let map: HashMap<(usize, usize), i64> = HashMap::new();
        let mut solutions = Solutions { map };
        let sol = find_solution(&problem, &mut solutions, 1, 2);
        assert_eq!(sol, 130773);

        let sol2 = find_solution(&problem, &mut solutions, 0, 3);
        assert_eq!(sol2, 1099837);
    }

    #[test]
    fn test_find_min_triangle_3() {
        let problem = generate_problem(3);
        let min = find_min_triangle(problem);
        assert_eq!(min, -153582);
    }

    #[test]
    fn test_find_min_triangle_10() {
        let problem = generate_problem(10);
        let min = find_min_triangle(problem);
        assert_eq!(min, -488152);
    }
}

fn main() {
    println!("Running...");
    let problem = generate_problem(500500);
    println!("Generated problem");
    let sol = find_min_triangle(problem);
    println!("{}", sol)
}
