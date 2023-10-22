using server.Models;

public static class PizzaServices{
    static List<Pizza> Pizzas {get;}
    
    // static constructor is called only once when the class is loaded for the first time
    static PizzaServices(){
        Pizzas = new List<Pizza>
        {
            new Pizza { Id = 1, Name = "Classic Italian", IsGlutenFree = false },
            new Pizza { Id = 2, Name = "Veggie", IsGlutenFree = true },
            new Pizza { Id = 3, Name = "Pepperoni", IsGlutenFree = false },
            new Pizza { Id = 4, Name = "Hawaiian", IsGlutenFree = true }
        };
    }

    public static List<Pizza> GetAll() => Pizzas;
}

