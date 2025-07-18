<script lang="ts">
	import '../app.css';
	import ImageMask from '../components/utility/ImageMask.svelte';

	let { children } = $props();
</script>

<div class="surface flex h-full w-full flex-row">
	<div class="surface-container flex h-full w-20 flex-col gap-4 overflow-y-auto p-2">
		<div class="mask-abundance-large bg-wind aspect-square w-16"></div>
		<div class="mask-abundance-medium bg-wind aspect-square w-16"></div>
		<div class="mask-abundance-small bg-wind aspect-square w-16"></div>
		<ImageMask
			image="/images/path/large/remembrance.png"
			class="bg-on-surface hover:bg-primary aspect-square w-16 transition-colors duration-200 ease-in-out hover:cursor-pointer"
		/>
	</div>
	<div class="flex flex-1 flex-col gap-4 p-4">
		<img src="/images/rarity/Star5.png" alt="Star 5" class="h-16 w-80" />
		<ImageMask image="/images/rarity/Star5.png" class="bg-rarity-5 h-16 w-80" />
		<ImageMask image="/images/rarity/Star4.png" class="bg-rarity-4 h-16 w-80" />
		<ImageMask image="/images/rarity/Star3.png" class="bg-rarity-3 h-16 w-80" />
		<ImageMask image="/images/rarity/Star2.png" class="bg-rarity-2 h-16 w-80" />
		<ImageMask image="/images/rarity/Star1.png" class="bg-rarity-1 h-16 w-80" />
		<ImageMask image="/images/rarity/Star1.png" class="bg-rarity-0 h-16 w-80" />
		<div class="flex-1 overflow-y-auto">
			{@render children()}
		</div>
	</div>
</div>
