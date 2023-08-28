<script>
	import list from './elements.json';
	let store = list.reduce(
		(prev, curr) => {
			return { ...prev, [curr.id]: { clicked: false, id: [curr.id], d: [curr.d] } };
		},
		{ accent_circle: { clicked: false, id: 'accent_circle' } }
	);
	// let overlay = [];
	let stack = [];
	let gray = {
		display: 'inline',
		fill: 'none',
		'fill-opacity': 1,
		'stroke-width': 4,
		'stroke-linecap': 'round',
		'stroke-linejoin': 'bevel',
		'stroke-miterlimit': 1,
		'stroke-dasharray': 'none',
		'stroke-dashoffset': 0,
		'stroke-opacity': 1,
		'paint-order': 'normal'
	};
	function clickme(e) {
		const id = e.target.id;
		const clicked = store[id].clicked;
		store[id].clicked = !clicked;
		// if (!clicked) {
		// 	overlay = [...overlay, { id: e.target.id, d: e.target.d }];
		// } else {
		// 	overlay = overlay.map((x) => {
		// 		if (x.id != id) return x;
		// 	});
		// }
		// console.log(overlay);
	}

	function reset() {
		Object.keys(store).map((x) => {
			store[x].clicked = false;
		});
	}

	function submit() {
		const arr = [];
		Object.keys(store).map((x) => {
			if (store[x].clicked) {
				arr.push(x);
			}
		});
		console.log(stack);
		arr.length != 0 ? (stack = [...stack, arr]) : null;
	}
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<div display="flex">
	{#each stack as elem}
		<svg
			width="12mm"
			height="15mm"
			viewBox="0 0 120 150"
			version="1.1"
			id="svg1"
			xmlns="http://www.w3.org/2000/svg"
			xmlns:svg="http://www.w3.org/2000/svg"
		>
			{#each elem as id}
				{#if id == 'accent_circle'}
					<circle
						{...gray}
						fill="#000000"
						fill-opacity="0"
						{id}
						stroke="#000000"
						cx="60"
						cy="130"
						r="8"
					/>
				{:else}
					<path {...gray} d={store[id].d} stroke="#000000" />
				{/if}
			{/each}
			<path {...gray} d="M 9.9255908,75 H 110.07441" id="base" stroke="#000000" />
		</svg>
	{/each}
</div>

<svg
	width="120mm"
	height="150mm"
	viewBox="0 0 120 150"
	version="1.1"
	id="svg1"
	xmlns="http://www.w3.org/2000/svg"
	xmlns:svg="http://www.w3.org/2000/svg"
>
	<g>
		{#each list as elem}
			<path
				on:click={clickme}
				{...gray}
				{...elem}
				stroke={store[elem.id].clicked ? '#000000' : '#b4b4b4'}
			/>
		{/each}
		<path {...gray} d="M 9.9255908,75 H 110.07441" id="base" stroke="#000000" />
		<circle
			on:click={clickme}
			{...gray}
			fill="#000000"
			fill-opacity="0"
			id="accent_circle"
			stroke={store['accent_circle'].clicked ? '#000000' : '#b4b4b4'}
			cx="60"
			cy="130"
			r="8"
		/>
	</g>
	<!-- ! Figure this out -->
	<!-- <g>
		{#each overlay as elem}
			{#if elem.id == 'accent_circle'}
				<circle
					{...gray}
					fill="#000000"
					fill-opacity="0"
					id={elem.id}
					stroke="#000000"
					cx="60"
					cy="130"
					r="8"
				/>
			{:else}
				<path on:click={clickme} {...gray} {...elem} stroke="#000000" />
			{/if}
		{/each}
	</g> -->
</svg>

<button on:click={reset}>Reset</button>
<button on:click={submit}>Submit</button>

<style>
</style>
