package main

// Given a string, find the length of the longest substring without repeating characters.

// Examples:

// Given "abcabcbb", the answer is "abc", which the length is 3.

// Given "bbbbb", the answer is "b", with the length of 1.

// Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
// "pwke" is a subsequence and not a substring.

func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}

func lengthOfLongestSubstring(s string) int {
	var length, start int
	mp := make(map[rune]int)

	for i, v := range s {
		if index, ok := mp[v]; ok {
			start = max(start, index + 1)
		}
		mp[v] = i
		length = max(length, i - start + 1)
	}
	return length
}
