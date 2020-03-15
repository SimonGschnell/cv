<template>

  <v-app>
   <div>
    <v-app-bar
      color="deep-purple accent-4"
      
      dark
      collapse-on-scroll
      style="
      background-image: url('https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg');
      background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  "
      app
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Page title</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
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
       <div class="d-flex">
      <v-card
    height="400"
    width="256"
    class="ma-6"
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
      <v-card class="flex-grow-1 mr-6 mb-6 mt-6 pa-6">
        <router-view/>
      </v-card>
      </div>
    </v-content>
    
    
  </v-app>
</template>

<script>
export default {
  name: 'App',


  data: () => ({
    items: [
      { icon: "mdi-account-box", title : "Home" },
      { icon: "mdi-account-box", title : "About" },
      { icon: "mdi-account-box", title : "Contact" },
      { icon: "mdi-account-box", title : "Projects" },
      
    ]
  }),
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
