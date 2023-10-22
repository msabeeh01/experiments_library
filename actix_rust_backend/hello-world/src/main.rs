use actix_web::{get, web, App, HttpResponse, HttpServer, Responder};
use postgrest::Postgrest;
use serde::Deserialize;
use serde::Serialize;
use lazy_static::lazy_static;

// supabase

lazy_static!(
    static ref CLIENT: Postgrest = create_client();
);

#[get("/")]
async fn hello() -> impl Responder {
    HttpResponse::Ok().body("Hello world!")
}

#[derive(Deserialize, Serialize)]
struct Pet {
    pet_name: String,
    pet_desc: String
}

#[get("/pets")]
async fn get_pet() -> impl Responder {
    let response = CLIENT.from("pets").select("*").execute().await;
    match response {
        Ok(res) => {
            let res_body = res.text().await.unwrap();
            let pet: Pet = serde_json::from_str(&res_body).unwrap();
            let pet_json = serde_json::to_string(&pet).unwrap();
            HttpResponse::Ok().json(pet_json) // Return the JSON
        },
        Err(e) => {
            println!("{:?}", e);
            HttpResponse::InternalServerError().finish()
        }
    }
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(hello)
            .service(get_pet)
        })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}