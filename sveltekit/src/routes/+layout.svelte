<script>
    // tailwind import
    import '../app.css'

    // svelte query
    import {QueryClient, QueryClientProvider} from '@sveltestack/svelte-query'

    const queryClient = new QueryClient
</script>


<QueryClientProvider client={queryClient}>
<slot />
</QueryClientProvider>