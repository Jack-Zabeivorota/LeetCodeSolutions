package main

import (
	"sort"
)

/// Deque

type Node[T any] struct {
	val        T
	prev, next any
}

type Deque[T any] struct {
	left, right *Node[T]
	len         int
}

func NewDeque[T any]() *Deque[T] {
	return &Deque[T]{}
}

func (d *Deque[T]) Len() int {
	return d.len
}

func (d *Deque[T]) Push(val T) {
	if d.len == 0 {
		d.right = &Node[T]{val: val}
		d.left = d.right
		d.len = 1
		return
	}

	d.right = &Node[T]{
		val:  val,
		prev: d.right,
	}
	d.right.prev.(*Node[T]).next = d.right

	d.len++
}

func (d *Deque[T]) PushLeft(val T) {
	if d.len == 0 {
		d.right = &Node[T]{val: val}
		d.left = d.right
		d.len = 1
		return
	}

	d.left = &Node[T]{
		val:  val,
		next: d.left,
	}
	d.left.next.(*Node[T]).prev = d.left

	d.len++
}

func (d *Deque[T]) Pop() T {
	val := d.right.val

	if d.len == 1 {
		d.left, d.right = nil, nil
	} else {
		d.right = d.right.prev.(*Node[T])
		d.right.next = nil
	}

	d.len--
	return val
}

func (d *Deque[T]) PopLeft() T {
	val := d.left.val

	if d.len == 1 {
		d.left, d.right = nil, nil
	} else {
		d.left = d.left.next.(*Node[T])
		d.left.prev = nil
	}

	d.len--
	return val
}

/// Window queue

type WQueue[T any] struct {
	i     int
	arr   []T
	limit float64
}

func NewWQueue[T any](garbageLimit float64) *WQueue[T] {
	return &WQueue[T]{
		arr:   []T{},
		limit: garbageLimit,
	}
}

func (q *WQueue[T]) Len() int {
	return len(q.arr) - q.i
}

func (q *WQueue[T]) reorganize() {
	for i := q.i; i < len(q.arr); i++ {
		q.arr[i-q.i] = q.arr[i]
	}
	q.arr = q.arr[:q.Len()]
	q.i = 0
}

func (q *WQueue[T]) Push(val T) {
	q.arr = append(q.arr, val)

	if len(q.arr) > 100 && q.i > int(q.limit*float64(len(q.arr))) {
		q.reorganize()
	}
}

func (q *WQueue[T]) Pop() (T, bool) {
	if q.Len() == 0 {
		var t T
		return t, false
	}

	val := q.arr[q.i]
	q.i++

	if q.i == len(q.arr) {
		q.arr = q.arr[:0]
		q.i = 0
	}

	return val, true
}

func (q *WQueue[T]) Search(predicate func(T) bool) int {
	return sort.Search(q.Len(), func(i int) bool {
		return predicate(q.arr[i+q.i])
	})
}

/// Solution

/*
|

	Source      - відправник пакета
	Destination - отримувач пакета
	Timestamp   - час прибуття пакета до роутера
*/
type Pack struct {
	Source, Destination, Timestamp int
}

func (p *Pack) ToSlice() []int {
	return []int{p.Source, p.Destination, p.Timestamp}
}

type Router struct {
	register map[Pack]bool
	packs    *Deque[*Pack]
	limit    int
	dests    map[int]*WQueue[*Pack]
}

func Constructor(memoryLimit int) Router {
	return Router{
		register: map[Pack]bool{},
		dests:    map[int]*WQueue[*Pack]{},
		limit:    memoryLimit,
		packs:    NewDeque[*Pack](),
	}
}

func (r *Router) popPack() *Pack {
	// Delete pack from queue and unregister
	pack := r.packs.PopLeft()
	delete(r.register, *pack)

	// Delete pack from queue with destinations
	dest := r.dests[pack.Destination]
	dest.Pop()

	if dest.Len() == 0 {
		delete(r.dests, pack.Destination)
	}
	return pack
}

/*
Додає пакет в чергу, якщо такого пакета ще в ній не має, і повертає `true`,
або якщо такий пакет вже є в черзі, то повертає `false`.
Якщо кількість пакетів перевищує `memoryLimit`, то перший пакет в черзі видаляється.
*/
func (r *Router) AddPacket(source, destination, timestamp int) bool {
	// Create pack

	pack := &Pack{
		Source:      source,
		Destination: destination,
		Timestamp:   timestamp,
	}

	// Check in register

	if r.register[*pack] {
		return false
	}
	r.register[*pack] = true

	// Add pack

	r.packs.Push(pack)
	dest, ok := r.dests[destination]

	if !ok {
		dest = NewWQueue[*Pack](0.5)
		r.dests[destination] = dest
	}
	dest.Push(pack)

	// Delete oldest pack

	if r.packs.Len() > r.limit {
		r.popPack()
	}
	return true
}

/*
Повертає та видаляє перший пакет з черги в форматі `[source, destination, timestamp]`.
Якщо пакетів в черзі не має, то повертає пустий слайс.
*/
func (r *Router) ForwardPacket() []int {
	if r.packs.Len() == 0 {
		return []int{}
	}
	return r.popPack().ToSlice()
}

/*
Повертає кількість пакеті, що знаходятся в черзі, які адресовані `destination`,
і `timestamp` яких входить в діапазон `startTime` та `endTime`.
*/
func (r *Router) GetCount(destination, startTime, endTime int) int {
	dest, ok := r.dests[destination]

	if !ok {
		return 0
	}

	start := dest.Search(func(p *Pack) bool {
		return p.Timestamp >= startTime
	})

	end := dest.Search(func(p *Pack) bool {
		return p.Timestamp > endTime
	})

	return end - start
}
