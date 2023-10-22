using Microsoft.AspNetCore.Mvc;
using server.Models;

[ApiController]
[Route("[controller]")]
public class PetController : ControllerBase
{
    private readonly Supabase.Client _supabase;

    public PetController()
    {
        _supabase = SupabaseService.Supabase;
    }

    [HttpGet]
    public async Task<IEnumerable<SupabasePet>> GetAll()
    {
        var res = await _supabase.From<SupabasePet>().Get();
        return res.Models;
    }
}