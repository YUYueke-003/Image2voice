<template>
	<view>
		<view class="section-container">
			<text class="section-title"> Select from Scroller </text>
		</view>
		<scroll-view class="scroll" scroll-x="true" show-scrollbar="true">
			<view class="scroll-group-H">
				<view class="scroll-item">
					<image src="/static/images/Doraemon.jpg" mode="aspectFit"></image>
				</view>
				<view class="scroll-item">
					<image src="/static/images/HelloKitty.jpg" mode="aspectFit"></image>
				</view>
				<view class="scroll-item">
					<image src="/static/images/winnie_friends.jpg" mode="aspectFit"></image>
				</view>
				<view class="scroll-item">
					<image src="/static/images/cartoon_monsters.jpg" mode="aspectFit"></image>
				</view>
			</view>
		</scroll-view>
		
		<view class="section-container">
			<text class="section-title"> Select from Swiper </text>
		</view>
		<swiper class="swiper" autoplay="true" circular="true" interval="2000" indicator-dots="true">
			<swiper-item class="swiper-item" v-for="item in [1,2,3,4]">
				<image :src="'/static/images/NewYorker_'+item+'.jpg'" mode="aspectFit"></image>
			</swiper-item>
		</swiper>
		
		<view class="section-container">
			<text class="section-title"> Click to see hidden text </text>
		</view>
		<view class="uni-padding-wrap uni-common-mt">
			<view class="text-box" scroll-y="true">
				<text>{{text}}</text>
			</view>
			<view class="uni-btn-v">
				<button type="primary" :disabled="!canAdd" @click="add">Add Text</button>
				<button type="warn" :disabled="!canRemove" @click="remove">Remove Text</button>
			</view>
		</view>
		
		<view style="height: 100rpx;"></view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
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
				extraLine: []
			}
		},
		methods: {
			add: function(e) {
				this.extraLine.push(this.texts[this.extraLine.length % 6]);
				this.text = this.extraLine.join('\n');
				this.canAdd = this.extraLine.length < 6;
				this.canRemove = this.extraLine.length > 0;
			},
			remove: function(e) {
				if (this.extraLine.length > 0) {
					this.extraLine.pop();
					this.text = this.extraLine.join('\n');
					this.canAdd = this.extraLine.length < 6;
					this.canRemove = this.extraLine.length > 0;
				}
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
	.scroll{
		.scroll-group-H{
			white-space: nowrap;
			.scroll-item{
				display: inline-block;
				margin: 10px;
				border: 1px solid rgba(0, 0, 50, 0.2);
				border-radius: 12px;
				box-shadow: 12px 12px 2px 1px rgba(0, 0, 50, 0.2);
			}
		}
	}
	.swiper{
		height: 500rpx;
		.swiper-item{
			image{
				width: 100%;
				height: 500rpx;
			}
			background-color: white;
			border-radius: 16px;
			box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
		}
	}
	.section-container{
		.section-title{
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
</style>