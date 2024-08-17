package main

type HeightData struct {
	Height int
	Delta  int
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func getLastEl(arr []HeightData) *HeightData {
	return &arr[len(arr)-1]
}

/* Slow version of method `maxArea` */
func maxAreaSlow(heights []int) int {
	leftHeights := []HeightData{{heights[0], 0}}
	rightHeights := []HeightData{{heights[len(heights)-1], 0}}

	for l, r := 1, len(heights)-2; r > 0; l, r = l+1, r-1 {
		if heights[l] > getLastEl(leftHeights).Height {
			leftHeights = append(leftHeights, HeightData{heights[l], l})
		}

		if heights[r] > getLastEl(rightHeights).Height {
			rightHeights = append(rightHeights, HeightData{heights[r], l})
		}
	}

	maxWather := 0

	for _, lhd := range leftHeights {
		for _, rhd := range rightHeights {
			delta := len(heights) - lhd.Delta - rhd.Delta - 1

			if delta < 1 {
				break
			}

			wather := delta * Min(lhd.Height, rhd.Height)
			maxWather = Max(maxWather, wather)
		}
	}

	return maxWather
}

/*
Повертає максимальний об'єм води між двома із вказанних в
массиві `heights` висотами

	      m   n
	  n; ;m;m;n
	m n;m;m;m;n

	maxArea([]int{1, 2, 1, 3, 2, 3}) -> 8
*/
func maxArea(heights []int) int {
	maxVolume, l, r := 0, 0, len(heights)-1

	for l < r {
		height := Min(heights[l], heights[r])
		maxVolume = Max(maxVolume, (r-l)*height)

		if heights[l] < heights[r] {
			l++
		} else {
			r--
		}
	}

	return maxVolume
}

func main() {
	print(maxArea([]int{1, 8, 6, 2, 5, 4, 8, 3, 7}))
}
