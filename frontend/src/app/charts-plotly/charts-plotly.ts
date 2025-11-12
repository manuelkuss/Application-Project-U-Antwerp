import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { DataService } from '../services/data-service';
import { ChartDataResponse, ChartSeries } from '../models/chartData.model';
import { PlotlyModule } from 'angular-plotly.js';
import * as PlotlyJS from 'plotly.js-dist-min';

PlotlyModule.forRoot(PlotlyJS);
@Component({
  selector: 'app-charts-plotly',
  standalone: true,
  imports: [CommonModule, HttpClientModule, PlotlyModule], 
  providers: [DataService],
  templateUrl: './charts-plotly.html',
  styleUrl: './charts-plotly.scss',
})
export class ChartsPlotly {
  chartData: ChartSeries[] = [];
  graphs: any[] = []

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.loadChart();
  }

  loadChart(): void {

    // Plotly Chart

    this.dataService.getChartData().subscribe((charts: any[]) => {
      charts.forEach((chart) => {

        var mz = chart.mz;
        var intensity = chart.intensity;

        console.log("chart: ", chart);

        // Plotly "stem plot" using scatter with mode 'lines'
        var trace = {
          x: mz,
          y: intensity,
          mode: 'lines',
          line: { color: 'blue' },
          type: 'scatter',
          fill: 'tozeroy', // fills line down to x-axis
        };

        this.graphs.push({
          data: [trace],
          layout: {
            title: chart.title,
            xaxis: {
              title: 'm/z',
              type: 'linear'
            },
            yaxis: {
              title: 'Intensity'
            },
            margin: { t: 50, l: 60, r: 20, b: 50 },
          },
          config: { responsive: true }
        });
      });
    });
  }

}