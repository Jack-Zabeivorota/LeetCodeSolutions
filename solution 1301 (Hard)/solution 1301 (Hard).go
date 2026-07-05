package main

import (
	"strconv"
)

type Cell struct {
	Val, Variates int
}

func calcCell(cells ...Cell) Cell {
	res := Cell{cells[0].Val, 0}

	for _, cell := range cells {
		if cell.Val > res.Val {
			res.Val = cell.Val
		}
	}

	for _, cell := range cells {
		if cell.Val == res.Val {
			res.Variates = (res.Variates + cell.Variates) % 1_000_000_007
		}
	}

	return res
}

/*
Повертає массив з двух елементів:
  - максимальну винагороду, що можно зібрати на карті `board`;
  - кількість шляхів, що привели до максимальної винагороди.

Елементи карти `board`:
  - S - старт;
  - E - фініш;
  - X - перешкода;
  - число - винагорода.

Ігрок починає зі старту і повинен дістатися фінішу уникаючи перешкод.
Ходити можна вверх, вліво або вверх і вліво.

	pathsWithMaxScore([]string{ "E12", "1X1", "21S" }) -> [4, 2]

	// E 1 2
	// 1 X 1
	// 2 1 S

	// Path 1:
	// E 1 2
	//     1
	//     S

	// Path 2:
	// E
	// 1
	// 2 1

	// Revard: 1 + 2 + 1 = 4
*/
func pathsWithMaxScore(board []string) []int {
	// Create dp and set cells

	n := len(board)
	dp := make([][]Cell, n+1)

	for y := range dp {
		dp[y] = make([]Cell, n+1)

		if y == n {
			for x := range dp {
				dp[y][x] = Cell{Val: -1}
			}
			continue
		}

		for x := range board {
			c := board[y][x]

			if c == 'X' {
				dp[y][x] = Cell{Val: -1}

			} else if c != 'E' && c != 'S' {
				val, _ := strconv.Atoi(string(c))
				dp[y][x] = Cell{Val: val}
			}
		}
		dp[y][n] = Cell{Val: -1}
	}

	dp[n-1][n-1].Variates = 1

	// Calculate max revard and posible paths

	for y := n - 1; y >= 0; y-- {
		for x := n - 1; x >= 0; x-- {

			if dp[y][x].Val == -1 {
				continue
			}

			cell := calcCell(dp[y+1][x], dp[y][x+1], dp[y+1][x+1])

			if cell.Val > -1 {
				dp[y][x].Val += cell.Val
				dp[y][x].Variates = cell.Variates

			} else if dp[y][x].Val > 0 {
				dp[y][x] = Cell{Val: -1}
			}
		}
	}

	return []int{dp[0][0].Val, dp[0][0].Variates}
}

func main() {
	res := pathsWithMaxScore([]string{
		"E12",
		"1X1",
		"21S",
	})
	println(res[0], res[1])
}
