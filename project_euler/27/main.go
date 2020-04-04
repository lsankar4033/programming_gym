package main

import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	for i := 2; i <= int(math.Floor(float64(n)/2)); i++ {
		if n%i == 0 {
			return false
		}
	}

	return n > 1
}

func quad(x int, a int, b int) int {
	return (x * x) + (a * x) + b
}

func getStreak(a int, b int, primes map[int]bool, comps map[int]bool) int {
	x := -1
	for {
		x++

		q := quad(x, a, b)

		if _, ok := comps[q]; ok == true {
			break
		}

		if _, ok := primes[q]; ok == true {
			continue
		}

		if isPrime(q) {
			primes[q] = true
		} else {
			comps[q] = true
			break
		}
	}

	return x
}

func main() {
	primes := map[int]bool{}
	comps := map[int]bool{}

	bestStreak := 0
	bestProd := 0

	for a := -999; a < 1000; a++ {
		for b := -1000; b < 1001; b++ {
			streak := getStreak(a, b, primes, comps)

			if streak > bestStreak {
				bestStreak = streak
				bestProd = a * b

				fmt.Printf("bestStreak = %+v\n", bestStreak)
				fmt.Printf("bestProd = %+v\n", bestProd)
			}
		}
	}

	fmt.Println("Done!")
}
