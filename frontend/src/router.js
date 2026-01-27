import { createRouter, createWebHistory } from 'vue-router'
import Journals from './views/Journals.vue';
import NotFound from './views/NotFound.vue';
import CreateReport from './views/CreateReport.vue';
import ViewReport from './views/ViewReport.vue';
import EditReport from './views/EditReport.vue';

const routes = [
    { path: '/', component: Journals },
    { path: '/create-report', component: CreateReport },
    { path: '/view-report/:id', component: ViewReport },
    { path: '/edit-report/:id', component: EditReport },
    { path: '/:pathMatch(.*)*', component: NotFound }
]

export const router = createRouter({
    history: createWebHistory(),
    routes,
    linkExactActiveClass: 'active'
});