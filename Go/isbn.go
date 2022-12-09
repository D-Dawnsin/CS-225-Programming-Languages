package main

import "fmt"

func get_isbn() [9]int {
	var input [9]int
	x := 1
	var number int

	for x < 10 {
		fmt.Println("Enter a number between 0 and 9 for number ", x)
		fmt.Scanln(&number)
		input[x-1] = number
		x++
	}

	return input
}

func compute_marker(array [9]int) int {

	var multiplications [9]int

	for i := 0; i < len(array); i++ {
		x := i + 1
		multiplications[i] = array[i] * x
	}

	var number int
	for i := 0; i < len(multiplications); i++ {
		number += multiplications[i]
	}

	marker := number % 11

	return marker
}

func main() {
	fmt.Println("Welcome to an ISBN marker calculater.")
	fmt.Println("")

	var isbn [9]int = get_isbn()
	var marker int = compute_marker(isbn)
	fmt.Println("The ISBN you inputted: ")
	for i := 0; i < 9; i++ {
		fmt.Print(isbn[i])
	}

	fmt.Println("")
	fmt.Println("Your ISBN with the marker: ")

	for i := 0; i < 9; i++ {
		fmt.Print(isbn[i])
	}
	if marker >= 10 {
		fmt.Print("X")
	} else {
		fmt.Print(marker)
	}

}
