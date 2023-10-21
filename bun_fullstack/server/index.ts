Bun.serve({
    port: 3001,
    fetch(req){
        return new Response('Hello World')
    }
})

console.log('Listening on http://localhost:3001')