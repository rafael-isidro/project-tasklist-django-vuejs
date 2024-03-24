<template>
    <div class="container-fluid">
        <div class="row py-4 d-flex flex-column align-items-center justify-content-center middle-content">
            <div class="col-md-6 p-4 login-container">
                <h3 class="text-white text-center mb-4">Faça login</h3>
                <hr class="bg-white">
                <form @submit.prevent="submitForm">
                    <div v-if="errors.wrong_credentials" class="form-group my-2 text-start">
                        <small class="text-light-red">{{ errors.wrong_credentials }}</small>
                    </div>
                    <div class="form-group my-2 text-start">
                        <input class="form-control" type="username" placeholder="Digite o usuário" name="username"
                            v-model="username">
                        <small v-if="errors.username" class="text-light-red">{{ errors.username }}</small>
                    </div>
                    <div class="form-group my-2 text-start">
                        <input class="form-control" type="password" placeholder="Digite a senha" name="password"
                            v-model="password">
                        <small v-if="errors.password" class="text-light-red">{{ errors.password }}</small>
                    </div>
                    <div class="form-group my-2 d-grid gap-2">
                        <button type="submit" class="btn btn-primary login-button">Entrar</button>
                    </div>
                    <div class="form-group my-2 d-grid gap-2">
                        <p class="text-white">
                            Não possui uma conta?
                            <router-link class="text-decoration-none" to="/signup">Registrar-se</router-link>
                        </p>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
    name: "Login",
    data() {
        return {
            username: "",
            password: "",
            errors: {
                username: "",
                password: "",
                wrong_credentials: "",
            }
        }
    },
    methods: {
        isValidForm() {
            let valid = true;
            this.errors.username = this.username ? "" : "O campo não pode estar vazio";
            this.errors.password = this.password ? "" : "O campo não pode estar vazio";
            if (this.errors.username || this.errors.password) {
                valid = false;
            }
            return valid;
        },
        submitForm() {
            if (this.isValidForm()) {
                const url = "/login/";
                axios.post(url, { username: this.username, password: this.password })
                    .then(response => {
                        const { token, user_id } = response.data;
                        this.$store.commit("setToken", { token, user_id });
                        this.username = "";
                        this.password = "";
                        this.$router.push('/tasklist');
                    })
                    .catch(error => {
                        if (error.response.data.non_field_errors) {
                            this.errors.wrong_credentials = error.response.data.non_field_errors.join("")
                        } else {
                            this.errors.wrong_credentials = "";
                        }
                    })
            }
        },
    }
}
</script>

<style scoped lang="scss">
.middle-content {
    height: 100vh;
    background-color: #7a889b;
}

.login-container {
    background-color: #001a41;
    border-radius: 2rem;
}

.text-light-red {
    color: #ff7777;
}

.login-button {
    background-color: #8CA3C8;
    color: #001a42;
    font-weight: 600;
    border-radius: 20px;
    padding: 10px 20px;
    border: none;
    transition: color 0.3s ease;
}

.login-button:hover {
    color: #375581;
    background-color: #8CA3C8;
}
</style>
