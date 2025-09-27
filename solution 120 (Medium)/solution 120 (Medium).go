package main

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func last(arr []int) int {
	return arr[len(arr)-1]
}

/*
Повертає мінімальну суму шляхів зверху вниз по трикутнику `triangle`.

	      2
	     ↙ \
	    3   4
	   / ↘ / \
	  6   5   7
	 / \ ↙ \ / \
	4   1   8   9

	minimumTotal([][]int{
		{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 9},
	}) -> 2 + 3 + 5 + 1 = 11
*/
func minimumTotal(triangle [][]int) int {
	t := make([][]int, len(triangle))
	t[0] = []int{triangle[0][0]}

	for i := 1; i < len(t); i++ {
		t[i] = make([]int, len(triangle[i]))

		// Set start and end
		t[i][0] = triangle[i][0] + t[i-1][0]
		t[i][len(t[i])-1] = last(triangle[i]) + last(t[i-1])

		// Set central
		for j := 1; j < len(t[i])-1; j++ {
			t[i][j] = triangle[i][j] + min(t[i-1][j-1], t[i-1][j])
		}
	}

	// Find minimum total path

	lastRow := t[len(t)-1]
	m := lastRow[0]

	for _, val := range lastRow {
		if val < m {
			m = val
		}
	}
	return m
}

func main() {
	println(minimumTotal([][]int{{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 9}}))
}
