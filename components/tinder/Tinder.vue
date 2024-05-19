<script setup lang="ts">
const tinder = ref(null);

const isLoading = ref(true);
const cards = reactive({
    data: null,
    index: 0,
    max: 10,
});

function getData() {
    isLoading.value = true;
    cards.data = null;

    const request = new XMLHttpRequest();
    request.open('GET', 'https://randomuser.me/api/?results=' + cards.max, true);

    request.onload = function() {
        const response = JSON.parse(request.responseText).results;

        const data = response.map(function(object) {

            /*
                Construct a new array with objects containing only
                the relevent data from the original response data
            */

            return {
                name: object.name.first + ' ' + object.name.last,
                picture: object.picture.large,
                rating: Math.floor(Math.random() * 5 + 1),
                approved: null
            };

        });

        // Fake delay for purposes of demonstration
        setTimeout(function() {
            cards.data = data;
            cards.index = 0;
            isLoading.value = false;
        }, 500);

    };

    request.send();
}

function setApproval(approval: boolean) {
    cards.data[cards.index].approved = approval;
    cards.index++;

    if (cards.index >= cards.data.length) {
        getData();
    }
}

getData();
</script>

<template>
    <div ref="tinder">
        <div v-show="isLoading" class="loading">
            <div class="loading-icon"></div>
        </div>

        <div class="card-container">
            <TinderCard v-for="(card, index) in cards.data" :key="index"
                :current="index === cards.index"
                :fullName="card.name"
                :picture="card.picture"
                :rating="card.rating"
                :approved="card.approved"
                :draggedThreshold="setApproval">
            </TinderCard>
        </div>
    </div>
</template>

<style scoped>
/* CONSTANTS */

html {
	box-sizing: border-box;
}

body {
	min-width: 320px;
	font-family: "Nunito", sans-serif;
	font-weight: 700;
	color: #444444;
	overflow: hidden;
	background: #F3F3F3;
	text-rendering: optimizeLegibility;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	-moz-font-feature-settings: "liga" on;
}

*,
*:before,
*:after {
	margin: 0;
	padding: 0;
	box-sizing: inherit;
}

a {
	color: inherit;
}

aside,
section,
main,
nav,
header,
footer {
	display: block;
}



/* MAIN */

#app {
	position: relative;
	width: 100vw;
	height: 100vh;
}

.card-container {
	position: relative;
	top: 50%;
	margin: 0 auto 0 auto;
	width: 420px;
	height: calc(570px);
	transform: translateY(-50%);
}

/* LOADING */
.loading {
	z-index: 10;
	position: fixed;
	width: 100%;
	height: 100%;
	background: rgba(240, 164, 53, 0.5);
}

.loading > .loading-icon {
	width: 125px;
	height: 125px;
    position: absolute;
	left: 50%;
	top: 50%;
	margin-left: -62.5px;
	margin-top: -62.5px;
}

.loading > .loading-icon:before,
.loading > .loading-icon:after {
	content: "";
	display: block;
    position: absolute;
	left: 50%;
	top: 50%;
	margin-left: -62.5px;
	margin-top: -62.5px;
    width: 125px;
	height: 125px;
	border-radius: 50%;
	border: 4px solid #FFFFFF;
}

.loading > .loading-icon:before {
	z-index: 0;
	animation: 1s pulse infinite linear;
}

.loading > .loading-icon:after {
	z-index: 10;
	background: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/617753/loading-default.jpg") center center no-repeat #FFFFFF;
	background-size: cover;
}

@-webkit-keyframes pulse {
	0% { opacity: 0; -webkit-transform: scale(0.8); }
	50% { opacity: 1; }
	100% { opacity: 0; -webkit-transform: scale(1.5); }
}

@-moz-keyframes pulse {
	0% { opacity: 0; -moz-transform: scale(0.8); }
	50% { opacity: 1; }
	100% { opacity: 0; -moz-transform: scale(1.5); }
}

@-ms-keyframes pulse {
	0% { opacity: 0; -ms-transform: scale(0.8); }
	50% { opacity: 1; }
	100% { opacity: 0; -ms-transform: scale(1.5); }
}

@-o-keyframes pulse {
	0% { opacity: 0; -o-transform: scale(0.8); }
	50% { opacity: 1; }
	100% { opacity: 0; -o-transform: scale(1.5); }
}

@keyframes pulse {
	0% { opacity: 0; transform: scale(0.8); }
	50% { opacity: 1; }
	100% { opacity: 0; transform: scale(1.5); }
}

/* CARD */

.card {
	pointer-events: none;
	z-index: 0;
	opacity: 0;
	left: 0;
	top: 0;
	position: absolute;
	padding: 15px 15px 30px 15px;
	width: 420px;
	height: 550px;
	border-radius: 8px;
	background: #FFFFFF;
	box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
	transform: translateY(30px) scale(0.94);
	transform-origin: 50% 100%;
	will-change: transform, opacity;
}

/*
	Cascade the cards by translation and scale based on
	their nth-child index
*/
.card:nth-child(1) {
    opacity: 1;
    z-index: 3;
    transform: translateY(0) scale(1);
}

.card:nth-child(2) {
    opacity: 1;
    z-index: 2;
    transform: translateY(10px) scale(0.98);
}

.card:nth-child(3) {
    opacity: 1;
    z-index: 1;
    transform: translateY(20px) scale(0.96);
}

.card.current {
	pointer-events: auto;
}

.card.animated {
	transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.card > .image {
	margin: 0 auto 30px 0;
	width: calc(420px - (15px * 2));
	height: calc(420px - (15px * 2));
    background: center center no-repeat transparent;
	background-size: contain;
}

.card > .image > .image-icon {
	position: relative;
	left: 50%;
	top: 50%;
	width: 200px;
	height: 200px;
	transform: translateX(-50%) translateY(-50%);
	background: center center no-repeat transparent;
	background-size: contain;
}

.card > .image > .image-icon.approve {
	background-image: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/617753/icon-approve.svg");
}

.card > .image > .image-icon.reject {
	background-image: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/617753/icon-reject.svg");
}

.card > .name {
	margin: 0 auto 30px 0;
	display: block;
	font-size: 24px;
	line-height: 24px;
	text-align: center;
	text-transform: capitalize;
}

.card > .stars {
	margin: 0 auto 0 auto;
	width: calc((25px * 5) + (25px * (5 - 1)));
}

.card > .stars:after {
	content: "";
	display: table;
	clear: both;
}

.card > .stars > .star-active,
.card > .stars > .star-inactive {
	float: left;
	margin-right: 25px;
	width: 25px;
	height: 25px;
    background: center center no-repeat transparent;
	background-size: contain;
}

.card > .stars > .star-active:last-child,
.card > .stars > .star-inactive:last-child {
	margin-right: 0;
}

.card > .stars > .star-active {
	background-image: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/617753/star-active.svg");
}

.card > .stars > .star-inactive {
	background-image: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/617753/star-inactive.svg");
}
</style>