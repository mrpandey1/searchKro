<template>
  <q-page>
    <div id="jumbo" class="q-pa-lg text-center">
      <h3>Ask Me Something</h3>
      <q-input
        v-model="query"
        class="q-pb-lg"
        style="max-width: 50%; margin: auto; font-size:1.3rem"
      />

      <q-btn
        @click="submit"
        color="primary"
        label="Submit"
        :loading="loading"
        style="width: 150px"
      >
        <template v-slot:loading>
          <q-spinner-gears class="on-left" />
          Searching...
        </template>
      </q-btn>

      <!-- <q-icon
        name="arrow_downward"
        v-if="questions"
        size="xl"
        class="q-pt-xl"
        style="display: block; margin: auto"
      /> -->
    </div>

    <!-- when data is available -->
    <div v-if="questions!=null">
      <center>
        <h4>People also ask</h4>
        <q-btn-toggle
          v-model="toggle_value"
          class="q-mb-lg"
          toggle-color="primary"
          :options="[
            { label: 'Result', value: 'result' },
            { label: 'Graph', value: 'graph' },
          ]"
        />
      </center>
      <my-questions :questions="questions" v-if="toggle_value == 'result'" />
      <my-graph :tree="graph" v-else />
    </div>
  </q-page>
</template>

<script>
export default {
  components: {
    "my-graph": require("components/Graph").default,
    "my-questions": require("components/Questions").default,
  },
  data() {
    return {
      query: "",
      loading: false,
      questions: null,
      graph: null,
      toggle_value: "result",
    };
  },
  methods: {
    async submit() {
      try {
        this.questions = null;
        this.loading = true;
        const res = await this.$axios.get(
          `http://localhost:8000/api/quora?query=${this.query}`
        );
        this.questions = res.data.response;
        this.graph = res.data.graph;
        this.loading = false;
        // console.log(this.questions);
        // console.log(this.graph);
      } catch (e) {
        alert(e);
      }
    },
  },
};
</script>
<style lang="scss">
  
</style>