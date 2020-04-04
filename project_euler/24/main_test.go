package main

import "testing"

func TestFactorial(t *testing.T) {
	if factorial(1) != 1 {
		t.Errorf("fact(1) != 1")
	}

	if factorial(3) != 6 {
		t.Errorf("fact(3) != 6")
	}

	if factorial(10) != 3628800 {
		t.Errorf("fact(10) != 3628800")
	}
}
