package main

import (
	"fmt"
	"math/big"
)

func main() {
	terms := make(map[string]bool)
	for a := 2; a <= 100; a++ {
		for b := 2; b <= 100; b++ {
			ab := big.NewInt(int64(a))
			bb := big.NewInt(int64(b))

			terms[ab.Exp(ab, bb, nil).String()] = true
		}
	}

	fmt.Printf("len(terms) = %+v\n", len(terms))
}
