FROM golang:1.16-buster AS build

WORKDIR /app

COPY go.mod ./
#COPY go.sum ./
RUN go mod download

COPY *.go ./

RUN CGO_ENABLED=0 GOOS=linux go build -o /server

FROM alpine

WORKDIR /

COPY --from=build /server /server
COPY html html
COPY css css
COPY files files

EXPOSE 80

ENTRYPOINT ["./server", "-p", "80"]