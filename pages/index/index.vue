<template>
	<view>
		<page-head :title="title"></page-head>
		<text class="section-title"> Select from Scroller </text>
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
		
		<text class="section-title"> Select from Swiper </text>
		<swiper class="swiper" autoplay="true" circular="true" interval="2000" indicator-dots="true">
			<swiper-item class="swiper-item">
				<image src="/static/images/NewYorker_1.jpg" mode="aspectFit"></image>
			</swiper-item>
			<swiper-item class="swiper-item">
				<image src="/static/images/NewYorker_2.jpg" mode="aspectFit"></image>
			</swiper-item>
			<swiper-item class="swiper-item">
				<image src="/static/images/NewYorker_3.jpg" mode="aspectFit"></image>
			</swiper-item>
			<swiper-item class="swiper-item">
				<image src="/static/images/NewYorker_4.jpg" mode="aspectFit"></image>
			</swiper-item>
		</swiper>
		
		<text class="section-title"> Click to see hidden text </text>
		<view class="uni-padding-wrap uni-common-mt">
			<view class="text-box" scroll-y="true">
				<text>{{text}}</text>
			</view>
			<view class="uni-btn-v">
				<button type="primary" :disabled="!canAdd" @click="add">Add Text</button>
				<button type="warn" :disabled="!canRemove" @click="remove">Remove Text</button>
			</view>
		</view>
		
		<view style="height: 200rpx;"></view>
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
	.text-box {
		margin-bottom: 40rpx;
		padding: 40rpx 0;
		display: flex;
		min-height: 300rpx;
		background-color: #FFFFFF;
		justify-content: center;
		align-items: center;
		text-align: center;
		font-size: 30rpx;
		color: #353535;
		line-height: 1.8;
	}
	.scroll{
		.scroll-group-H{
			white-space: nowrap;
			.scroll-item{
				display: inline-block;
				margin-right: 20rpx;
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
		}
	}
	.section-title{
		display: block;
		text-align: center;
		font-size: 24px;
		font-weight: bold;
		margin-top: 10px;
		color: coral;
	}
</style>