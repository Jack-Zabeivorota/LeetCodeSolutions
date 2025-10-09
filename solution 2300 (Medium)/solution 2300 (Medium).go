package main

import (
	"slices"
	"sort"
)

func last(arr []int) int {
	return arr[len(arr)-1]
}

/*
Повертає пари закляття-зілля, добуток яких досягає або перевищує `success`

	successfulPairs([]int{5,1,3}, []int{1,5,3,4,2}, 7) -> [4,0,3]
	// 5 * [1 5 3 4 2] = [5 25 15 20 10] -> 4
	                        ‾‾ ‾‾ ‾‾ ‾‾
	// 1 * [1 5 3 4 2] = [5 5 3 4 2] -> 0

	// 3 * [1 5 3 4 2] = [3 15 9 12 6] -> 3
						    ‾‾ ‾ ‾‾
*/
func successfulPairs(spells []int, potions []int, success int64) []int {
	slices.Sort(potions)
	pairs := make([]int, len(spells))

	for i := range spells {

		// if weakest pair passes, then all pairs pass
		if spells[i]*potions[0] >= int(success) {
			pairs[i] = len(potions)

			// if strongest pair didn't passes, then all pairs didn't pass
		} else if spells[i]*last(potions) < int(success) {
			pairs[i] = 0

			// find the line between potions of suitable strength
			// and calculate number of pairs
		} else {
			pairs[i] = len(potions) - sort.Search(len(potions), func(j int) bool {
				return spells[i]*potions[j] >= int(success)
			})
		}

	}
	return pairs
}

func main() {
	pairs := successfulPairs([]int{5, 1, 3}, []int{1, 5, 3, 4, 2}, 7)

	for _, p := range pairs {
		print(p, " ")
	}
	println()
}
