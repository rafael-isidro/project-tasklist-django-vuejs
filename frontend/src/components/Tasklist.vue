<template>
    <div class="container">
        <div class="row py-4 d-flex flex-column align-items-center justify-content-center middle-content">
            <div class="col-md-12 my-4">
                <form v-if="!editing.status" @submit.prevent="addNew" action="" class="d-flex flex-row" method="POST">
                    <input class="form-control" type="text" name="title" placeholder="Tarefa de hoje"
                        v-model="newItem.title" required>
                    <button class="btn ms-2 btn-primary">Adicionar</button>
                </form>
                <form v-else @submit.prevent="update" action="" class="d-flex flex-row" method="POST">
                    <input class="form-control" type="text" name="title" placeholder="Tarefa de hoje"
                        v-model="newItem.title" required>
                    <button class="btn ms-2 btn-primary">Editar</button>
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
                        <tr v-for="item in tasks" v-bind:key="item.id">
                            <td>{{ item.title }}</td>
                            <td>
                                <div class="form-check" v-if="item.completed">
                                    <input class="form-check-input" type="checkbox" checked :id="item.id">
                                </div>
                                <div class="form-check" v-else>
                                    <input class="form-check-input" type="checkbox" :id="item.id">
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
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                    class="bi bi-x-lg" viewBox="0 0 16 16">
                                    <path
                                        d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8z" />
                                </svg>
                            </td>
                        </tr>
                    </tbody>
                </table>
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
            axios.defaults.headers['Authorization'] = `Token ${this.$store.state.token}`;
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
            axios.defaults.headers['Authorization'] = `Token ${this.$store.state.token}`;
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
        update() {

        }
    },
    mounted() {
        this.fetchTasklist();
    }
}
</script>

<style scoped lang="scss">
.middle-content {
    height: 100vh;
}

svg {
    cursor: pointer !important;
}
</style>
