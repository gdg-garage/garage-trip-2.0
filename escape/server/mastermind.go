package main

import (
	"fmt"
	"strings"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

type GuessResult struct {
	Configuration []string
	Black         int
	White         int
}

type MasterMind struct {
	Solution     string
	Solved       bool
	GuessHistory []GuessResult // First item is the last guessed (FIFO)
}

func NewMastermind(solution string) *MasterMind {
	return &MasterMind{
		Solution:     solution,
		Solved:       false,
		GuessHistory: []GuessResult{},
	}
}

func strSplit(str string) []string {
	res := []string{}
	for _, s := range str {
		res = append(res, string(s))
	}
	return res
}

func mapToPosition(conf string) map[string][]int {
	res := map[string][]int{}
	for i, c := range conf {
		s := string(c)
		res[s] = append(res[s], i)
	}
	return res
}

func (m *MasterMind) Guess(configuration string) (int, int, error) {
	if len(configuration) != len(m.Solution) {
		return 0, 0, fmt.Errorf("Wrong format")
	}
	configuration = strings.ToUpper(configuration)
	g := GuessResult{
		Configuration: strSplit(configuration),
	}
	if configuration == m.Solution {
		g.Black = len(configuration)
		g.White = 0
		m.GuessHistory = append([]GuessResult{g}, m.GuessHistory...)
		m.Solved = true
		return g.Black, g.White, nil
	}

	sm := mapToPosition(m.Solution)
	cm := mapToPosition(configuration)

	for k := range sm {
		if _, ok := cm[k]; ok {
			localBlack := 0
			for i := 0; i < len(cm[k]); i++ {
				for j := 0; j < len(sm[k]); j++ {
					if cm[k][i] == sm[k][j] {
						localBlack++
					}
				}
			}
			g.White += (min(len(sm[k]), len(cm[k])) - localBlack)
			g.Black += localBlack
		}
	}

	m.GuessHistory = append([]GuessResult{g}, m.GuessHistory...)

	return g.Black, g.White, nil
}

func (m *MasterMind) Reset() {
	m.GuessHistory = []GuessResult{}
	m.Solved = false
}
