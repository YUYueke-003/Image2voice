<template>
	<view class="Upload_page">
		<uni-card :is-shadow="false" is-full>
			<text class="illustration">Select a picture or take a photo and upload it to the currently bound service space.</text>
		</uni-card>
		<uni-section title="Choose from album" type="line">
			<view class="add_image">
				<uni-file-picker limit="1" title="Only one file each time"></uni-file-picker>
			</view>
		</uni-section>
		 <uni-section title="Take a photo" type="line">
			<view class="add_image">
				<button class="take-photo-button" type="primary" @click="takePhoto">Take Photo</button>
				<!-- Add function of image preview -->
				<image class="preview" v-if="imagePath" :src="imagePath" mode="aspectFit"></image>
			</view>
		</uni-section>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				imagePath: ''
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
	.add_image{
		padding: 10px;
		.take-photo-button{
			
		}
	}
</style>
