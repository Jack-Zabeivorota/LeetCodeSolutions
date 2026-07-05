package main

import (
	"fmt"
	"sort"
)

/*
Поветає массив із уникальних тріо чисел `nums`, сума яких дорівнює нулю.

	threeSum([]int{-1, 0, 1, 2, -1, -4}) -> []int{ {-1, -1, 2}, {-1, 0, 1} }
*/
func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	res := [][]int{}

	for i := 0; i < len(nums); i++ {
		if nums[i] > 0 {
			break
		}

		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		l, r := i+1, len(nums)-1

		for l < r {
			sum := nums[i] + nums[l] + nums[r]

			if sum == 0 {
				res = append(res, []int{nums[i], nums[l], nums[r]})
				l++
				r--

				for l < r && nums[l] == nums[l-1] {
					l++
				}

				for l < r && nums[r] == nums[r+1] {
					r--
				}

			} else if sum < 0 {
				l++

			} else {
				r--
			}
		}
	}

	return res
}

func main() {
	res := threeSum([]int{-1, 0, 1, 2, -1, -4})

	for _, row := range res {
		fmt.Printf("%d %d %d\n", row[0], row[1], row[2])
	}
}
