<script setup lang="ts">
import { Bold } from 'lucide-vue-next'
</script>

<template>
    <div class="flex h-screen">
        <main class="container m-auto flex justify-center">
            <Carousel class="max-w-5xl flex-grow">
                <CarouselContent>
                    <CarouselItem>
                        <Card>
                            <CardContent class="flex h-[75vh] items-center justify-center p-6 bg-gray-100">
                                <Toggle><Bold />American</Toggle>
                            </CardContent>
                        </Card>
                    </CarouselItem>
                    <CarouselItem>
                        <Card>
                            <CardContent class="flex h-[75vh] items-center justify-center p-6 bg-gray-100">
                                <CarouselNextButton />
                            </CardContent>
                        </Card>
                    </CarouselItem>
                </CarouselContent>
                <CarouselNext />
                <CarouselPrevious />
            </Carousel>
        </main>
    </div>
</template>
