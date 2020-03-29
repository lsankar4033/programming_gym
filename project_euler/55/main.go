package main

import (
	"fmt"
	"strconv"
	"strings"
)

type Checkpoint struct {
	depth    int
	terminal int
}

type State struct {
	maxDepth    int
	nonLychrels map[int]interface{}
	checkpoints map[int]Checkpoint
}

func reverse(num int) int {
	s := strconv.Itoa(num)

	var c []string = strings.Split(s, "")
	for i, j := 0, len(c)-1; i < j; i, j = i+1, j-1 {
		c[i], c[j] = c[j], c[i]
	}

	rs := strings.Join(c, "")

	rnum, _ := strconv.Atoi(rs)
	return rnum
}

func nextNum(num int) int {
	return num + reverse(num)
}

func isPalindromic(num int) bool {
	return reverse(num) == num
}

// return true if lychrel *and* change state with findings
func (s State) checkLychrel(num int) bool {
	if _, ok := s.nonLychrels[num]; ok {
		return false
	}

	startingCheckpoint := Checkpoint{0, num}
	if checkpoint, ok := s.checkpoints[num]; ok {
		startingCheckpoint = checkpoint
	}

	seenNums := []int{}
	cur := startingCheckpoint.terminal
	isLychrel := true
	for i := startingCheckpoint.depth; i < s.maxDepth; i++ {
		// NOTE: Could make this faster still by checking if next num has a checkpoint already or is a known
		// non-lychrel
		seenNums = append(seenNums, cur)

		cur = nextNum(cur)
		if isPalindromic(cur) {
			isLychrel = false
			break
		}
	}

	if !isLychrel {
		// NOTE: I could delete checkpoints here too. consider it
		for _, num := range seenNums {
			if num <= 10000 {
				s.nonLychrels[num] = struct{}{}
			}
		}

		s.nonLychrels[num] = struct{}{}
	} else {
		for i, num := range seenNums {
			if num <= 10000 {
				s.checkpoints[num] = Checkpoint{
					s.maxDepth - i,
					cur,
				}
			}
		}

		s.checkpoints[num] = Checkpoint{
			s.maxDepth,
			cur,
		}
	}

	return isLychrel
}

func main() {
	count := 0
	state := State{50, map[int]interface{}{}, map[int]Checkpoint{}}
	for i := 0; i < 10000; i++ {
		if state.checkLychrel(i) {
			count += 1
		}
	}

	fmt.Printf("Found %d Lychrels", count)
}
