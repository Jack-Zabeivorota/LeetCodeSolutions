package main

/*
Повертає максимальну кількість випитих пляшок, виходячи з наступиних правил:
	- Спочатку є `fulles` повних пляшок. Повні пляшки можна випити
	перетворюючи їх на пусті;
	- Пусті пляшки в кількості `numExchange` штук, можна обміняти
	на одну повну пляшку (після кожного обміну `numExchange`
	збільшується на одиницю).
*/
func maxBottlesDrunk(fulles, numExchange int) int {
	empties, drinked := fulles, fulles
	fulles = 0

	for {
		if empties < numExchange {
			empties += fulles
			drinked += fulles
			fulles = 0

			if empties < numExchange {
				return drinked
			}
		}

		empties -= numExchange
		fulles++
		numExchange++
	}
}

func main() {
	println(maxBottlesDrunk(13, 6)) // -> 15
	println(maxBottlesDrunk(10, 3)) // -> 13
}
