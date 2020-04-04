package main

import "testing"

func TestPrime(t *testing.T) {
	if !isPrime(2) {
		t.Errorf("2 is prime")
	}

	if isPrime(4) {
		t.Errorf("4 isn't prime")
	}

	if !isPrime(7) {
		t.Errorf("7 is prime")
	}
}
