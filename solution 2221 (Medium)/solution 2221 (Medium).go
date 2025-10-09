package main

/*
Повертає суму вершини трикутника з основами `nums`

	1   2   3   4   5
	 \ / \ / \ / \ /
	  3   5   7   9
	   \ / \ / \ /
	    8   2   6
		 \ / \ /
		  0   8
		   \ /
		    8

	triangularSum([]int{1, 2, 3, 4, 5}) -> 8
*/
func triangularSum(nums []int) int {
	for n := len(nums) - 1; n > 0; n-- {
		for i := 0; i < n; i++ {
			nums[i] = (nums[i] + nums[i+1]) % 10
		}
	}
	return nums[0]
}

func main() {
	println(triangularSum([]int{1, 2, 3, 4, 5}))
}
