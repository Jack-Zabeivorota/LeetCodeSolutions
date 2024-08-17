package main

func numDistinct(source, word string) int {
	rows, columns := len(source)+1, len(word)+1

	table := make([][]int, rows)

	for y := 0; y < rows; y++ {
		table[y] = make([]int, columns)
		table[y][0] = 1
	}

	for y := 1; y < rows; y++ {
		for x := 1; x < columns; x++ {
			if source[y-1] == word[x-1] {
				table[y][x] = table[y-1][x-1] + table[y-1][x]
			} else {
				table[y][x] = table[y-1][x]
			}
		}
	}

	return table[rows-1][columns-1]
}

func main() {
	print(numDistinct("rabbbit", "rabbit"))
}

/*
  rabbit
r 100000
a 110000
b 111000
b 112100
b 113300
i 113330
t 113333
*/
