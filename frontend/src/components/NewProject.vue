<template>
  <v-container>
          <v-row >
              <v-col cols="8">
    <v-text-field
    v-for="atr in attributes" :key="atr.name"
            :label="atr.name"
            v-model="atr.content"
          ></v-text-field>
          </v-col>
          <v-col align-self="center" align="center" cols="4">
              <v-btn @click="clearIteams()" dark fab color="red"><v-icon>{{ "mdi-close" }}</v-icon></v-btn>
          </v-col>
          </v-row>
          <v-row>
              <v-col cols="8">
              <v-btn @click="createProject()" color="primary">submit</v-btn>
              </v-col>
          </v-row>
          </v-container>
         
</template>


<script>
import axios from 'axios'
export default {
  data () {
    return {
        attributes: [{name: "title", content:""},
        {name: "description", content:""},
        {name: "logo", content:""},
        {name: "date", content:""},
        ],
    }
  },
  methods:{
    getProjectsFromBackend () {
          
    },
    clearIteams (check = false) {
        let value = true;
        if(check){
            for (let item of this.attributes){
                if(item.content.length == 0){
                    value = false
                }
            }
            return value
        }else{
            for (let item of this.attributes){
                item.content=""
            }
        }
    },
    createProject () {
        let path = "https://portfoglio.herokuapp.com/api/newproject"
        if (this.clearIteams(true)){
            
            axios.post(path,this.attributes).then( response => {
                console.log(response)
                if (response.data == "200"){
                    this.clearIteams()
                }
            }).catch( e =>{
                console.log(e)
            }) 
        }
        
    }
    //
  },
  created () {
    
  }
}
</script>