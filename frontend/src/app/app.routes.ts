import { Routes } from '@angular/router';
import { Notes } from './notes/notes';
import { Home } from './home/home';
import { ChartsNGX } from './charts-ngx/charts-ngx';
import { ChartsPlotly } from './charts-plotly/charts-plotly';
import { Sequence } from './sequence/sequence';
import { InteractivePlot } from './interactive-plot/interactive-plot';
import { SequenceViewer } from './sequence-viewer/sequence-viewer';

export const routes: Routes = [
    {
        path: '',
        redirectTo: '/home',
        pathMatch: 'full'
    },
    {
        path: 'home',
        component: Home
    },
    {
        path: 'notes',
        component: Notes
    },
    {
        path: 'charts-ngx',
        component: ChartsNGX
    },
    {
        path: 'charts-plotly',
        component: ChartsPlotly
    },
    { 
        path: 'sequence/:id', 
        component: Sequence 
    },
    {
        path: 'interactive-plot',
        component: InteractivePlot
    },
    {
        path: 'sequence-viewer',
        component: SequenceViewer
    }
];