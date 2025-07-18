<script lang="ts">
	import { onMount } from 'svelte';

	const themes = ['latte', 'frappe', 'macchiato', 'mocha', 'dark'];

	let currentTheme = 'macchiato';

	onMount(() => {
		const savedTheme = localStorage.getItem('theme');
		if (savedTheme && themes.includes(savedTheme)) {
			currentTheme = savedTheme;
		}
		document.documentElement.setAttribute('data-theme', currentTheme);
		localStorage.setItem('theme', currentTheme);
	});

	function toggleTheme() {
		const currentIndex = themes.indexOf(currentTheme);
		const nextIndex = (currentIndex + 1) % themes.length;
		currentTheme = themes[nextIndex];
		document.documentElement.setAttribute('data-theme', currentTheme);
		localStorage.setItem('theme', currentTheme);
	}
	function setTheme(theme: string) {
		if (themes.includes(theme)) {
			currentTheme = theme;
			document.documentElement.setAttribute('data-theme', currentTheme);
			localStorage.setItem('theme', currentTheme);
		}
	}
</script>

<select
	class="select select-bordered w-full max-w-xs"
	bind:value={currentTheme}
	on:change={() => setTheme(currentTheme)}
>
	{#each themes as theme}
		<option value={theme}>{theme}</option>
	{/each}
</select>
