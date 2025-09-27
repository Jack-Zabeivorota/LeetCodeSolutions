package main

import (
	"fmt"
	"strconv"
	"strings"
)

/*
Повертає результат ділення `num` на `den` в строковому форматі.
Періодична дробова частина знаходится в дужках: 1.16666... -> 1.1(6)
*/
func fractionToDecimal(num, den int) string {
	if num == 0 {
		return "0"
	}
	sb := &strings.Builder{}

	// Get rid of the sign

	if (num < 0) != (den < 0) {
		sb.WriteByte('-')
	}
	n, d := int64(num), int64(den)

	if n < 0 {
		n = -n
	}
	if d < 0 {
		d = -d
	}

	// Integer part

	sb.WriteString(strconv.FormatInt(n/d, 10))
	rem := n % d

	if rem == 0 {
		return sb.String()
	}

	// Fractional part

	sb.WriteByte('.')
	pos := map[int64]int{}

	for rem > 0 {
		if p, ok := pos[rem]; ok {
			s := sb.String()
			return fmt.Sprintf("%s(%s)", s[:p], s[p:])
		}
		pos[rem] = sb.Len()
		rem *= 10
		sb.WriteString(strconv.FormatInt(rem/d, 10))

		rem %= d
	}

	return sb.String()
}

func main() {
	println(fractionToDecimal(4, 2))  // -> 2
	println(fractionToDecimal(1, 8))  // -> 0.125
	println(fractionToDecimal(1, 3))  // -> 0.(3)
	println(fractionToDecimal(5, 28)) // -> 0.17(857142)
}
