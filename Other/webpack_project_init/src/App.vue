<template>
	<div>
		<h3>这是登陆组件，使用 .vue文件define</h3>

		<div>
			<mt-button type="default" icon="back">default</mt-button>
			<mt-button type="primary" @click="show">primary</mt-button>
			<mt-button type="danger">danger</mt-button>
		</div>

		<router-link to="/account">account</router-link>
		<router-link to="/list">list</router-link>

		<router-view></router-view>
	</div>
</template>

<script>
import { Toast } from 'mint-ui';

export default {
	methods: {
		show() {
			Toast({
				message:'aa',
				duration: 500
			})
		}
	}
}
</script>

<style lang="scss">
</style>