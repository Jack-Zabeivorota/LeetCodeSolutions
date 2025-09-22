package main

import (
	"slices"
)

type Entry struct {
	Shop     int
	Movie    int
	Price    int
	IsRented bool
}

func (e *Entry) AsReportItem() []int {
	return []int{e.Shop, e.Movie}
}

type MovieRentingSystem struct {
	list   []*Entry               // sorted list of all entities
	shops  map[int]map[int]*Entry // shops with movies
	movies map[int][]*Entry       // sorted lists of entities related to movies
}

func Constructor(n int, entries [][]int) MovieRentingSystem {
	list := make([]*Entry, len(entries))
	shops := map[int]map[int]*Entry{}

	for i := range entries {
		e := &Entry{
			Shop:  entries[i][0],
			Movie: entries[i][1],
			Price: entries[i][2],
		}
		list[i] = e

		_, ok := shops[e.Shop]

		if !ok {
			shops[e.Shop] = map[int]*Entry{}
		}
		shops[e.Shop][e.Movie] = e
	}

	slices.SortFunc(list, func(e1, e2 *Entry) int {
		if e1.Price == e2.Price {
			if e1.Shop == e2.Shop {

				if e1.Movie < e2.Movie {
					return -1
				}
				if e1.Movie > e2.Movie {
					return 1
				}
				return 0
			}

			if e1.Shop < e2.Shop {
				return -1
			}
			return 1
		}

		if e1.Price < e2.Price {
			return -1
		}
		return 1
	})

	movies := map[int][]*Entry{}

	for _, e := range list {
		movies[e.Movie] = append(movies[e.Movie], e)
	}

	return MovieRentingSystem{
		list:   list,
		shops:  shops,
		movies: movies,
	}
}

/*
Повертає перші 5 магазинів, де можно арендувати фільм `movie` по найдешій ціні
*/
func (s *MovieRentingSystem) Search(movie int) []int {
	result := make([]int, 0, 5)
	movies := s.movies[movie]

	for i := 0; i < len(movies) && len(result) < cap(result); i++ {
		if !movies[i].IsRented {
			result = append(result, movies[i].Shop)
		}
	}

	return result
}

/*
Арендує фільм `movie` в магазині `shop`
*/
func (s *MovieRentingSystem) Rent(shop int, movie int) {
	s.shops[shop][movie].IsRented = true
}

/*
Повертає фільм `movie` назад в магазин `shop`
*/
func (s *MovieRentingSystem) Drop(shop int, movie int) {
	s.shops[shop][movie].IsRented = false
}

/*
Повертає перші 5 найдешевших арендованих фільмів в форматі `[shop, movie]`
*/
func (s *MovieRentingSystem) Report() [][]int {
	result := make([][]int, 0, 5)

	for i := 0; i < len(s.list) && len(result) < cap(result); i++ {
		if s.list[i].IsRented {
			result = append(result, s.list[i].AsReportItem())
		}
	}

	return result
}

func printSlice(ss [][]int) {
	println("Report:")

	for i := range ss {
		for j := range ss[i] {
			print(" ", ss[i][j])
		}
		println()
	}
}

func main() {
	s := Constructor(3, [][]int{
		{0, 1, 5},
		{0, 2, 6},
		{0, 3, 7},
		{1, 1, 4},
		{1, 2, 7},
		{2, 1, 5},
	})
	printSlice([][]int{s.Search(1)})
}
