<template>
  <div>
    <h3>Сделаем короткой вашу url ссылку</h3>
    <form @submit="formSubmit">
      <label for="url">Ваш url</label>
      <input id="url" type="text" class="form-control" v-model="longurl">
      <button type="submit">Укоротить</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  mounted() {
    console.log('Component mounted.')
  },
  data() {
    return {
      longurl: '',
      description: '',
      output: ''
    };
  },
  methods: {
    formSubmit(e) {
      e.preventDefault();
      let currentObj = this;
      axios.post('http://localhost:5000/api/create_short_url', {
        longurl: this.longurl,
      })
      .then(function (response) {
        currentObj.output = response.data;
      })
      .catch(function (error) {
        currentObj.output = error;
      });
    }
  }
}
</script>
