<template>
  <div id="questions row" v-if="questions" class="text-center q-mb-xls">
    <div v-for="(g, index) in questions" :key="index" class="q-pt-sm">
      <q-chip
        clickable
        outline
        square
        color="light-blue-9"
        class="q-py-lg"
        text-color="white"
        @click="paraphrasing_query=g;showDialog = true"
      >
        <span style="font-size: 1.2rem;">{{ g.length > 100 ? g.slice(0,100)+'...':g.slice(0,100)}} </span>
      </q-chip>
    </div>
    <q-dialog v-model="showDialog" persistent>
      <my-popup :query="paraphrasing_query" @close="showDialog = false" />
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
      paraphrasing_query: "",
      showDialog: false,
    };
  },
  methods: {},
};
</script>
<style lang="scss" scoped>
</style>