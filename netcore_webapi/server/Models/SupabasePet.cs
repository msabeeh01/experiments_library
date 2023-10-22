using Postgrest.Attributes;
using Postgrest.Models;

namespace server.Models;

[Table("pets")]
public class SupabasePet : BaseModel {
    [PrimaryKey("id", false)]
    public int Id { get; set; }

    [Column("pet_name")]
    public string? name { get; set; }
    [Column("pet_desc")]
    public string? desc { get; set; }
    [Column("user_id")]
    public string? userId { get; set; }
    [Column("created_at")]
    public DateTime createdAt { get; set; }
}



