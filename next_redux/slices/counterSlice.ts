import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { PayloadAction } from "@reduxjs/toolkit";

export interface CounterState {
    value: number;
}

const initialState: CounterState = {
    value: 0
};

export const fetch = createAsyncThunk("counter/fetch", async (_, {dispatch}) => {
    await new Promise((resolve) => setTimeout(resolve, 1000));
    return 10;
})

//define slice and actions
export const counterSlice = createSlice({
    name: "counter",
    initialState,
    reducers:{
        increment: (state) => {
            state.value += 1;
        },
        decrement: (state) => {
            state.value -= 1;
        },
        incrementByAmount: (state, action: PayloadAction<number>) => {
            state.value += action.payload;
        },   
    },
    extraReducers: (builder) => {
        builder.addCase(fetch.fulfilled, (state, action) => {
            state.value += action.payload;
        });
    }
});

//export actions for slice
export const {increment, decrement, incrementByAmount} = counterSlice.actions;


//export reducer for slice
export default counterSlice.reducer;
