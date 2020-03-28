package main

import (
	"reflect"
	"strconv"
	"testing"
)

func TestAllDigits(t *testing.T) {
	actual := allDigits()
	expected := map[int]bool{}
	for i := 0; i < 10; i++ {
		expected[i] = true
	}

	if !reflect.DeepEqual(actual, expected) {
		t.Errorf("Error. Got: %v, want: %v", actual, expected)
	}
}

func TestStrToDigits(t *testing.T) {
	actual := strToDigits("123")
	expected := map[int]bool{1: true, 2: true, 3: true}
	if !reflect.DeepEqual(actual, expected) {
		t.Errorf("Error. Got: %v, want: %v", actual, expected)
	}

	actual = strToDigits("101")
	expected = map[int]bool{0: true, 1: true}
	if !reflect.DeepEqual(actual, expected) {
		t.Errorf("Error. Got: %v, want: %v", actual, expected)
	}
}

func TestRecursiveGenerate(t *testing.T) {
	allDigits := allDigits()

	// 1 step with empty strings
	actual := recursiveGenerate(1, allDigits, map[string]bool{"": true})
	expected := map[string]bool{}
	for i := 0; i < 10; i++ {
		expected[strconv.Itoa(i)] = true
	}
	if !reflect.DeepEqual(actual, expected) {
		t.Errorf("Error. Got: %v, want: %v", actual, expected)
	}

	// 1 step with single-digit strings
	actual = recursiveGenerate(1, allDigits, map[string]bool{"0": true, "1": true})
	expected = map[string]bool{}
	for i := 0; i < 10; i++ {
		if i != 0 {
			expected[strconv.Itoa(i)+"0"] = true
		}

		if i != 1 {
			expected[strconv.Itoa(i)+"1"] = true
		}
	}
	if !reflect.DeepEqual(actual, expected) {
		t.Errorf("Error. Got: %v, want: %v", actual, expected)
	}
}

func TestDivisProperty(t *testing.T) {
	if hasDivisProperty("1111111111") {
		t.Errorf("1111111111 shouldn't have the property")
	}

	if !hasDivisProperty("1406357289") {
		t.Errorf("1406357289 should have the property")
	}
}
