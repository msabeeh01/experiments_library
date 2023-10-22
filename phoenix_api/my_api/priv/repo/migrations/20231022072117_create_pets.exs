defmodule MyApi.Repo.Migrations.CreatePets do
  use Ecto.Migration

  def change do
    create table(:pets) do
      add :name, :string

      timestamps(type: :utc_datetime)
    end
  end
end
