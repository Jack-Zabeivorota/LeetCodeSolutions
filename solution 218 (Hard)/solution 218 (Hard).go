package main

import "sort"

type Building struct {
	X1, X2, H int
}

/* Slow version of method `getSkyline` */
func getSkylineSlow(buildings [][]int) [][]int {
	prevs, highs, lows := map[Building]bool{}, map[int]int{}, [][]int{}

	// find hights and lowers points of buildings

	for _, building := range buildings {
		x1, x2, h := building[0], building[1], building[2]

		is_save_high := true
		low_h := 0
		deleted_prevs := []Building{}

		for prev := range prevs {
			// delete preview building if it is not actual
			if prev.X2 < x1 {
				deleted_prevs = append(deleted_prevs, prev)
				continue
			}

			// save high point if none of the previous buildings cover it
			if is_save_high && prev.H >= h {
				is_save_high = false
			}

			// raise the low point to the height of the highest building,
			// or remove the point if it is covers by another building
			if low_h > -1 && x2 < prev.X2 && prev.H > low_h {
				if prev.H < h {
					low_h = prev.H
				} else {
					low_h = -1
				}
			}
		}

		// raise all the low points that this building covers
		for _, low := range lows {
			l_x, l_h := low[0], low[1]

			if x1 <= l_x && l_x < x2 && h > l_h {
				low[1] = h
			}
		}

		if is_save_high {
			highs[x1] = h
		}

		if low_h > -1 {
			lows = append(lows, []int{x2, low_h})
		}

		for _, dp := range deleted_prevs {
			delete(prevs, dp)
		}
		prevs[Building{x1, x2, h}] = true
	}

	// merge all points and sort them by x-axis

	points := make([][]int, len(highs)+len(lows))
	i := 0

	for x, h := range highs {
		points[i] = []int{x, h}
		i++
	}

	for _, p := range lows {
		points[i] = p
		i++
	}

	sort.Slice(points, func(i, j int) bool {
		return points[i][0] < points[j][0]
	})

	// filter all points in a row at the same height

	result, curr_h := [][]int{}, -1

	for _, p := range points {
		if p[1] != curr_h {
			result = append(result, p)
			curr_h = p[1]
		}
	}

	return result
}

func binarySearchStart(points [][]int, x int) int {
	if len(points) == 0 || x > points[len(points)-1][0] {
		return -1
	}

	li, hi := -1, len(points)-1

	for li+1 < hi {
		mid := (li + hi) / 2

		if points[mid][0] >= x {
			hi = mid
		} else {
			li = mid
		}
	}

	return hi
}

/*
Повертає точки (x,y), які описують силует будівель `buildings` (x1, x2, height)

	5 ///|\\\                  *------
	4 |     |   ///|\\\        |     |   *------
	3 |     |   |     |        |     |   |     |
	2 |  /////|\\\\\  |   ->   |     *----     |
	1 |  |         |  |        |               *
	  0  3  6  10 13 16        0  3  6  10 13 16

	getSkyline([][]int{{0, 6, 5}, {3, 13, 2}, {10, 16, 4}}) -> {{0,5}, {6,2}, {10,4}, {16.0}}
*/
func getSkyline(buildings [][]int) [][]int {
	// find all points

	points := make([][]int, len(buildings)*2)
	i := 0

	for _, b := range buildings {
		x1, x2, h := b[0], b[1], b[2]

		points[i] = []int{x1, h}
		i++
		points[i] = []int{x2, 0}
		i++
	}

	// sort points by X-axis
	sort.Slice(points, func(i, j int) bool {
		return points[i][0] < points[j][0]
	})

	// align the points to the general silhouette of the buildings
	for _, b := range buildings {
		x1, x2, h := b[0], b[1], b[2]

		i = binarySearchStart(points, x1)

		if i == -1 {
			break
		}

		for points[i][0] < x2 {
			if h > points[i][1] {
				points[i][1] = h
			}
			i++
		}
	}

	// filter out unnecessary points
	// (which lie at the same height or in the same X-position)

	result, curr_h, curr_x := make([][]int, 0, len(points)-len(points)/3), -1, -1

	for _, p := range points {
		if p[0] != curr_x && p[1] != curr_h {
			result = append(result, p)
			curr_x, curr_h = p[0], p[1]
		}
	}

	return result
}

func main() {
	points := getSkyline([][]int{{0, 6, 5}, {3, 13, 2}, {10, 16, 4}})

	for _, p := range points {
		println(p[0], p[1])
	}
}
