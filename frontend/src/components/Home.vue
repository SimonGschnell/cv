<template>
  <div>
    <p>Home</p>
    <p>Random number from backend: {{ randomNumber }}</p>
    
    <v-btn color="primary" @click="getRandomNumberFromBackend()">Primary</v-btn>
    
  </div>
</template>

<script>
import axios from 'axios'
export default{
  data(){
    return{
      randomNumber: 0,
      projects : [{'title': 'something', 'date':'somethingelse'}]
    }
  },
  methods: {
    
    getRandomNumberFromBackend () {
      const path = 'http://localhost:5000/api/random'
      axios.get(path).then( response => {
        this.randomNumber= response.data.randomNumber
      }).catch( error => {
        console.log(error)
      })
    }
    
  }, 
  mounted () {
    
  } 
}
</script>
