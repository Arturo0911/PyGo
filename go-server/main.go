package main

import "fmt"

/*
// Declare data type struct

type Product struct {
    Code string
    Name string
    Stock int
    Price float64
}


// We use * to modify reference from  struct, that is the reason by 
// In the another function only indicates what's the type of varibale in the arguments
func LoadData(product *Product){

    fmt.Print("Codigo: ")
    fmt.Scan(&product.Code)

    fmt.Print("Name: ")
    fmt.Scan(&product.Name)

    fmt.Print("Stock: ")
    fmt.Scan(&product.Stock)

    fmt.Print("Price: ")
    fmt.Scan(&product.Price)

}

func ShowProduct(product Product){
    fmt.Println("The list of product: ")
    fmt.Println("Code => ", product.Code)
    fmt.Println("Name => ", product.Name)
    fmt.Println("Stock => ", product.Stock)
    fmt.Println("Price => ", product.Price)
}




func main (){
    fmt.Println("Hello world")

    var product Product

    LoadData(&product)
    ShowProduct(product)

}*/

/*
type Country struct {
    Name string
    Quantity int
}


func LoadCountry(country *Country){

    fmt.Print("Country name: ")
    fmt.Scan(&country.Name)

    fmt.Print("Country population: ")
    fmt.Scan(&country.Quantity)
    
}


func ShowCountry(country Country) {
    fmt.Println("This is the country and her data.")

    fmt.Println("Country name: ", country.Name)
    fmt.Println("Country population: ", country.Quantity)
}

func main (){

    var country Country

    LoadCountry(&country)

    ShowCountry(country)


}
*/
/*
// This structure is only avaliable for struct Product
type Date_ struct {
    day string
    month string
    year string
}

type Product struct {

    Code string
    Name string
    Stock string
    Price string
    DateVenc Date_

}

func LoadData(product *Product){
    fmt.Print("Code: ")
    fmt.Scan(&product.Code)

    fmt.Print("Name: ")
    fmt.Scan(&product.Name)

    fmt.Print("Stock: ")
    fmt.Scan(&product.Stock)

    fmt.Print("Price: ")
    fmt.Scan(&product.Price)

    fmt.Print("Day: ")
    fmt.Scan(&product.DateVenc.day)

    fmt.Print("Month: ")
    fmt.Scan(&product.DateVenc.month)

    fmt.Print("Year: ")
    fmt.Scan(&product.DateVenc.year)
}



func ShowData (product Product) {
    fmt.Println(product.Code)
    fmt.Println(product.Name)
    fmt.Println(product.Stock)
    fmt.Println(product.Price)
    fmt.Println(product.DateVenc.day)
    fmt.Println(product.DateVenc.month)
    fmt.Println(product.DateVenc.year)
}


func main (){
    var product Product

    LoadData(&product)
    ShowData(product)

} */

/*type Product struct {
    Code string
    Name string
    Price float64
}



func LoadData(product *[4]Product) {
    
    for i:=0; i < len(product); i++ {
        
        fmt.Print("Product code: ")
        fmt.Scan(&product[i].Code)
        
        fmt.Print("Product name: ")
        fmt.Scan(&product[i].Name)

        fmt.Print("Product price: ")
        fmt.Scan(&product[i].Price)
    }

}



func ShowData(product [4]Product){
    
    for j:=0 ; j < len(product); j++ {
        
        fmt.Println(product[j].Code)
        fmt.Println(product[j].Name)
        fmt.Println(product[j].Price)
    }
}


func IsBigger (product [4]Product){
    pos :=0

    for k:=1; k < len(product); k++{

        if product[k].Price > product[pos].Price {
            pos = k
        }
    }

    fmt.Println("El producto más caro es: ", product[pos].Price)

}


func main() {

    var product [4]Product

    LoadData(&product)
    ShowData(product)
    IsBigger(product)

}*/

type Product struct {
    Description string
    Stock int
    Price float64
}


func load (product map[string]Product){

    var code string
    var option string
    var pro Product

    for {

        fmt.Print("Codigo: ")
        fmt.Scan(&code)

        fmt.Print("Description: ")
        fmt.Scan(&pro.Description)

        fmt.Print("Stock: ")
        fmt.Scan(&pro.Stock)

        fmt.Print("Price: ")
        fmt.Scan(&pro.Price)
            
        product[code] = pro

        fmt.Print("Do you load more data ?")
        fmt.Scan(&option)
        
        if option == "n" {
            break
        }

    }

}

func show_(product map[string]Product){
    fmt.Println(": ",product)
    //ftm.Println(range product)
}



func Show (products map[string]Product){
    
    fmt.Println("Completly list")

    for code, product := range products {
        fmt.Println(code)
        fmt.Println("stock: ", product.Stock)
        fmt.Println("price: ", product.Price)
    }
}


func Check (products map[string]Product){
    
    var code string
    
    fmt.Print("Input code: ")
    fmt.Scan(&code)


    product, check := products[code]

    if check {
        fmt.Println("Product exist")
        fmt.Println(product)
        fmt.Println(products[code])
    }else {
        fmt.Println("Product doesn't exist")
    }
}





func main (){
    //var code string
    product := make(map[string]Product)
    
    load(product)
    show_(product)
    Show(product)
    Check(product)
}

