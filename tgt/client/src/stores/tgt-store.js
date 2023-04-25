import { defineStore } from 'pinia'
import { api } from 'src/boot/axios'

export const useRouterStore = defineStore('routers', {
  state: () => ({
    routers: [],
  }),
  getters: {
    // doubleCount: (state) => state.counter * 2,
  },
  actions: {
    async routerList() {
        try {
          this.routers = await api.get('http://127.0.0.1:8000/api/v1/')  
        } catch (error) {
            console.log(error)
          return error
        }
    },
    }
});
