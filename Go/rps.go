package main

import "fmt"

func get_player() [5]int {

	x := 1
	var input [5]int

	fmt.Println("1. Rock \n2. Paper \n3. Scissors \n")
	var number int

	for x < 6 {
		fmt.Println("Choose either rock, paper, or scissors for round ", x)
		fmt.Scanln(&number)
		input[x-1] = number
		x += 1
	}
	fmt.Println("")
	return input
}

func winner(play1 [5]int, play2 [5]int) {

	x := 1
	i := 0
	play_outcome1 := 0
	play_outcome2 := 0

	for i < 5 {

		fmt.Println("\nRound ", x, " results")
		////////////////Draws/////////////
		if play1[i] == 1 && play2[i] == 1 {
			fmt.Println("Draw: Rock and Rock")
		}
		if play1[i] == 2 && play2[i] == 2 {
			fmt.Println("Draw: Paper and Paper")
		}
		if play1[i] == 3 && play2[i] == 3 {
			fmt.Println("Draw: Scissors and Scissors")
		}

		////////////////Rock/////////////
		if play1[i] == 1 && play2[i] == 2 {
			fmt.Println("Player 2 wins: Paper beats Rock")
			play_outcome2 += 1
		}
		if play1[i] == 1 && play2[i] == 3 {
			fmt.Println("Player 1 wins: Rock beats Scissors")
			play_outcome1 += 1
		}

		///////////////Paper/////////////
		if play1[i] == 2 && play2[i] == 1 {
			fmt.Println("Player 1 wins: Paper beats Rock")
			play_outcome1 += 1
		}
		if play1[i] == 2 && play2[i] == 3 {
			fmt.Println("Player 2 wins: Scissors beats Paper")
			play_outcome2 += 1
		}

		////////////Scissors/////////////
		if play1[i] == 3 && play2[i] == 1 {
			fmt.Println("Player 2 wins: Rock beats Scissors")
			play_outcome2 += 1
		}
		if play1[i] == 3 && play2[i] == 2 {
			fmt.Println("Player 1 wins: Scissors beats Paper")
			play_outcome1 += 1
		}

		x += 1
		i += 1
	}

	fmt.Println("")

	if play_outcome1 > play_outcome2 {
		fmt.Println("Player 1 wins with ", play_outcome1, " win(s) to ", play_outcome2, " win(s).")
	}
	if play_outcome1 < play_outcome2 {
		fmt.Println("Player 2 wins with ", play_outcome2, " win(s) to ", play_outcome1, " win(s).")
	}
	if play_outcome1 == play_outcome2 {
		fmt.Println("It is a draw as Player 1 has ", play_outcome1, " win(s) and Player 2 has ", play_outcome2, " win(s).")
	}
}

func main() {
	fmt.Println("5 rounds of Rock Paper Scissors")
	fmt.Println("")

	fmt.Println("Up first is player 1")
	player1 := get_player()
	fmt.Println("\n")
	fmt.Println("Next to enter inputs is player 2 and no cheating ;)")
	player2 := get_player()

	winner(player1, player2)
}
