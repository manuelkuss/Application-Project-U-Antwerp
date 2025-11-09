import { Routes } from '@angular/router';
import { TestPage } from './test-page/test-page';
import { App } from './app';
import { Notes } from './notes/notes';
import { Home } from './home/home';

export const routes: Routes = [
    { 
        path: '', 
        redirectTo: '/home', 
        pathMatch: 'full' },
    { 
        path: 'home', 
        component: Home 
    },
    { 
        path: 'notes', 
        component: Notes 
    },
    {
        path: 'testPage',
        component: TestPage
    }
];