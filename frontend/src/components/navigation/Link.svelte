<script lang="ts">
	import { page } from '$app/state';
	import clsx from 'clsx';
	import ImageMask from '../utility/ImageMask.svelte';

	let { data }: { data: LinkData } = $props();

	let active = $derived(page.url.pathname == data.href);
</script>

<a
	href={data.href}
	class={clsx(
		'flex aspect-square h-16 w-full flex-row items-center gap-4 overflow-clip rounded-md p-2 lg:aspect-auto',
		active
			? 'bg-surface-container-highest'
			: 'bg-surface-container-high hover:bg-surface-container-highest transition-colors duration-200 ease-in-out'
	)}
>
	<ImageMask
		image={data.icon}
		class={clsx(
			'aspect-square h-full object-contain transition-colors duration-200 ease-in-out',
			active ? 'bg-primary' : 'bg-on-surface'
		)}
	/>
	<span
		class={clsx(
			'whitespace-nowrap font-medium opacity-0 transition-all duration-200 ease-in-out group-hover:opacity-100 lg:opacity-100',
			active && 'text-primary'
		)}>{data.label}</span
	>
</a>
