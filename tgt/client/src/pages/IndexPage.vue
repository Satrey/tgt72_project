<template>
  <q-page class="flex flex-center">
    <div>
      <div v-for="item in store.routers.data"
        :key="item.id"        
      >
        <a href="">{{ item }}</a>
      </div>
    </div>
    {{ store.routers.data }}
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import { useRouterStore } from '../stores/tgt-store'

export default defineComponent({
  name: 'IndexPage',

  setup() {
    const store = useRouterStore()
    return { 
      store,
    }
  },

  data() {
    return {

    }
  },

  computed: {

  },

  mounted() {
    this.store.routerList()
    console.log(this.store.routers)
  },

})
</script>
