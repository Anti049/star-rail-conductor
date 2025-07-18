<script lang="ts">
	import Link from './Link.svelte';

	let links: (LinkData | Separator)[] = [
		// Home
		{
			label: 'Home',
			href: '/',
			icon: '/icons/menu/NoviceCapsuleShopIcon.png'
		},
		// Banners
		{
			label: 'Banners',
			href: '/banners',
			icon: '/icons/menu/NoviceDrawcardIcon.png'
		},
		// To-Do List
		{
			label: 'To-Do List',
			href: '/todo',
			icon: '/icons/menu/NoviceAssignmentIcon.png'
		},
		{}, // Separator
		// Characters
		{
			label: 'Characters',
			href: '/characters',
			icon: '/icons/menu/NoviceAvatarIcon.png'
		},
		// Tier List
		{
			label: 'Tier List',
			href: '/characters/tier-list',
			icon: '/icons/menu/NoviceTeamIcon.png'
		},
		// Light Cones
		// {
		// 	label: 'Light Cones',
		// 	href: '/light-cones',
		// 	icon: '/icons/menu/inventory/light_cones.png',
		// },
		// Relics
		// {
		// 	label: 'Relics',
		// 	href: '/relics',
		// 	icon: '/icons/menu/inventory/relics.png',
		// },
		// Items
		{
			label: 'Items',
			href: '/items',
			icon: '/icons/menu/NoviceInventoryIcon.png'
		},
		// Activities
		{
			label: 'Activities',
			href: '/activities',
			icon: '/icons/menu/NoviceActivityIcon.png'
		},
		// Achievements
		{
			label: 'Achievements',
			href: '/achievements',
			icon: '/icons/menu/NoviceAchievementIcon.png'
		},
		// Quests
		{
			label: 'Quests',
			href: '/quests',
			icon: '/icons/menu/NoviceQuestIcon.png'
		},
		// Interactive Maps
		{
			label: 'Interactive Maps',
			href: '/maps',
			icon: '/icons/menu/NoviceMapIcon.png'
		},
		// Redemption Codes
		{
			label: 'Redemption Codes',
			href: '/codes',
			icon: '/icons/menu/NoviceMailsIcon.png'
		}
	];
</script>

<div
	class="surface-container-low border-r-surface-container-highest group flex h-full w-20 flex-col items-center gap-2 border-r p-2 transition-all duration-200 ease-in-out hover:w-64 lg:w-64"
>
	<Link
		data={{
			label: 'Profile',
			href: '/profile',
			icon: '/images/path/large/trailblaze.png'
		}}
	/>
	<div class="h-0.75 surface-container-high w-[calc(100%-theme(spacing.4))] rounded-full"></div>
	{#each links as link}
		{#if 'label' in link}
			<Link data={link} />
		{:else}
			<div class="h-0.75 surface-container-high w-[calc(100%-theme(spacing.4))] rounded-full"></div>
		{/if}
	{/each}
	<div class="flex-1"></div>
	<Link
		data={{
			label: 'Settings',
			href: '/settings',
			icon: '/icons/menu/NoviceSettingsIcon.png'
		}}
	/>
</div>
