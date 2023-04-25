<template>
  <q-page class="flex flex-center">
    <div>
      <div v-for="item in store.$state.routers.data" :key="item.id">
        {{ item }}
      </div>
    </div>
    <!-- <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    > -->
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

  computed: {

  },

  mounted() {
    this.store.routerList()
    console.log('Список маршрутов')
    console.log(this.store.routers)
  },

})
</script>
