package main

import (
	"reflect"
	"testing"
)

func TestReverse(t *testing.T) {
	if reverse(1) != 1 {
		t.Errorf("Error: reverse of 1 is 1")
	}

	if reverse(12) != 21 {
		t.Errorf("Error: reverse of 12 is 21")
	}

	if reverse(1123) != 3211 {
		t.Errorf("Error: reverse of 1123 is 3211")
	}
}

func TestIsPalindromic(t *testing.T) {
	if !isPalindromic(1) {
		t.Errorf("1 should be palindromic")
	}

	if isPalindromic(12) {
		t.Errorf("12 is not palindromic")
	}

	if !isPalindromic(1243421) {
		t.Errorf("1243421 should be palindromic")
	}

	if isPalindromic(12434212) {
		t.Errorf("12434212 is not palindromic")
	}
}

func TestCheckLychrel47(t *testing.T) {
	state := State{50, map[int]interface{}{}, map[int]Checkpoint{}}
	isLychrel := state.checkLychrel(47)
	if isLychrel {
		t.Errorf("47 shouldn't be lychrel")
	}

	expectedNonLychrels := map[int]interface{}{47: struct{}{}}
	if !reflect.DeepEqual(state.nonLychrels, expectedNonLychrels) {
		t.Errorf("47 should be only non lychrel in state")
	}

	expectedCheckpoints := map[int]Checkpoint{}
	if !reflect.DeepEqual(state.checkpoints, expectedCheckpoints) {
		t.Errorf("no expected checkpoints")
	}
}

func TestCheckLychrel349(t *testing.T) {
	state := State{50, map[int]interface{}{}, map[int]Checkpoint{}}
	isLychrel := state.checkLychrel(349)
	if isLychrel {
		t.Errorf("349 shouldn't be lychrel")
	}

	expectedNonLychrels := map[int]interface{}{
		349:  struct{}{},
		1292: struct{}{},
		4213: struct{}{},
	}
	if !reflect.DeepEqual(state.nonLychrels, expectedNonLychrels) {
		t.Errorf("Expected logged lychrels from 349 not found")
	}

	expectedCheckpoints := map[int]Checkpoint{}
	if !reflect.DeepEqual(state.checkpoints, expectedCheckpoints) {
		t.Errorf("expected checkpoints for 349 not found")
	}
}

func TestCheckLychrel349LowDepth(t *testing.T) {
	state := State{2, map[int]interface{}{}, map[int]Checkpoint{}}
	isLychrel := state.checkLychrel(349)
	if !isLychrel {
		t.Errorf("349 shouldn't be lychrel when testing with low depth")
	}

	expectedNonLychrels := map[int]interface{}{}
	if !reflect.DeepEqual(state.nonLychrels, expectedNonLychrels) {
		t.Errorf("Expected logged lychrels from 349 (low depth) not found")
	}

	expectedCheckpoints := map[int]Checkpoint{
		349:  Checkpoint{2, 4213},
		1292: Checkpoint{1, 4213},
	}
	if !reflect.DeepEqual(state.checkpoints, expectedCheckpoints) {
		t.Errorf("expected checkpoints for 349 (low depth) not found")
	}
}
