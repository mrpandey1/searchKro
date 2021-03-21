<template>
  <div>
    <tree
      :data="tree"
      node-text="name"
      layoutType="horizontal"
      :duration="750"
      style="max-height: 500px"
    >
    </tree>
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
import { tree } from "vued3tree";

export default {
  props: ["tree"],
  components: {
    tree,
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