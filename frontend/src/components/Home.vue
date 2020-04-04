<template>
  <v-container class="py-7">
    <v-row>
      <v-col offset="1" cols="2">
    <v-img src="/static/assets/placeholder.png" height="150" width="150" contain></v-img>
  </v-col>
  <v-col cols="5">
     <v-list
       dense
      >
       
        <v-list-item-group color="primary">
          <v-list-item
            v-for="item in list"
            :key="item.name"
          >
            
            <v-list-item-content>
              <v-list-item-title >{{item.name}}</v-list-item-title>
              <v-list-item-subtitle >{{item.value}}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
  </v-col>
  <v-col  align-self="end">
    <span class="display-1">Skills</span>
  </v-col>
    </v-row>
    <v-row>
  <v-col offset="1" >
    <v-sheet class="text-justify" style="line-height: 1.8">
      My friends call me Simml, my journey began with a simple desk office job where I started to realized that life provides many options and I myself am the one which chooses the direction.
      I went to a technological highschool and didn't have much experience in the field I love so much (programming). So I started small by buying beginner books advanced into online tutorials and paid courses.
      I took a step into the right direction and was welcomed into a company as a frontend developer after the completion of a test project for them to test my skills.
      I am currently a student for computer science in the university (unibz) and enjoying every little bit of knowledge in my favorite field even though Mathematics is pretty rough.
      
    </v-sheet>
  </v-col>
  <v-col sm="0" md="4" lg="4" xl="6">
    <v-chip 
      v-for="skill in skills"
      :key="skill"
      outlined
      ripple
      class="ma-2"
      :color="skill.color"
    >
      {{skill.name}}
    </v-chip>
    
  </v-col>
  </v-row>
 </v-container>
</template>

<script>
export default{
  data(){
    return{
        skills:[{name:"Html",color:"grey"},{name:"Css",color:"grey"},{name:"Java",color:"green"},{name:"Javascript",color:"orange"},{name:"Vue",color:"green"},{name:"Math",color:"grey"},{name:"Regex",color:"orange"}
        ,{name:"Python",color:"green"},{name:"Logic",color:"grey"},{name:"Descrete",color:"grey"},{name:"bs4",color:"orange"},{name:"Webscrapping",color:"green"},{name:"Backend",color:"grey"},{name:"Android",color:"orange"},{name:"Frontend",color:"grey"},{name:"Bash-Scripting",color:"orange"},{name:"Command-line",color:"orange"},{name:"Git",color:"green"}],
        list : [{name:"Age", value:22}, {name:"Name", value:"Simon Gschnell"}, {name:"Email", value:"Simon.Gschnell@stud-inf.unibz.it"}],

    }
  },
  methods: {
  }, 
  mounted () {
  } 
}
</script>
