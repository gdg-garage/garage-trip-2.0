package main

import (
	"flag"
	"fmt"
	"html/template"
	"log"
	"net/http"
	"os"
)

var mastermind MasterMind = MasterMind{Solution: "RYPBRT"}

type Page struct {
	Title        string
	Body         []byte
	GuessHistory []GuessResult
	Win          bool
}

func loadPage(title string) (*Page, error) {
	return &Page{
		Title:        title,
		GuessHistory: mastermind.GuessHistory,
		Win:          mastermind.Solved}, nil
}

func TextHandler(text string) func(http.ResponseWriter, *http.Request) {
	return func(w http.ResponseWriter, r *http.Request) {
		_, err := fmt.Fprint(w, text)
		if err != nil {
			log.Printf("Problem while handling %s %s\n", r.URL, err)
		}
	}
}

func MasterMindHandler(w http.ResponseWriter, r *http.Request) {
	title := "Mastermind"
	p, err := loadPage(title)
	if err != nil {
		fmt.Println(err.Error())
		p = &Page{Title: title}
	}
	t, _ := template.ParseFiles("html/mastermind.html")
	t.Execute(w, p)
}

func MasterMindGuessHandler(w http.ResponseWriter, r *http.Request) {
	guess := r.FormValue("body")
	_, _, err := mastermind.Guess(guess)
	if err != nil {
		fmt.Println(err.Error())
	}
	http.Redirect(w, r, "/logik/game", http.StatusFound)
}

func main() {
	var port = flag.Int("p", 8080, "Port")
	var logfile = flag.String("l", "log.txt", "Logfile")
	flag.Parse()

	file, err := os.OpenFile(*logfile, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0666)
	if err != nil {
		log.Fatal(err)
	}
	log.SetOutput(file)

	http.Handle("/css/", http.StripPrefix("/css/", http.FileServer(http.Dir("./css/"))))
	http.HandleFunc("/axzfom", TextHandler("1A"))     // cross
	http.HandleFunc("/PSAMRBJZ", TextHandler("2B"))   // cars
	http.HandleFunc("/logik/game", MasterMindHandler) // mastermind
	http.HandleFunc("/logik/guess", MasterMindGuessHandler)

	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%d", *port), nil))
}
