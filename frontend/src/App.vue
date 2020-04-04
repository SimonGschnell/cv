<template>

  <v-app>
   <div>
    <v-app-bar
      color="deep-purple accent-4"
      
      dark
      collapse-on-scroll
      style="
      background-image: url('https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg');"
      app
    >
    <v-menu offset-y>
      <template v-slot:activator="{ on }">
        <v-app-bar-nav-icon v-on="on"></v-app-bar-nav-icon>
      </template>
      <v-list>
          <v-list-item
            v-for="n in 5"
            :key="n"
            @click="() => {}"
          >
            <v-list-item-title>Option {{ n }}</v-list-item-title>
          </v-list-item>
        </v-list>
    </v-menu>
      


      <v-spacer></v-spacer>

      <v-btn target="_blank" href="https://www.linkedin.com/in/simon-gschnell-87b081169/" icon>
        <v-icon>mdi-linkedin</v-icon>
      </v-btn>

     

      <v-menu
        left
        bottom
      >
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="n in 5"
            :key="n"
            @click="() => {}"
          >
            <v-list-item-title>Option {{ n }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    
    </div>
    
    
  
    <!--<v-parallax height="100" src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg"></v-parallax>-->
   
   

    <v-content>
      <v-container fluid>
       <v-row>
         <v-col sm="2" md="auto">
      <v-card
    height="400"
    width="200"
  >
  
    <v-navigation-drawer 
    absolute
      dark
      src="https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg"
      width="100%"
      permanent
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            Portfoglio
          </v-list-item-title>
          <v-list-item-subtitle>
            Simon Gschnell
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        dense
        nav
      >
     <!--<router-link :to="{ name: 'about', params: { userId: 123 }}">-->
        <div
        v-for="item in items"
          :key="item.title"
          >
        <router-link :to="{ name: item.title }" exact>
        <v-list-item
          style="text-decoration: none;"
          link
        >
         
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
          
        </v-list-item>
        </router-link>
        </div>
      </v-list>
    </v-navigation-drawer>
  </v-card>
  </v-col>
  <v-col class="flex-grow-1" >
      <v-card >
        <router-view/>
      </v-card>
      </v-col>
      </v-row>
      </v-container>
    </v-content>
    
    
  </v-app>
</template>

<script>
export default {
  name: 'App',


  data: () => ({
    items: [
      { icon: "mdi-home-outline", title : "Home" },
      { icon: "mdi-information-outline", title : "About" },
      { icon: "mdi-folder-outline", title : "Projects" },
      { icon: "mdi-email-outline", title : "Contact" },
      { icon: "mdi-account-box", title : "NewProject" },
      
    ],
  }),
  methods:{
   
  }
};
</script>
<style>
a {
    text-decoration: none;
}
.router-link-exact-active > div:before{
    opacity: .25;
}
</style>
