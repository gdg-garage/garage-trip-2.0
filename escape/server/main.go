package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"
	"os"
)

func TextHandler(text string) func(http.ResponseWriter, *http.Request) {
	return func(w http.ResponseWriter, r *http.Request) {
		_, err := fmt.Fprint(w, text)
		if err != nil {
			log.Printf("Problem while handling %s %s\n", r.URL, err)
		}
	}
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

	http.HandleFunc("/axzfom", TextHandler("1A"))   // cross
	http.HandleFunc("/PSAMRBJZ", TextHandler("2B")) // cars
	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%d", *port), nil))
}
