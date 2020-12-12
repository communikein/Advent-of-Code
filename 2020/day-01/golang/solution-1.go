package main

import "fmt"
import "io/ioutil"

func main() {
    data, err := ioutil.ReadFile("../input.txt")
    if err != nil {
        fmt.Println("File reading error", err)
        return
    }

    for 
    fmt.Println("Contents of file:")
    fmt.Println(string(data))
}