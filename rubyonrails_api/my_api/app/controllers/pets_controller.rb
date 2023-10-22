class PetsController < ApplicationController
    def index
        @pets = Pet.all
        render json: @pets
    end

    def create
        @pet = Pet.create(pet_params)
        if @pet.save
            render json: @pet, status: :created
        else
            render json: @pet.errors, status: :unprocessable_entity
        end
    end

    private

    def pet_params
        params.require(:pet).permit(:name)
    end
end
