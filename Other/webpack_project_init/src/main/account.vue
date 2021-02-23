<template>
	<div>
		<h3>这是account组件</h3>

		<router-link to="/account/login">login</router-link>
		<router-link to="/account/register">register</router-link>
		<router-view></router-view>
	</div>
</template>

<script>
export default {}
</script>

<style lang="scss" scoped>
body{
	div{
		color: #f00;
	}
}
</style>