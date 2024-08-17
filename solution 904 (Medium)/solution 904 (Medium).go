package main

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

/*
Повертає максимальну кількість зібраних фруктів з ряду дерев,
які вказані в масиві `fruits`, якщо збирати з ліва на право та
всі фрукти в ряд будуть тільки двух видів
(максимальну кількість елеменітів в підмасиві, я кому фігурують тільки два числа)

	totalFruit([]int{1, 6, 3, 2, 2, 4}) -> 3
*/
func totalFruit(fruits []int) int {
	mark1, mark2, maxCount := 0, 0, 0
	fruit1, fruit2 := fruits[0], fruits[0]

	for i, fruit := range fruits {
		if fruit != fruit2 {
			if fruit != fruit1 {
				maxCount = Max(maxCount, i-mark1)
				fruit1, fruit2 = fruit2, fruit
				mark1 = mark2
			} else {
				fruit1, fruit2 = fruit2, fruit1
			}
			mark2 = i
		}
	}

	return Max(maxCount, len(fruits)-mark1)
}

func main() {
	print(totalFruit([]int{3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4}))
}
