package main

import (
	"strconv"
	"strings"
)

/*
Електронна таблиця, в яку можно вставляти, видаляти та діставати значення
з певних клітинок. Таблиця має 26 стовпців (від A до Z) та до 105 рядків
(кількість можна задати в `rows`). Посилання на клітинки мають мають формат
`A10`, тобто стовпчик і рядок.
*/
type Spreadsheet struct {
	matrix [][]int
}

func Constructor(rows int) Spreadsheet {
	matrix := make([][]int, 26)

	for i := range matrix {
		matrix[i] = make([]int, rows)
	}

	return Spreadsheet{
		matrix: matrix,
	}
}

func cellToIndices(cell string) (y, x int) {
	y = int(cell[0]) - 65
	x, _ = strconv.Atoi(cell[1:])
	return y, x - 1
}

func (s *Spreadsheet) SetCell(cell string, value int) {
	y, x := cellToIndices(cell)
	s.matrix[y][x] = value
}

func (s *Spreadsheet) ResetCell(cell string) {
	y, x := cellToIndices(cell)
	s.matrix[y][x] = 0
}

func (s *Spreadsheet) extractValue(source string) int {
	if source[0] >= 65 && source[0] <= 90 {
		y, x := cellToIndices(source)
		return s.matrix[y][x]
	}
	val, _ := strconv.Atoi(source)
	return val
}

/*
Повертає результат `formula`, яка має формат `=X+Y`, де X та Y може бути числом
або посиланням на клітинку.
*/
func (s *Spreadsheet) GetValue(formula string) int {
	i := strings.Index(formula, "+")
	v1, v2 := formula[1:i], formula[i+1:]
	return s.extractValue(v1) + s.extractValue(v2)
}

func main() {
	s := Constructor(10)

	s.SetCell("A7", 5)
	println(s.GetValue("=A7+10")) // 15

	s.ResetCell("A7")
	println(s.GetValue("=10+A7")) // 10
}
