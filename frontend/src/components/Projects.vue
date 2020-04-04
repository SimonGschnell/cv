<template>
  <v-container fluid="true" v-if="items">
    <h1 class="pl-2 display-2 font-weight-bold" >Projects</h1>
    <v-container>
      <v-row dense>
         <v-col
          v-for="item in items"
          :key="item.title"
          cols="12"
          class="mb-3"
        >
    <v-card
            shaped
            dark
          >
         <v-row>
           <v-col sm="12" md="4"  class="align-center">
          <v-img
              :src="item.logo"
              height="200"
              width="200"
              contain
              class="grey darken-4"
            ></v-img>
            </v-col>
            <v-col sm="12" md="8">
       
            <v-card-title class="headline">{{item.title}}</v-card-title>

            <v-card-subtitle>{{item.logo}}</v-card-subtitle>
            <v-card-text>{{item.description}}</v-card-text>
            <v-card-actions>
              <v-btn text>Listen Now</v-btn>
              <span class="ml-auto mr-5 font-weight-light">{{item.date}}</span>
            </v-card-actions>
         </v-col>
         </v-row>
          </v-card>
         </v-col>
          </v-row>
    </v-container>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      items :null
    }
  },
  methods:{
    getProjectsFromBackend () {
          
    },
    //
  },
  created () {
    const path = 'http://localhost:5000/api/projects'
          let result = null
          axios.get(path).then( response => {
            this.items = response.data
          }).catch( error => {
            console.log(error)
          })
  }
}
</script>


