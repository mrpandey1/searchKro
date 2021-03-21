<template>
  <q-card style="min-width:500px">
    <q-toolbar>
      <q-avatar rounded>
        <img src="https://www.flaticon.com/svg/vstatic/svg/2820/2820207.svg?token=exp=1616319960~hmac=5367e52048da4674fd1e518fa84ca2fe" />
      </q-avatar>

      <q-toolbar-title
        ><span class="text-weight-bold" style="font-size:1.42rem">In other words</span></q-toolbar-title
      >
      <q-btn flat round dense icon="close" v-close-popup />
    </q-toolbar>

    <q-card-section>
      <div v-for="(p, index) in data" :key="index" class="q-mb-md" style="font-size:1.02rem">
        {{ p }}
        <hr style="opacity:0.25">
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  props: ["query", "data"],
  methods: {
    close() {
      this.$emit("close");
    },
  },
};
</script>

<style lang="scss" scoped>
</style>