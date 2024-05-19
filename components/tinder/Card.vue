<script setup lang="ts">
import interact from "interactjs";

const props = defineProps<{
    current: boolean,
    fullName: string,
    picture: string,
    rating: number,
    approved: boolean,
}>();
const propRefs = toRefs(props);

const emit = defineEmits(["draggedActive", "draggedThreshold", "draggedEnded"]);

const card = ref(null);

const threshold = window.innerWidth / 3;
const maxRotation = 20;

const showing = ref(true);
const maxStars = ref(5);
const animating = ref(true);
const position = reactive({ x: 0, y: 0, rotation: 0 });
const icon = reactive({ opacity: 0, type: null });

const imageString = computed(() => 'url(' + props.picture + ')');
const transformString = computed(() => {
    if (animating.value === false || props.approved !== null) {
        const x = position.x;
        const y = position.y;
        const rotate = position.rotation;
        return 'translate3D(' + x + 'px, ' + y + 'px, 0) rotate(' + rotate + 'deg)';
    }
    else {
        return "";
    }
});

watch(propRefs.approved, () => {
    if (props.approved !== null) {

        // Remove interact listener to prevent further dragging
        interact(card.value).unset();
        animating.value = true;

        /*
            Move card off-screen in direction of approve/reject status,
            then remove it from the DOM, thereby adjusting the CSS
            nth-child selectors.
        */

        const x = window.innerWidth + (window.innerWidth / 2) + card.value.offsetWidth;

        if (props.approved === true) {
            position.x = x;
            position.rotation = maxRotation;
            icon.type = 'approve';
        }
        else if (approved === false) {
            position.x = -x;
            position.rotation = -maxRotation;
            icon.type = 'reject';
        }

        icon.opacity = 1;

        setTimeout(function() {
            self.showing = false;
        }, 200);

    }
});

interact(card.value).draggable({
    inertia: false,
    onstart: function() {
        animating.value = false;
    },
    onmove: function(event) {
        /*
            Calculate new x and y coordinate values from the local value and
            the event object value. Also adjust element rotation transformation
            based on proximity to approve/reject threshold.
        */

        const x = (position.x || 0) + event.dx;
        const y = (position.y || 0) + event.dy;

        let rotate = maxRotation * (x / threshold);

        if (rotate > maxRotation) {
            rotate = maxRotation;
        }
        else if (rotate < -maxRotation) {
            rotate = -maxRotation;
        }

        position.x = x;
        position.y = y;
        position.rotation = rotate;

        /*
            Change icon image type based on drag direction and adjust opacity
            from 0-1 based on current rotation amount. Also emit an event to
            show/hide respective button below cards during dragging.
        */

        if (rotate > 0) {
            icon.type = 'approve';
        }
        else if (rotate < 0) {
            icon.type = 'reject';
        }

        const opacityAmount = Math.abs(rotate) / maxRotation;

        icon.opacity = opacityAmount;
        emit('draggedActive', icon.type, opacityAmount);
    },
    onend: function(event) {
        /*
            Check if card has passed the approve/reject threshold and emit approval
            value change event, otherwise reset card and icon to default values.
        */

        animating.value = true;

        if (position.x > threshold) {
            emit('draggedThreshold', true);
            icon.opacity = 1;
        }
        else if (position.x < -threshold) {
            emit('draggedThreshold', false);
            icon.opacity = 1;
        }
        else {
            position.x = 0;
            position.y = 0;
            position.rotation = 0;
            icon.opacity = 0;
        }

        emit('draggedEnded');
    }
});
</script>

<template>
    <div v-if="showing" class="card" ref="card"
        :class="{ animated: animating, current: current }"
        :style="{ transform: transformString }">
        <div class="image"
            v-bind:style="{ backgroundImage: imageString }">
            <div class="image-icon"
                v-bind:class="icon.type"
                v-bind:style="{ opacity: icon.opacity }">
            </div>
        </div>
        <h1 class="name">{{ fullName }}</h1>
        <div class="stars">
            <div v-for="(star, index) in maxStars"
                v-bind:class="[(rating > index) ? 'star-active' : 'star-inactive']">
            </div>
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