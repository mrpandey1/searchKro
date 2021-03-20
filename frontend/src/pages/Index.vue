<template>
  <q-page>
    <div
      id="jumbo"
      class="q-pa-lg text-center"
      style="width: 100vw; height: 100vh"
    >
      <h3>Enter Query</h3>
      <q-input
        v-model="query"
        class="q-pb-lg"
        style="max-width: 50%; margin: auto"
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

      <q-icon
        name="arrow_downward"
        v-if="google_data"
        size="xl"
        class="q-pt-xl"
        style="display: block; margin: auto"
      />
    </div>

    <div id="googleRes" v-if="google_data" class="text-center">
      <q-separator class="q-mb-xl" />
      <h3>Top related queries</h3>
      <div v-for="(g, index) in google_data" :key="index">
        <q-chip clickable outline square color="deep-orange" text-color="white" @click="openUrl(g)">
          {{ g }}
        </q-chip>
      </div>
    </div>
    <div class="q-mb-md"></div>
  </q-page>
</template>

<script>
export default {
  data() {
    return {
      query: "",
      loading: false,
      google_data: null,
    };
  },
  methods: {
    openUrl(url) {
      window.open("https://www.google.com/search?q="+url, "_blank");
    },
    async submit() {
      try {
        this.google_data = null
        this.loading = true;
        const google_res = await this.$axios.get(
          `http://localhost:5000/?query=${this.query}`
        );
        console.log(google_res.data);
        this.google_data = google_res.data.response;
        this.loading = false;
      } catch (e) {
        alert(e);
      }
    },
  },
};
</script>
<style lang="scss" scoped>

  html{
    overflow-x: hidden;
  }
</style>