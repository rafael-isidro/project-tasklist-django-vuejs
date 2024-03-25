<template>
    <div class="container-container">
        <div class="container-content">
            <div class="row py-4 d-flex flex-column align-items-center justify-content-center middle-content">
                <div class="col-md-12 my-4">
                    <form v-if="!editing.status" @submit.prevent="addNew" action="" class="d-flex flex-row"
                        method="POST">
                        <input class="form-control" type="text" name="title" placeholder="Tarefa de hoje"
                            v-model="newItem.title" required>
                        <button class="styled-button btn ms-2 btn-primary">Adicionar</button>
                    </form>
                    <form v-else @submit.prevent="update" action="" class="d-flex flex-row" method="POST">
                        <input class="form-control" type="text" name="title" placeholder="Tarefa de hoje"
                            v-model="editing.item.title" required>
                        <button class="styled-button btn ms-2 btn-primary">Editar</button>
                    </form>
                </div>
                <div class="col-md-12 text-start">
                    <table class="table">
                        <thead>
                            <tr>
                                <th scope="col"></th>
                                <th scope="col"></th>
                                <th scope="col"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="item in tasks" v-bind:key="item.id" class="text-center">
                                <td>{{ item.title }}</td>
                                <td>
                                    <div class="form-check" v-if="item.completed">
                                        <input class="form-check-input" type="checkbox" checked :id="item.id"
                                            @change="changeStatus(item)">
                                    </div>
                                    <div class="form-check" v-else>
                                        <input class="form-check-input" type="checkbox" :id="item.id"
                                            @change="changeStatus(item)">
                                    </div>
                                </td>
                                <td>
                                    <svg @click="edit(item)" xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                        fill="currentColor" class="bi bi-pencil-square me-1" viewBox="0 0 16 16">
                                        <path
                                            d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z" />
                                        <path fill-rule="evenodd"
                                            d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z" />
                                    </svg>
                                    <svg @click="removeItem(item.id)" xmlns="http://www.w3.org/2000/svg" width="16"
                                        height="16" fill="currentColor" class="bi bi-x-lg" viewBox="0 0 16 16">
                                        <path d=" M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1
                                        .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0
                                        1-.708-.708L7.293 8z" />
                                    </svg>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="col-md-12 position-absolute top-0 end-0 mt-3 me-3">
                    <button @click="logout()" type="submit" class="styled-button btn btn-primary">Sair
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                            class="bi bi-box-arrow-right" viewBox="0 0 16 16">
                            <path fill-rule="evenodd"
                                d="M10 12.5a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v2a.5.5 0 0 0 1 0v-2A1.5 1.5 0 0 0 9.5 2h-8A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-2a.5.5 0 0 0-1 0z" />
                            <path fill-rule="evenodd"
                                d="M15.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708.708L14.293 7.5H5.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708z" />
                        </svg>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "Tasklist",
    data() {
        return {
            tasks: [],
            newItem: {
                title: "",
                completed: false,
                user: this.$store.state.user_id
            },
            editing: {
                status: false,
                item: {}
            }
        };
    },
    methods: {
        fetchTasklist() {
            axios.defaults.headers["Authorization"] = `Token ${this.$store.state.token}`;
            const url = "/list-create-tasklist/";
            axios.get(url)
                .then(response => {
                    this.tasks = response.data;
                })
                .catch(error => {
                    console.log(error)
                })
        },
        addNew() {
            axios.defaults.headers["Authorization"] = `Token ${this.$store.state.token}`;
            const url = "/list-create-tasklist/";
            axios.post(url, this.newItem)
                .then(response => {
                    this.tasks.unshift(response.data);
                    this.newItem = { title: "", completed: false, user: this.$store.state.user_id };
                })
                .catch(error => {
                    console.log(error)
                })
        },
        edit(item) {
            this.editing.status = true;
            this.editing.item = item;
        },
        changeStatus(item) {
            this.editing.item = item;
            this.editing.item.completed = !item.completed;
            this.update();
        },
        update() {
            axios.defaults.headers["Authorization"] = `Token ${this.$store.state.token}`;
            const url = "/retrieve-update-destroy-tasklist/" + this.editing.item.id + "/";
            axios.put(url, this.editing.item)
                .then(response => {
                    this.editing.status = false;
                    this.editing.item = {}
                    this.fetchTasklist();
                })
                .catch(error => {
                    console.log(error)
                })
        },
        removeItem(id) {
            axios.defaults.headers["Authorization"] = `Token ${this.$store.state.token}`;
            const url = "/retrieve-update-destroy-tasklist/" + id + "/";
            axios.delete(url)
                .then(response => {
                    this.fetchTasklist();
                })
                .catch(error => {
                    console.log(error)
                })
        },
        logout() {
            this.$store.commit("removeToken");
            this.$router.push('/');
        }
    },
    mounted() {
        this.fetchTasklist();
    }
}
</script>

<style scoped lang="scss">
.container-container {
    display: flex;
    background-color: #6882aa;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.container-content {
    background-color: #ffffff;
    border-radius: 20px;
    padding: 15px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
    min-width: 50vw;
    min-height: 50vh;
}

.styled-button {
    background-color: #001a42;
    color: #ffffff;
    font-weight: 600;
    border-radius: 20px;
    padding: 10px 20px;
    border: none;
    transition: background-color color 0.3s ease;
}

.styled-button:hover {
    color: #ffffff;
    background-color: #2a456d;
}

svg {
    cursor: pointer;
}
</style>