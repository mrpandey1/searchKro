<template>
  <div id="questions row" v-if="questions" class="text-center q-mb-xl">
    <div v-for="(g, index) in questions" :key="index" class="q-pt-sm">
      <q-chip
        clickable
        outline
        square
        color="light-blue-9"
        class="q-py-lg"
        text-color="white"
        @click="getParaphrase(g)"
      >
        <span style="font-size: 1.2rem">{{ g }} </span>
      </q-chip>
    </div>
    <q-dialog v-model="paraphrasing_available" persistent>
      <my-popup
        @close="reset"
        :data="paraphrasing_data"
        :query="paraphrasing_query"
      />
    </q-dialog>
  </div>
</template>

<script>
export default {
  props: ["questions"],
  components: {
    "my-popup": require("components/PopUp").default,
  },
  data() {
    return {
      paraphrasing_available: false,
      paraphrasing_data: null,
      paraphrasing_query: "",
    };
  },
  methods: {
    reset() {
      console.log("closed");
    },
    async getParaphrase(query) {
      this.paraphrasing_query = query;
      const para = await this.$axios.get(
        `http://localhost:5000/rewrite/?query=${query}`
      );
      this.paraphrasing_data = para.data.response;
      console.log(this.paraphrasing_data);
      this.paraphrasing_available = para.data != null;
    },
  },
};
</script>
<style lang="scss" scoped>
</style>