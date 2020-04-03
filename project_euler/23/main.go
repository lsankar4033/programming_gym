package main

import (
	"fmt"
)

func isAbundant(n int) bool {
	maxDiv := n / 2

	sum := 0
	for i := 1; i <= maxDiv; i++ {
		if n%i == 0 {
			sum += i
		}
	}

	return sum > n
}

// NOTE: sorted
func getAbundants() []int {
	var abundants []int

	for i := 12; i <= 28123; i++ {
		if isAbundant(i) {
			abundants = append(abundants, i)
		}
	}

	return abundants
}

//func isAbundantSum(n int, abundants []int) bool {

//}

func main() {
	fmt.Println("Getting abundants")
	abundants := getAbundants()
	fmt.Printf("len(abundants) = %+v\n", len(abundants))

	fmt.Println("Seeding non-abundant sums map")
	nonAbundantSums := map[int]bool{}
	for i := 1; i <= 28123; i++ {
		nonAbundantSums[i] = true
	}

	fmt.Println("Removing all combinations of abundants")
	for i := 0; i < len(abundants); i++ {
		for j := i; j < len(abundants); j++ {
			sum := abundants[i] + abundants[j]

			_, ok := nonAbundantSums[sum]
			if ok {
				delete(nonAbundantSums, sum)
			}
		}
	}
	fmt.Printf("len(nonAbundantSums) = %+v\n", len(nonAbundantSums))

	total := 0
	for n, _ := range nonAbundantSums {
		total += n
	}
	fmt.Printf("total = %+v\n", total)
}
