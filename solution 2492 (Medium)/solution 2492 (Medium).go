package main

type Road struct {
	To, Dis int
}

/*
Повертає найменшу дистанцію дороги із массиву дорог `roads`
яка входить в шлях від міста 1 до міста `n`.

	minScore(4, [][]int{
	//{from, to, distance}
		{1,   2,   5},
		{1,   3,   7},
		{3,   4,   9},
	}) -> 5

	//   (1)
	//  7/ \5
	// (3) (2)
	//  9\
	//   (4)
	//
	// Path: (1) -5-> (2) -5-> (1) -7-> (3) -9-> (4)
*/
func minScore(n int, roads [][]int) int {
	nodes := make([][]Road, n+1)

	for _, road := range roads {
		n1, n2, dis := road[0], road[1], road[2]
		nodes[n1] = append(nodes[n1], Road{n2, dis})
		nodes[n2] = append(nodes[n2], Road{n1, dis})
	}

	visited := make([]bool, n+1)
	visited[1] = true

	queue := []int{1}
	minDis := nodes[1][0].Dis

	for i := 0; i < len(queue); i++ {
		node := queue[i]

		for _, road := range nodes[node] {
			if road.Dis < minDis {
				minDis = road.Dis
			}

			if !visited[road.To] {
				visited[road.To] = true
				queue = append(queue, road.To)
			}
		}
	}

	return minDis
}

func main() {
	println(minScore(4, [][]int{{1, 2, 9}, {2, 3, 6}, {2, 4, 5}, {1, 4, 7}}))
	println(minScore(4, [][]int{{1, 2, 5}, {1, 3, 7}, {3, 4, 9}}))
}
