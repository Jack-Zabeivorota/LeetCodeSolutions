package main

type ListNode struct {
	Val  int
	Next *ListNode
}

/*
Повертає сумму двох чисел, які закодованих в листах `l1` та `l2`

	// 328 + 54 = 382
	addTwoNumbers(8->2->3, 4->5) -> 2->8->3
*/
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	root := &ListNode{}
	l := root
	rem := 0
	n1, n2 := l1.Val, l2.Val

	for {
		l.Val = n1 + n2 + rem
		rem = 0

		if l.Val > 9 {
			rem = 1
			l.Val -= 10
		}

		if l1.Next == nil && l2.Next == nil {
			if rem == 1 {
				l.Next = &ListNode{Val: 1}
			}
			return root
		}

		if l1.Next != nil {
			l1 = l1.Next
			n1 = l1.Val
		} else {
			n1 = 0
		}

		if l2.Next != nil {
			l2 = l2.Next
			n2 = l2.Val
		} else {
			n2 = 0
		}

		l.Next = &ListNode{}
		l = l.Next
	}
}

func NewList(nums ...int) *ListNode {
	root := &ListNode{}
	node := root

	for _, num := range nums {
		node.Val = num
		node.Next = &ListNode{}
		node = node.Next
	}
	node.Next = nil

	return root
}

func ListToNum(l *ListNode) int {
	result := 0
	mult := 1

	for {
		result += l.Val * mult

		if l.Next == nil {
			return result
		}

		l = l.Next
		mult *= 10
	}
}

func main() {
	println(ListToNum(addTwoNumbers(NewList(2, 4, 3), NewList(5, 6, 4))))
}
