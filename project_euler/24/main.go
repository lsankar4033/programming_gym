package main

import "fmt"

func factorial(n int) int {
	if n == 0 {
		return 1
	}

	return n * factorial(n-1)
}

func main() {
	remainingDigits := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	permDigits := []int{}

	remainingPerms := 1000000
	for {
		fmt.Printf("permDigits so far = %+v\n", permDigits)

		if len(remainingDigits) == 1 {
			permDigits = append(permDigits, remainingDigits[0])
			break
		}

		increment := factorial(len(remainingDigits) - 1)
		for i := 0; i < len(remainingDigits); i++ {
			if remainingPerms <= increment {
				permDigits = append(permDigits, remainingDigits[i])
				remainingDigits = append(remainingDigits[0:i], remainingDigits[i+1:]...)
				break
			}

			remainingPerms -= increment
		}
	}

	fmt.Printf("permDigits = %+v\n", permDigits)
}
