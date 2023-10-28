<script lang="ts">
    import type { PageData } from './$types';
    export let data: PageData
	// // button imports
	import Card from '../components/Card.svelte';


</script>

<div class="grid grid-cols-3 text-center grid-cols items-center justify-center gap-5">
    {#each data.todos as {id, title}}
        <Card id={id} title={title} />
    {/each}
</div>
