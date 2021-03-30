<template>
  <q-card style="min-width: 500px">
    <q-toolbar>
      <q-avatar rounded>
        <img
          src="https://www.flaticon.com/svg/vstatic/svg/2820/2820207.svg?token=exp=1616319960~hmac=5367e52048da4674fd1e518fa84ca2fe"
        />
      </q-avatar>

      <q-toolbar-title
        ><span class="text-weight-bold" style="font-size: 1.42rem"
          >Similar Questions</span
        ></q-toolbar-title
      >
      <q-btn flat round dense icon="close" v-close-popup />
    </q-toolbar>

    <q-card-section>
      <div v-if="!paraphrasing_available">
        <center>
          <q-circular-progress
            indeterminate
            size="50px"
            color="light-blue-9"
            class="q-ma-md"
          />
        </center>
      </div>
      <div
        v-else
        v-for="(p, index) in paraphrasing_data"
        :key="index"
        class="q-mb-md"
        style="font-size: 1.02rem"
        @click="getParaphrase(p)"
      >
        {{ p }}
        <hr style="opacity: 0.25" />
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  props: ["query"],
  data() {
    return {
      paraphrasing_available: false,
      paraphrasing_data: null,
    };
  },
  mounted() {
    console.log(this.query);
    this.getParaphrase();
  },
  methods: {
    close() {
      this.$emit("close");
    },
    async getParaphrase() {
      const url = `http://localhost:8000/rewrite?query=${this.query}`;
      // console.log(url);
      const para = await this.$axios.get(url);
      this.paraphrasing_data = para.data.response;
      // console.log(this.paraphrasing_data);
      this.paraphrasing_available = para.data != null;
    },
  },
};
</script>

<style lang="scss" scoped>
</style>