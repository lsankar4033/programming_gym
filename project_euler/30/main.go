package main

import (
	"fmt"
	"strconv"
)

func digitSum(n int) int {
	s := strconv.Itoa(n)

	sum := 0
	for _, c := range s {
		d, _ := strconv.Atoi(string(c))

		sum += (d * d * d * d * d)
	}

	return sum
}

func main() {
	fmt.Println("vim-go")

	i := 1332
	s := strconv.Itoa(i)
	fmt.Printf("s = %+v\n", s)
	fmt.Printf("s[2] = %+v\n", string(s[2]))

	sum := 0
	for i := 10; i < 413343; i++ {
		ds := digitSum(i)

		if ds == i {
			fmt.Printf("i = %+v\n", i)
			sum += i
		}
	}

	fmt.Printf("sum = %+v\n", sum)
}
