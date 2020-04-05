<template>
  <v-container>
    
    <v-timeline dense>
      <v-timeline-item
      hideDot
    >
    <h2>Education</h2>
    </v-timeline-item>
    <v-timeline-item
      v-for="(item, i) in school"
      :key="i"
      fillDot
    >
    
      <v-card class="elevation-2 mr-4">
          <v-card-title class="headline">{{item.header}}</v-card-title>
          <v-card-text>{{item.text}} </v-card-text>
        </v-card>
    </v-timeline-item>
    
  </v-timeline>
    <v-timeline dense reverse>
     
      <v-timeline-item
      hideDot

    >
    <h2 class="text-right">Work experience</h2>
    </v-timeline-item>
    <v-timeline-item
    
    
      v-for="(item, i) in work"
      :key="i"
      :color="item.color"
      large
    >
    <template v-slot:icon>
        <v-avatar>
          <img :src="item.avatar">
        </v-avatar>
      </template>
     
      <div class="py-4">
         <v-card class="elevation-2 ml-4">
           <v-container fluid>
             <v-row>
               <v-col>
                  <v-card-title class="headline pb-0">{{item.header}}
                     
                  </v-card-title>
                  <p class="pa-0 pl-4 ma-0 font-weight-light">{{item.subheader}}</p>
                 
                  <v-card-text>{{item.text}} </v-card-text>
               </v-col>
               <v-col>
                  <v-list
                  class="align-center text-left "
                  dense
                  >
                   
                    <v-list-item-group color="primary">
                      <v-list-item
                        v-for="(item,i) in item.list"
                        :key="i"
                      >
                        
                        <v-list-item-content>
                          <v-list-item-title >{{item}}</v-list-item-title>
                          
                        </v-list-item-content>
                      </v-list-item>
                    </v-list-item-group>
                  </v-list>
               </v-col>
             </v-row>
           </v-container>
        
        </v-card>
           
      </div>
    </v-timeline-item>
  </v-timeline>
  </v-container>
</template>

<script>
export default{
  data(){
    return{
      sampletext:"Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at.",
      work: [
        {
          color: 'cyan',
          avatar:"static/assets/mitas.jpg",
          list:["Managment of computer-hardware","Contact with customers","Build pc setups"],
          header:"Mitas",
          subheader:"Computer hardware managment",
          text:"Some text"
        },
        {
          color: 'green',
          avatar:"static/assets/webalm.jpg",
          list:["Collaboration on customer requested Website","Web development with bootstrap","Javascript",],
          header:"webAlm",
          subheader:"Web development",
          text:""
        },
        {
          color: 'pink',
          avatar:"static/assets/gruber.jpg",
          list:["Relation with suppliers","ERP management","Report creation","Sql queries","Hardware managment for employees (ME MDM app)"],
          header:"Gruber Logistics Spa",
          subheader:"Application support",
          text:""
        },
        {
          color: 'primary',
          avatar:"static/assets/yanovis.jpg",
          list:["javascript development","Vue Framework","Html & Css","Axios requests (javascript)"],
          header:"Yanovis",
          subheader:"Frontend Developer",
          text:""
        },],
      school: [
        {
          header:"Landesberufsschule für Handwerk und Industrie",
          text:"Matura Informatik"
        },
        {
          header:"Unibz",
          text:"Bachelor Computer Science"
        },
       ],
    }
  },
  methods: {
  }, 
  mounted () {
  } 
}
</script>


