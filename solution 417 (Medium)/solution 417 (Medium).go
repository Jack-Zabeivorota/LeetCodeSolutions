package main

/// Queue

type Node[T any] struct {
	val  T
	next any
}

type Queue[T any] struct {
	first, last *Node[T]
	len         int
}

func (q *Queue[T]) Len() int {
	return q.len
}

func (q *Queue[T]) Push(val T) {
	node := &Node[T]{val: val}

	if q.first == nil && q.last == nil {
		q.first, q.last = node, node
	} else {
		q.last.next = node
		q.last = node
	}
	q.len++
}

func (q *Queue[T]) Pop() T {
	val := q.first.val

	if q.len == 1 {
		q.first, q.last = nil, nil
	} else {
		q.first = q.first.next.(*Node[T])
	}

	q.len--
	return val
}

/// Solution

func createOceanMap(rows, columns int) [][][]bool {
	matrix := make([][][]bool, rows)

	for y := range matrix {
		matrix[y] = make([][]bool, columns)

		for x := range matrix[y] {
			matrix[y][x] = make([]bool, 2)
		}
	}
	return matrix
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func traceFlow(hs [][]int, omap [][][]bool, y, x, ocean int, pos *[][]int) {
	if omap[y][x][ocean] {
		return
	}
	omap[y][x][ocean] = true

	shift := []int{
		-1, 0,
		0, -1,
		1, 0,
		0, 1,
	}
	queue := &Queue[[]int]{}
	queue.Push([]int{y, x})

	r, c := len(hs), len(hs[0])

	for queue.Len() > 0 {
		p := queue.Pop()
		y, x = p[0], p[1]

		if omap[y][x][0] && omap[y][x][1] {
			*pos = append(*pos, []int{y, x})
		}

		for i := 0; i < len(shift); i += 2 {
			y_, x_ := y+shift[i], x+shift[i+1]

			// out of matrix
			if y_ == -1 || x_ == -1 || y_ == r || x_ == c {
				continue
			}

			//     more higher              not same ocean
			if hs[y_][x_] >= hs[y][x] && !omap[y_][x_][ocean] {
				omap[y_][x_][ocean] = true
				queue.Push([]int{y_, x_})
			}
		}
	}
}

/*
Повертає позиції секторів острова ([y, x]), з яких вода може стікати
як в Тихий, так і в Атлантичний океани (Тихий океан омиває північ і
захід острову, а Атлантичний омиває схід і південь).

`heights` - висоти секторів острова.

	pacificAtlantic([][]int{
		{1, 2, 2, 3, 5},
		{3, 2, 3, 4, 4},
		{2, 4, 5, 3, 1},
		{6, 7, 1, 4, 5},
		{5, 1, 1, 2, 4},
	}) -> [[0,4], [1,3], [1,4], [2,2], [3,0], [3,1], [4,0]]

	//  Ocean map:

	//      0   1   2   3   4
	//      ------------------
	//	0 | p , p , p , p , pa,
	//	1 | p , p , p , pa, pa,
	//	2 | p , p , pa,  a,  a,
	//	3 | pa, pa,  a,  a,  a,
	//	4 | pa,  a,  a,  a,  a,
*/
func pacificAtlantic(heights [][]int) [][]int {
	r, c := len(heights), len(heights[0])
	omap := createOceanMap(r, c)
	pos := [][]int{}

	pacific, atlantic := 0, 1

	for y := range heights {
		traceFlow(heights, omap, y, 0, pacific, &pos)
		traceFlow(heights, omap, y, c-1, atlantic, &pos)
	}
	for x := range heights[0] {
		traceFlow(heights, omap, 0, x, pacific, &pos)
		traceFlow(heights, omap, r-1, x, atlantic, &pos)
	}
	return pos
}

func printMartix(m [][]int) {
	for i := range m {
		println(m[i][0], m[i][1])
	}
	println("---")
}

func main() {
	printMartix(pacificAtlantic([][]int{
		{1, 2, 2, 3, 5},
		{3, 2, 3, 4, 4},
		{2, 4, 5, 3, 1},
		{6, 7, 1, 4, 5},
		{5, 1, 1, 2, 4},
	}))
	//  Ocean map:
	//	{p , p , p , p , pa},
	//	{p , p , p , pa, pa},
	//	{p , p , pa,  a,  a},
	//	{pa, pa,  a,  a,  a},
	//	{pa,  a,  a,  a,  a},

	printMartix(pacificAtlantic([][]int{
		{1, 2},
		{4, 3},
	}))
	//  Ocean map:
	//	{p , pa},
	//	{pa, pa},
}
