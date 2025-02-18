import './assets/main.css';

import { createNotivue } from 'notivue';
import { createPinia } from 'pinia';
import { createApp } from 'vue';

import App from './App.vue';
import router from './router';

import 'notivue/animations.css'; // Only needed if using default animations
import 'notivue/notification.css'; // Only needed if using built-in <Notification />
import 'notivue/notification-progress.css';

const app = createApp(App);
const notivue = createNotivue({
    position: 'bottom-right',
    notifications: {
        global: {
            duration: 3000,
        },
    },
    limit: 5,
});

app.use(createPinia());
app.use(router);
app.use(notivue);

app.mount('#app');
