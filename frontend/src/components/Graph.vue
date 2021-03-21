<template>
  <div class="q-pa-md q-gutter-sm">
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

    <q-tree
      :nodes="[tree]"
      node-key="label"
      :filter="filter"
      default-expand-all
    />
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