package main

import "testing"

func TestDigitSum(t *testing.T) {
	if digitSum(11) != 2 {
		t.Errorf("digitSum(11) != 2")
	}

	if digitSum(22122) != 129 {
		t.Errorf("digitSum(22122) != 129")
	}
}
