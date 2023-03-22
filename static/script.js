async function fetchData(city) {
	const response = await fetch(`/data?city=${city}`);
	const data = await response.json();
	return data;
}

function createWordElement(text, size, color) {
	const span = document.createElement("span");
	span.textContent = text;
	span.style.fontSize = Math.min(size, 48) + "px";
	span.style.color = color;
	span.style.animationName = "fadeInOut";
	span.style.animationDelay = Math.random() * 3 + "s";
	return span;
}

function generateColor() {
	const hue = Math.floor(Math.random() * 360);
	return `hsl(${hue}, 70%, 50%)`;
}

async function createWordCloud(city) {
	const location = document.getElementById("location");
	const loading = document.getElementById("loading");
	const city_input = document.getElementById("city-input");
	loading.style.display = "flex";
	const data = await fetchData(city);
	const container = document.getElementById("word-cloud");

	loading.style.display = "none";
	location.textContent = `Trends in ${city}`;
	city_input.value = "";

	container.innerHTML = "";
	data.forEach((item) => {
		const size = Math.floor((item.tweet_volume / 10000) * 3 + 16);
		const color = generateColor();
		const wordElement = createWordElement(item.name, size, color);
		container.appendChild(wordElement);
	});
}

const cityForm = document.getElementById("city-form");
const cityInput = document.getElementById("city-input");
cityForm.addEventListener("submit", (event) => {
	event.preventDefault();
	const city = cityInput.value;
	createWordCloud(city);
});
