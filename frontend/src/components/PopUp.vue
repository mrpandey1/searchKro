<template>
  <q-card>
    <q-card-section>
      <div class="text-h5">{{query}}</div>

      <div v-for="(p,index) in data" :key="index">
          {{p}}
      </div>
    </q-card-section>
    <q-btn flat label="OK" color="primary" v-close-popup @click="close" />
  </q-card>
</template>

<script>
export default {
  props: ["query","data"],
  methods: {
    close() {
      this.$emit("close");
    },
  },
};
</script>

<style lang="scss" scoped>
</style>