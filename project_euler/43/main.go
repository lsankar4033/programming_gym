package main

import (
	"fmt"
	"strconv"
	"strings"
)

func allDigits() map[int]bool {
	digits := map[int]bool{}
	for i := 0; i < 10; i++ {
		digits[i] = true
	}

	return digits
}

func strToDigits(s string) map[int]bool {
	digits := map[int]bool{}
	for _, r := range s {
		digits[int(r-'0')] = true
	}

	return digits
}

func recursiveGenerate(stepsRemaining uint, allDigits map[int]bool, existing map[string]bool) map[string]bool {
	if stepsRemaining < 1 {
		return existing
	}

	toRecurse := map[string]bool{}

	for e, _ := range existing {
		digits := strToDigits(e)
		for d, _ := range allDigits {
			if !digits[d] {
				// add d + e to ret
				newStr := strconv.Itoa(d) + e
				toRecurse[newStr] = true
			}
		}
	}

	return recursiveGenerate(stepsRemaining-1, allDigits, toRecurse)
}

func hasDivisProperty(numStr string) bool {
	// map that tells us start idx + divisibility check
	divisChecks := map[int]int{
		1: 2,
		2: 3,
		3: 5,
		4: 7,
		5: 11,
		6: 13,
		7: 17,
	}

	// check each relevant substring's divisibility
	for startIdx, divisCheck := range divisChecks {
		toCheck, err := strconv.Atoi(numStr[startIdx : startIdx+3])
		if err != nil {
			fmt.Println("error parsing!")
			return false
		}

		if toCheck%divisCheck != 0 {
			return false
		}
	}

	return true
}

// Sum of all 0-9 pandigital numbers with substring divisibility
func main() {
	fmt.Printf("generating pandigital nums\n")

	// generate *all* 9-digit pandigitals
	allDigits := allDigits()
	panDigitalStrs := recursiveGenerate(10, allDigits, map[string]bool{"": true})

	// filter out those with a leading 0
	panDigitalNums := []string{}
	for s, _ := range panDigitalStrs {
		if !strings.HasPrefix(s, "0") {
			panDigitalNums = append(panDigitalNums, s)
		}
	}

	// add all of those satisfying the property
	sum := 0
	for _, s := range panDigitalNums {
		if hasDivisProperty(s) {
			i, err := strconv.Atoi(s)
			if err != nil {
				fmt.Println("error parsing!")
			}

			sum += i
		}
	}

	fmt.Printf("Finished, with sum %d", sum)
}
