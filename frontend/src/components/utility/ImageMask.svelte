<script lang="ts">
	import clsx from 'clsx';

	let { class: className, image }: { class: string; image: string } = $props();
</script>

<div
	style="mask-image: url('{image}'); -webkit-mask-image: url('{image}');"
	class={clsx(className, 'mask-contain mask-no-repeat mask-center')}
></div>
