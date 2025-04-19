<template>
	<view class="about_us">
		<text class="title">Image2Voice</text>
		<view class="spacer"></view>
		<text class="body">This	is a project designed to transform images into voices, with the goal of assisting:</text>
		<view class="spacer"></view>
		<text class="bullets">Disabled individuals</text> 
		<text class="bullets-body">in understanding visual content more effectively.</text>
		<view class="spacer"></view>
		<text class="bullets">Elderly individuals</text>
		<text class="bullets-body">who may struggle to view images clearly.</text>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
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

   .about_us {
        background: linear-gradient(135deg, #ffffff 0%, #f9f9f9 100%);
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        padding: 30px;
        width: 80%;
        max-width: 600px;
        transition: all 0.3s ease;

        &:hover {
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.15);
            transform: translateY(-5px);
        }

       .title {
            font-size: 34px;
            font-weight: bold;
            text-align: center;
            display: block;
            margin-top: 20px;
            margin-bottom: 20px;
            color: rosybrown;
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

       .body {
            font-size: 20px;
            line-height: 1.6;
            margin-bottom: 10px;
        }

       .spacer {
            height: 10px;
        }
    }
</style>
    