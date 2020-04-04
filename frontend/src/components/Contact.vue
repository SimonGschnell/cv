<template>
  <v-container >
    
    
    <v-form
   
    ref="form"
    v-model="valid"
   
  >
<v-container class="pa-5">
  <v-row>
    <v-col>
  <h2>Contact me</h2>
    </v-col>
  </v-row>
  <v-row>
    <v-col sm="12" md="6" lg="6" xl="4">
    <v-text-field
      v-model="name"
      label="Name"
      required
      :rules="nameRules"
      prepend-icon="mdi-account-box-outline"
    ></v-text-field>
</v-col>
<v-col sm="12" md="6" lg="6" xl="4">
    <v-text-field
      v-model="email"
      :rules="emailRules"
      label="E-mail"
      required
      prepend-icon="mdi-email-outline"
    ></v-text-field>
</v-col>
   <v-col sm="12" md="12" lg="12" xl="4">
    <v-combobox
    prepend-icon="mdi-information-outline"
          v-model="select"
          :items="items"
          label="Where did you hear from me"
          
        ></v-combobox>
        </v-col>
        </v-row>
        <v-row>
          <v-col>
           <v-textarea
          solo
          :rules="messageRules"
          name="message"
          label="Message"
          v-model="message"
          required
        ></v-textarea>
        </v-col>
        </v-row>
        <v-row>
        <v-col>
    <v-btn
      color="success"
      class="mr-4"
      @click="validate"
    >
      Say Hello!
    </v-btn>
    </v-col>
        </v-row>
   
    
   </v-container>
  </v-form>
  
  </v-container>
</template>

<script>
export default{
  data(){
    return{
      valid :false,
      name:"",
      nameRules: [
        v => !!v || 'Name is required'
      ],
      message:"",
      messageRules: [
        v => !!v || 'Message is required'
      ],
      email: '',
      select:"",
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid',
      ],
      items: [
        'item 1',
        'Item 2',
        'Item 3',
        'Item 4',
      ],
    }
  },
  methods:{

  },
}
</script>
