import type { PageServerLoad } from "./$types";


export const load: PageServerLoad = async () => {
    const response = await fetch("https://jsonplaceholder.typicode.com/todos");
    const data = await response.json();
    console.log(data)
    return { todos: data.map((todo: any) => ({
        title: todo.title,
        id: todo.id

    }))};
}
