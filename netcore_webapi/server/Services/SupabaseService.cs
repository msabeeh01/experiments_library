using Supabase;

public class SupabaseService{
    private static Client _supabase = new Client();

    public static Client Supabase{
        get{
            return _supabase;
        }
    }
}