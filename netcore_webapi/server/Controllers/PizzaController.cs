using Microsoft.AspNetCore.Mvc;
using server.Models;

[ApiController]
[Route("[controller]")]
public class PizzaController : ControllerBase{
    public PizzaController(){
        
    }

    //when "/pizza" is requested, this method is called
    [HttpGet]
    public ActionResult<List<Pizza>> GetAll(){
        return PizzaServices.GetAll();
    }
}