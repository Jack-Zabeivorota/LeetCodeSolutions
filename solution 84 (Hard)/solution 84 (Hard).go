package main

type Height struct {
	Height   int
	Position int
}

func GetLast(stack []Height) (Height, bool) {
	if len(stack) == 0 {
		return Height{}, false
	}
	return stack[len(stack)-1], true
}

func Pop(stack []Height) []Height {
	return stack[:len(stack)-1]
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

/*
Повертає периметр найбільшого прямокутника, який можна вписати
в гістограму указану в массиві `heights`

	      m
	    o o
	    o o
	    o o   m
	m   o o m m
	m m o o m m

	largestRectangleArea([]int{2, 1, 5, 6, 2, 3}) -> 10
*/
func largestRectangleArea(heights []int) int {
	maxArea := 0
	stack := []Height{}

	for i := 0; i < len(heights); i++ {
		lastHeight, ok := GetLast(stack)
		height := Height{heights[i], i}

		if !ok || lastHeight.Height < heights[i] {
			stack = append(stack, height)
			continue
		}

		for ok && lastHeight.Height > heights[i] {
			area := (i - lastHeight.Position) * lastHeight.Height
			maxArea = Max(maxArea, area)

			height.Position = lastHeight.Position
			stack = Pop(stack)
			lastHeight, ok = GetLast(stack)
		}

		if !ok || lastHeight.Height < height.Height {
			stack = append(stack, height)
		}
	}

	n := len(heights)

	for _, height := range stack {
		area := (n - height.Position) * height.Height
		maxArea = Max(maxArea, area)
	}

	return maxArea
}

func main() {
	print(largestRectangleArea([]int{2, 1, 5, 6, 2, 3}))
}
