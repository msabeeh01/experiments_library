defmodule MyApi.PetsFixtures do
  @moduledoc """
  This module defines test helpers for creating
  entities via the `MyApi.Pets` context.
  """

  @doc """
  Generate a pet.
  """
  def pet_fixture(attrs \\ %{}) do
    {:ok, pet} =
      attrs
      |> Enum.into(%{
        name: "some name"
      })
      |> MyApi.Pets.create_pet()

    pet
  end
end
