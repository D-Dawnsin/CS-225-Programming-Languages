package main

import (
	"fmt"
	"math/rand"
	"time"
)

func roll_dice() int {
	rand.Seed(time.Now().UnixNano())
	roll := rand.Intn(7-1) + 1
	return roll
}

func main() {
	fmt.Println("This program will roll two dice for you and output their numbers and then their sum")
	fmt.Println("")

	dice1 := roll_dice()
	fmt.Println("Dice one is: ", dice1)
	dice2 := roll_dice()
	fmt.Println("\nDice one is: ", dice2)

	sum := dice1 + dice2
	fmt.Println("\nThe sum of the two dice is: ", sum)

}
