package main

import "testing"

func TestIsAbundant(t *testing.T) {
	if isAbundant(28) {
		t.Errorf("28 must not be abundant")
	}

	if !isAbundant(12) {
		t.Errorf("12 must be abundant")
	}
}
