<template>
    <view>
        <!-- scroller image selection session -->
        <view class="section-container">
            <text class="section-title"> Click to select from Scroller </text>
        </view>
        <scroll-view class="scroll" scroll-x="true" show-scrollbar="true">
            <view class="scroll-group-H">
                <view class="scroll-item" v-for="(scrollerImg, index) in scrollerImages" :key="index">
                    <image :src="scrollerImg.src" mode="aspectFit" @click="showScrollerImageInfo(scrollerImg)"></image>
                </view>
            </view>
        </scroll-view>

        <!-- scroller image selected show captioned text & transformed voice -->
        <view class="section-container" v-if="selectedScrollerImageInfo">
            <text class="section-title"> See Scroller Image Description </text>
        </view>
        <uni-card class="image-info" v-if="selectedScrollerImageInfo" :cover="selectedScrollerImageInfo.src">
            <view class="select-image-text">
                <text>{{selectedScrollerImageInfo.text}}</text>
            </view>
            <view class="select-image-audio">
                <button @click="playAudio(selectedScrollerImageInfo.audio)" type="primary">Play Audio</button>
            </view>
        </uni-card>

        <!-- swiper image selection session -->
        <view class="section-container">
            <text class="section-title"> Click to select from Swiper </text>
        </view>
        <swiper class="swiper" autoplay="true" circular="true" interval="2000" indicator-dots="true">
            <swiper-item class="swiper-item" v-for="(swiperImg, index) in swiperImages" :key="index">
                <image :src="swiperImg.src" mode="aspectFit" @click="showSwiperImageInfo(swiperImg)"></image>
            </swiper-item>
        </swiper>

        <!-- swiper image selected show captioned text & transformed voice -->
        <view class="section-container" v-if="selectedSwiperImageInfo">
            <text class="section-title"> See Swiper Image Description </text>
        </view>
        <uni-card class="image-info" v-if="selectedSwiperImageInfo" :cover="selectedSwiperImageInfo.src">
            <view class="select-image-text">
                <text>{{selectedSwiperImageInfo.text}}</text>
            </view>
            <view class="select-image-audio">
                <button @click="playAudio(selectedSwiperImageInfo.audio)" type="primary">Play Audio</button>
            </view>
        </uni-card>

        <!-- Voting text box  -->
        <view class="section-container">
            <text class="section-title"> Click to see hidden text </text>
        </view>
        <view class="uni-padding-wrap uni-common-mt">
            <view class="text-box" scroll-y="true">
                <text>{{text}}</text>
            </view>
            <view class="buttons">
                <button class="line-button" type="primary" :disabled="!canAdd" @click="add">Add Text</button>
                <button class="line-button" type="warn" :disabled="!canRemove" @click="remove">Remove Text</button>
            </view>
        </view>

        <view style="height: 100rpx;"></view>
    </view>
</template>

<script>
export default {
    data() {
        return {
            // text lines for voting, to show in bottom text box
            title: 'text',
            texts: [
                'ELEC4544 Group Project: Group 6 is the best!',
                'Group 6 YuYueke & ZhaoWenzhe!',
                'Vote for us!',
                'Vote for us!',
                'Vote for us!',
                'Thank you!'
            ],
            text: '',
            canAdd: true,
            canRemove: false,
            extraLine: [],

            // scroller images objects
            scrollerImages: [
                { src: '/static/images/Doraemon.jpg', text: 'a cartoon character with a heart on his chest', audio: 'doraemon_audio_url' },
                { src: '/static/images/HelloKitty.jpg', text: 'hello kitty clipart hello kitty clipart hello kitty clipart', audio: 'hellokitty_audio_url' },
                { src: '/static/images/winnie_friends.jpg', text: 'winnie the poo and friends', audio: 'winnie_audio_url' },
                { src: '/static/images/cartoon_monsters.jpg', text: 'two dinosaurs sitting around a campfire', audio: 'monsters_audio_url' }
            ],
            // swiper images objects
            swiperImages: [
                { src: '/static/images/NewYorker_1.jpg', text: 'a man in a suit is standing next to a giant piano', audio: 'newyorker1_audio_url' },
                { src: '/static/images/NewYorker_2.jpg', text: 'a man standing in front of a painting', audio: 'newyorker2_audio_url' },
                { src: '/static/images/NewYorker_3.jpg', text: 'a woman sits at a table with a man who is talking to her', audio: 'newyorker3_audio_url' },
                { src: '/static/images/NewYorker_4.jpg', text: 'a cartoon drawing of a man in a cloak and a woman in a cloak', audio: 'newyorker4_audio_url' }
            ],
            // selected scroller image information 
            selectedScrollerImageInfo: null,
            // selected swiper image information 
            selectedSwiperImageInfo: null
        }
    },
    methods: {
        add: function (e) {
            this.extraLine.push(this.texts[this.extraLine.length % 6]);
            this.text = this.extraLine.join('\n');
            this.canAdd = this.extraLine.length < 6;
            this.canRemove = this.extraLine.length > 0;
        },
        remove: function (e) {
            if (this.extraLine.length > 0) {
                this.extraLine.pop();
                this.text = this.extraLine.join('\n');
                this.canAdd = this.extraLine.length < 6;
                this.canRemove = this.extraLine.length > 0;
            }
        },
        // tap scroller image to show image information
        showScrollerImageInfo(image) {
            this.selectedScrollerImageInfo = image;
        },
        // tap swiper image to show image information
        showSwiperImageInfo(image) {
            this.selectedSwiperImageInfo = image;
        },
        // tap button to listen the transformed image content audio
        playAudio(audioUrl) {
            const innerAudioContext = uni.createInnerAudioContext();
            innerAudioContext.src = audioUrl;
            innerAudioContext.play();
        }
    }
}
</script>

<style lang="scss">
page {
    justify-content: center;
    min-height: 100vh;
    background-color: #f0f0f0;
}

.text-box {
    margin-bottom: 40rpx;
    padding: 40rpx 0;
    display: flex;
    min-height: 300rpx;
    background-color: #ffffff;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-size: 30rpx;
    color: #353535;
    line-height: 1.8;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.buttons {
    display: flex;
    justify-content: center;
}

.line-button {
    margin: 10px;
    width: 80%;
}

.scroll {
    .scroll-group-H {
        white-space: nowrap;
        .scroll-item {
            display: inline-block;
            margin: 10px;
            border: 1px solid rgba(0, 0, 50, 0.2);
            border-radius: 12px;
            box-shadow: 12px 12px 2px 1px rgba(0, 0, 50, 0.2);
        }
    }
}

.swiper {
    height: 500rpx;
    .swiper-item {
        image {
            width: 100%;
            height: 500rpx;
        }
        background-color: white;
        border-radius: 16px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
    }
}

.section-container {
    .section-title {
        display: block;
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-size: 28px;
        color: #4a4a4a;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 10px;
    }
}

.scroll-item:hover {
    transform: scale(1.05);
    transition: transform 0.3s ease-in-out;
}

.image-info {
    margin-top: 20px;
    padding: 20px;
    background-color: #ffffff;
    border: 1px solid #e0e0e0;
    // border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
    text-align: center;
    .select-image-text {
        margin: 10px;
    }
}
</style>    