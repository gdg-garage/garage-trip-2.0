package main

import (
	"testing"
)

type out struct {
	black int
	white int
	err   error
}

func testInternal(a string, b string, expected out, t *testing.T) {
	m := NewMastermind(a)
	black, white, err := m.Guess(b)
	if black != expected.black || white != expected.white || err != expected.err {
		t.Errorf(`In: %s, %s, black: have %d, want %d; white: have %d, want %d; err %v`, a, b, black, expected.black, white, expected.white, err)
	}
}

func TestMasterMind(t *testing.T) {
	testInternal("RGB", "RGB", out{3, 0, nil}, t)
	testInternal("RGB", "BGR", out{1, 2, nil}, t)
	testInternal("WBGT", "BWGT", out{2, 2, nil}, t)
	testInternal("BBB", "BGT", out{1, 0, nil}, t)
}
