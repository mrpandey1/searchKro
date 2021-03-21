<template>
  <div
    class="q-pa-md q-gutter-sm"
    id="graph"
    style="max-width: 600px; margin: 0 auto"
  >
    <q-input ref="filter" filled v-model="filter" label="Filter">
      <template v-slot:append>
        <q-icon
          v-if="filter !== ''"
          name="clear"
          class="cursor-pointer"
          @click="resetFilter"
        />
      </template>
    </q-input>
    <div id="qtree" class="q-mb-lg">
      <q-tree
        :nodes="[tree]"
        node-key="label"
        :filter="filter"
      />
    </div>
  </div>
</template>

<script>
export default {
  props: ["tree"],
  data() {
    return {
      filter: "",
    };
  },
  methods: {
    resetFilter() {
      this.filter = "";
      this.$refs.filter.focus();
    },
  },
};
</script>

<style lang="scss" scoped>
* {
  font-size: 107%;
}
</style>