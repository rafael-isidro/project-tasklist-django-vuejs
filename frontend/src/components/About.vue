<template>
    <div class="container-fluid">
        <div class="row py-4 d-flex flex-column align-items-center justify-content-center middle-content">
            <div class="col-md-6 p-4 login-container">
                <h3 class="text-white text-center mb-4">Sobre a Aplicação</h3>
                <hr class="bg-white">
                <div class="text-white">
                    <p>Esta é uma aplicação simples para gerenciamento de tarefas (tasks).</p>
                    <hr>
                    <p>Recursos disponíveis:</p>
                    <ul class="list-unstyled">
                        <li>---- Realizar login ----</li>
                        <li>---- Cadastrar tarefas ----</li>
                        <li>---- Gerenciar tarefas ----</li>
                        <hr>
                    </ul>
                </div>
                <div class="row">
                    <div class="col-sm-6">
                        <router-link to="/" class="about-button btn btn-primary">Ir para Login</router-link>
                    </div>
                    <div class="col-sm-6">
                        <router-link to="/signup" class="about-button btn btn-primary">Ir para Cadastro</router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "About",
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
    width: 100%;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
}

.about-button {
    background-color: #8CA3C8;
    color: #001a42;
    font-weight: 600;
    border-radius: 20px;
    padding: 10px 20px;
    border: none;
    height: 3.5rem;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background-color color 0.3s ease;
}

.about-button:hover {
    color: #ffffff;
    background-color: #6882aa;
}

@media (min-width: 720px) {
    .login-container {
        width: 40vw;
    }
}
</style>
