<template>
  <div v-if="items">
    <h1>Projects</h1>
    <v-container>
      <v-row dense>
         <v-col
          v-for="item in items"
          :key="item.title"
          cols="12"
        >
    <v-card

            color="#385F73"
            dark
            :style="{'background-image': 'url(/static/assets/inst.png)'}"
          >
            <v-card-title class="headline">{{item.title}}</v-card-title>

            <v-card-subtitle>{{item.logo}}</v-card-subtitle>
            <v-card-text>{{item.description}}</v-card-text>
            <v-card-actions>
              <v-btn text>Listen Now</v-btn>
              <span class="ml-auto mr-5 font-weight-light">{{item.date}}</span>
            </v-card-actions>
          </v-card>
         </v-col>
          </v-row>
    </v-container>
    
    
  </div>
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


