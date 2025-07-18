<script lang="ts">
	import '../app.css';
	import Sidebar from '../components/navigation/Sidebar.svelte';
	import ImageMask from '../components/utility/ImageMask.svelte';

	let { children } = $props();
</script>

<div class="surface flex h-full w-full flex-row">
	<Sidebar />
	<div class="flex flex-1 flex-col">
		<div
			class="border-surface-container-highest surface-container-low flex h-[81.5px] w-full items-center justify-between gap-4 border-b px-4"
		>
			<h1 class="text-lg font-semibold">Star Rail Conductor</h1>
		</div>
		<div class="flex-1 gap-4 overflow-y-auto p-4">
			{@render children()}
		</div>
	</div>
</div>
