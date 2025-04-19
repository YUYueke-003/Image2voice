<template>
    <view class="page-container">
        <view class="about_us">
            <view class="project-title">
                <text class="title">Image2Voice</text>
            </view>
            <view class="project-intro">
                <text class="body">This is a project designed to transform images into voices, with the goal of assisting:</text>
            </view>
            <view class="target-users">
                <text class="bullets">Disabled individuals</text> 
                <text class="bullets-body">in understanding visual content more effectively.</text>
            </view>
            <view class="target-users">
                <text class="bullets">Elderly individuals</text>
                <text class="bullets-body">who may struggle to view images clearly.</text>
            </view>
        </view>
        <view class="author-container">
            <view class="author-info">
                <text class="author-section-title">Developer Names: </text>
                <view class="author-list">
                    <text class="author-name" v-for="author in authors" :key="author.name">{{ author.name }}</text>
                </view>
                <text class="author-section-title">Developer Contact Infomation: </text>
                <view class="author-list">
                    <text class="author-email" v-for="author in authors" :key="author.email">{{ author.email }}</text>
                </view>
            </view>
        </view>
    </view>
</template>

<script>
    export default {
        data() {
            return {
                authors: [
                    {
                        name: 'YuYueke',
                        email: 'yuyueke@connect.hku.hk'
                    },
                    {
                        name: 'ZhaoWenzhe',
                        email: 'wayne66@connect.hku.hk'
                    }
                ]
            };
        }
    }
</script>

<style lang="scss">
    page {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        margin-top: 20px;
        min-height: 100vh;
        background-color: #f0f0f0;
    }

   .page-container {
        width: 90%;
        max-width: 600px;
    }

   .about_us {
        background: linear-gradient(135deg, #ffffff 0%, #f9f9f9 100%);
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        padding: 30px;
        transition: all 0.3s ease;
        margin-bottom: 20px;
    }

   .about_us:hover {
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
        transform: translateY(-5px);
    }

   .project-title {
        text-align: center;
        margin-bottom: 20px;
    }

   .title {
        font-size: 34px;
        font-weight: bold;
        color: rosybrown;
    }

   .project-intro {
        margin-bottom: 20px;
    }

   .body {
        font-size: 20px;
        line-height: 1.6;
    }

   .target-users {
        margin-bottom: 20px;
    }

   .bullets {
        font-size: 20px;
        font-weight: bold;
        color: black;
    }

   .bullets-body {
        font-size: 20px;
        line-height: 1.6;
        margin-bottom: 10px;
        margin-left: 6px;
    }

   .author-container {
        background: linear-gradient(135deg, #ffffff 0%, #f9f9f9 100%);
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        padding: 30px;
        transition: all 0.3s ease;
    }

   .author-container:hover {
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
        transform: translateY(-5px);
    }

   .author-info {
        font-size: 16px;
        line-height: 1.5;
    }

   .author-section-title {
        font-size: 16px;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
        display: block;
    }

   .author-list {
        margin-bottom: 20px;
    }

   .author-name,
   .author-email {
        display: block;
        margin-bottom: 5px;
    }
</style>    