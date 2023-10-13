import { create } from "zustand";

interface BearState {
    bears: number;
    increase: (number: number) => void;
    fetch: () => void;
}

export const useBearStore = create<BearState>(
    (set): BearState => ({
        bears: 0,
        increase: (number: number) => set(state => ({ bears: state.bears + number })),
        fetch: async () => {
            setTimeout(async () => {
                set({ bears: 100 })
            }, 1000);
        }
    })
)