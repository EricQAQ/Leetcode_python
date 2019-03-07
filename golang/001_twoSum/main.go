package main

import (
	"fmt"
)

// Given an array of integers, return indices of the two numbers such that they add up to a specific target.

// You may assume that each input would have exactly one solution.

// Example:
// Given nums = [2, 7, 11, 15], target = 9,

// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].

func twoSum(nums []int, target int) []int {
	rv := make([]int, 2)
	rev := make(map[int]int, len(nums))
	for i, v := range nums {
		if idx, ok := rev[v]; ok && v + v == target {
			rv[0] = i
			rv[1] = idx
			return rv
		}
		rev[v] = i
	}

	for v, index := range rev {
		if idx, ok := rev[target - v]; ok && idx != index {
			rv[0] = index
			rv[1] = idx
			return rv
		}
	}
	return rv
}

// 整体思路和上一个一样
func twoSum2(nums []int, target int) []int {
	rv := make([]int, 2)
	rev := make(map[int]int, len(nums))

	for i, v := range nums {
		if idx, ok := rev[target - v]; ok {
			rv[0] = idx
			rv[1] = i
			return rv
		}
		rev[v] = i
	}
	return rv
}
