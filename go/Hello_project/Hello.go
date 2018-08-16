package main

import "fmt"

func main() {
	fmt.Println("Hello world")
	fmt.Println(add(1, 3, "test"))
}

func add(x, y int, z string) int {
	return x + y
}
