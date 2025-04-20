<template>
	<view class="Upload_page">
		<uni-card :is-shadow="false" is-full>
			<text class="illustration">Select a picture or take a photo and upload it to the currently bound service space.</text>
		</uni-card>
		<uni-section class="section-container" title="Choose from album" type="line" title-font-size="20px">
			<view class="add_image">
				<uni-file-picker limit="1" title="Only one file each time"></uni-file-picker>
			</view>
		</uni-section>
		 <uni-section class="section-container" title="Take a photo" type="line" title-font-size="20px">
			<view class="add_image">
				<button class="take-photo-button" type="primary" @click="takePhoto">Take Photo</button>
				<view class="preview-image-container">
					<image v-if="imagePath" :src="imagePath" mode="aspectFit"></image>
				</view>
			</view>
		</uni-section>
		<uni-section class="audio-section" title="Audio of Image Content" type="line" title-font-size="20px">
			<view class="audio-container" v-if="voicePath">
				<audio class="audio-bar" :src="voicePath" controls="true"></audio>
			</view>
		</uni-section>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				imagePath: '',
				voicePath: ''
			};
		},
		methods: {
			takePhoto: function(e) {
				uni.chooseImage({
					count:1,
					sizeType:['original', 'compressed'],
					sourceType:['camera'],
					success: (res) => {
						this.imagePath = res.tempFilePaths[0];
						console.log("Image Temporary Path: ", JSON.stringify(res.tempFilePaths));
					},
					fail: (err) => {
						console.error("Failed to take photo", JSON.stringify(err));
					}
				})
			}
		}
	}
</script>

<style lang="scss">
	page{
		justify-content: center;
		min-height: 100vh;
		background-color: #f0f0f0;
	}
	.illustration{
		font-size: 16px;
	}
	.add_image{
		padding: 10px;
		.take-photo-button{
			margin: 10px;
		}
		.preview-image-container{
			display: flex;
			justify-content: center;
			align-items: center;
		}
	}
	.audio-container{
		display: flex;
		justify-content: center;
		align-items: center;
		margin: 10px;
	}
</style>
