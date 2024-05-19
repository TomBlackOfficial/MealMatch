<template>
    <div class="LandingPage w-full h-[1403px] relative bg-white">
        <div class="Rectangle23788 w-full h-[742px] left-0 top-[661px] absolute bg-pink-50"></div>
        <div class="Rectangle23784 w-full h-[727px] left-0 top-0 absolute bg-rose-100"></div>
        <img class="Mascot1RedUpscaled1 w-[729px] h-[729px] left-[704px] top-[-13px] absolute" src="~/assets/images/panda.png" />
        <div class="PickUp w-[1390px] py-2.5 left-[71px] top-[592px] absolute rounded-[10px] justify-between items-start inline-flex">
            <div class="Catalog1 w-[304px] h-[264px] relative cursor-pointer" @click="navigateTo('/')">
                <div class="Rectangle23793 w-[304px] h-[264px] left-0 top-0 absolute bg-stone-50/opacity-70 rounded-[25px] shadow border-2 border-white/opacity-50 backdrop-blur-[20px]"></div>
                <div class="Name w-[250px] h-[46px] left-[27px] top-[195px] absolute flex-col justify-start items-start gap-1 inline-flex">
                    <div class="Breakfast self-stretch grow shrink basis-0 text-center text-stone-800 text-3xl font-extrabold font-['Plus Jakarta Sans'] leading-[45px]">Breakfast</div>
                </div>
                <img class="Breakfast3 w-[250px] h-[250px] left-[27px] top-[-51px] absolute" src="~/assets/images/pancakes.png" />
            </div>
            <div class="Catalog2 w-[304px] h-[264px] relative cursor-pointer" @click="navigateTo('/')">
                <div class="Rectangle23793 w-[304px] h-[264px] left-0 top-0 absolute bg-stone-50/opacity-70 rounded-[25px] shadow border-2 border-white/opacity-50 backdrop-blur-[20px]"></div>
                <div class="Name w-[250px] h-[46px] left-[27px] top-[195px] absolute flex-col justify-start items-start gap-1 inline-flex">
                    <div class="Lunch self-stretch grow shrink basis-0 text-center text-stone-800 text-3xl font-extrabold font-['Plus Jakarta Sans'] leading-[45px]">Lunch</div>
                </div>
                <img class="Breakfast3 w-[250px] h-[250px] left-[27px] top-[-51px] absolute" src="~/assets/images/sandwich.png" />
            </div>
            <div class="Catalog3 w-[304px] h-[264px] relative cursor-pointer" @click="navigateTo('/')">
                <div class="Rectangle23793 w-[304px] h-[264px] left-0 top-0 absolute bg-stone-50/opacity-70 rounded-[25px] shadow border-2 border-white/opacity-50 backdrop-blur-[20px]"></div>
                <div class="Name w-[250px] h-[46px] left-[27px] top-[195px] absolute flex-col justify-start items-start gap-1 inline-flex">
                    <div class="Dinner self-stretch grow shrink basis-0 text-center text-stone-800 text-3xl font-extrabold font-['Plus Jakarta Sans'] leading-[45px]">Dinner</div>
                </div>
                <img class="Breakfast3 w-[250px] h-[250px] left-[27px] top-[-51px] absolute" src="~/assets/images/steak.png" />
            </div>
            <div class="Catalog4 w-[304px] h-[264px] relative cursor-pointer" @click="navigateTo('/')">
                <div class="Rectangle23793 w-[304px] h-[264px] left-0 top-0 absolute bg-stone-50/opacity-70 rounded-[25px] shadow border-2 border-white/opacity-50 backdrop-blur-[20px]"></div>
                <div class="Name w-[250px] h-[46px] left-[27px] top-[195px] absolute flex-col justify-start items-start gap-1 inline-flex">
                    <div class="Dessert self-stretch grow shrink basis-0 text-center text-stone-800 text-3xl font-extrabold font-['Plus Jakarta Sans'] leading-[45px]">Dessert</div>
                </div>
                <img class="Breakfast3 w-[250px] h-[250px] left-[27px] top-[-51px] absolute" src="~/assets/images/cake.png" />
            </div>
        </div>
        <div class="NavBarTop w-full h-[145px] pl-[81px] pr-[1045px] pt-[37px] pb-[38px] left-0 top-0 absolute bg-white/opacity-0 justify-start items-center inline-flex">
            <img class="Asset12 w-[314px] h-[85px]" src="~/assets/images/MealMatch_LogoWide.png" />
        </div>
        <div class="Group40 h-[205px] left-[88px] top-[213px] absolute">
            <div class="FillOutOurSurveyInMinutesThenSwipeLeftOrRightOnCuratedMealsAndRecipesSuitedToYourCravingsAndDietaryRestrictions w-[534px] left-[1px] top-[153px] absolute opacity-40 text-stone-800 text-base font-normal font-['Baloo 2'] leading-relaxed">Your recipe wizard! Select your tastes, answer quick questions, and bam! Personalized recipes ready to save you time and tantalize your taste buds. Say hello to hassle-free meals with MealMatch!</div>
            <div class="TimeIsMoneyWhyWasteIt w-[574.66px] left-0 top-[30px] absolute text-yellow-950 text-[55px] font-normal font-['Baloo'] uppercase leading-[55px]">Time is money,<br/>Why waste it?</div>
        </div>
        <div class="Group39 w-full h-[245.75px] left-[79px] top-[997px] absolute">
            <div class="AnswerQuestions left-[38.24px] top-[135.15px] absolute text-center text-stone-800 text-2xl font-semibold font-['Plus Jakarta Sans'] leading-9">Answer questions</div>
            <div class="FillOutOurFastAndProprietarySurveyInJustMinutesSoWeCanBetterFitYourNeeds w-[276.48px] h-[62px] left-0 top-[183.75px] absolute text-center text-stone-800 text-sm font-normal font-['Plus Jakarta Sans'] leading-normal">Fill out our fast and proprietary survey in just minutes so we can better fit your needs.</div>
            <div class="Group34 w-[106px] h-[106px] left-[85.24px] top-0 absolute">
                <div class="Rectangle23787 w-[106px] h-[106px] left-0 top-0 absolute opacity-25 bg-orange-400 rounded-[30px]"></div>
            </div>
            <div class="Group36 w-[276.48px] h-[245.75px] left-[550px] top-0 absolute">
                <div class="PickARecipe left-[71.78px] top-[135.15px] absolute text-center text-stone-800 text-2xl font-semibold font-['Plus Jakarta Sans'] leading-9">Pick a recipe</div>
                <div class="SwipeLeftOrRightOnMealOptionsUntilYouFindAMatchForYourCravings w-[276.48px] h-[62px] left-0 top-[183.75px] absolute text-center text-stone-800 text-sm font-normal font-['Plus Jakarta Sans'] leading-normal">Swipe left or right on meal options until you find a match for your cravings.</div>
                <div class="Group35 w-[106px] h-[106px] left-[85.24px] top-0 absolute">
                    <div class="Rectangle23787 w-[106px] h-[106px] left-0 top-0 absolute opacity-25 bg-orange-400 rounded-[30px]"></div>
                    <div class="AntDesignCalendarFilled w-[45px] h-11 left-[75.50px] top-[31px] absolute origin-top-left rotate-180 justify-center items-center inline-flex"></div>
                </div>
            </div>
            <div class="Group36 w-[276.48px] h-[245.75px] left-[1086px] top-0 absolute">
                <div class="EnjoyYourMeal left-[54.78px] top-[135.15px] absolute text-center text-stone-800 text-2xl font-semibold font-['Plus Jakarta Sans'] leading-9">Enjoy your meal</div>
                <div class="NowSitBackRelaxAndEnjoyMealAndAllTheTimeYouSavedByUsingMealmatch w-[276.48px] h-[62px] left-0 top-[183.75px] absolute text-center text-stone-800 text-sm font-normal font-['Plus Jakarta Sans'] leading-normal">Now sit back, relax, and enjoy  meal and all the time you saved by using MealMatch.</div>
                <div class="Rectangle23787 w-[106px] h-[106px] left-[85.24px] top-0 absolute opacity-25 bg-orange-400 rounded-[30px]"></div>
            </div>
            <div class="BiCarFrontFill w-[47px] h-[49px] py-[6.12px] left-[1120.74px] top-[28.50px] absolute flex-col justify-center items-center inline-flex"></div>
        </div>
    </div>
</template>
<script setup lang="ts">
</script>