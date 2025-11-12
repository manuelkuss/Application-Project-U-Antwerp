import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { DataService } from '../services/data-service';
import { ChartDataResponse, ChartSeries } from '../models/chartData.model';
import { NgxChartsModule } from '@swimlane/ngx-charts';
// import { PlotlyModule } from 'angular-plotly.js';
// import * as PlotlyJS from 'plotly.js-dist-min';

@Component({
  selector: 'app-charts',
  standalone: true,
  imports: [CommonModule, HttpClientModule, NgxChartsModule],
  providers: [DataService],
  templateUrl: './charts.html',
  styleUrl: './charts.scss',
  // template: '<plotly-plot [data]="graph.data" [layout]="graph.layout"></plotly-plot>'
})
export class Charts {

  chartData: ChartSeries[] = [];
  // public graph = {
  //       data: [
  //           { x: [1, 2, 3], y: [2, 6, 3], type: 'scatter', mode: 'lines+points', marker: {color: 'red'} },
  //           { x: [1, 2, 3], y: [2, 5, 3], type: 'bar' },
  //       ],
  //       layout: {width: 320, height: 240, title: 'A Fancy Plot'}
  //   };

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.loadChart();
  }

  loadChart(): void {

    // NGX Chart

    this.dataService.getChartData().subscribe({
      next: (dataResponse: ChartDataResponse[]) => {
        console.log('Fetched chart data:', dataResponse);


        // Convert backend data into ngx-charts line chart series
        this.chartData = dataResponse.map(chart => {
          // Option A: simple line connecting points
          const series = chart.mz.map((mzValue, i) => ({
            name: mzValue,
            value: chart.intensity[i]
          }));

          // // Option B: "stem plot" style (vertical lines to x-axis)
          // const series = chart.mz.flatMap((mzValue, i) => [
          //   { name: mzValue, value: 0 },                 // baseline
          //   { name: mzValue, value: chart.intensity[i] } // peak
          // ]);

          return {
            name: chart.title,
            series
          };
        });

      },
      error: err => console.error('Error fetching chart data', err)
    });


    // Plotly Chart

    // this.dataService.getChartData().subscribe((charts: any[]) => {
    //   const chart = charts[0]; // assuming a single chart

    //   const mz = chart.mz;
    //   const intensity = chart.intensity;

    //   console.log("chart: ", chart);

    //   // Plotly "stem plot" using scatter with mode 'lines'
    //   const trace = {
    //     x: mz,
    //     y: intensity,
    //     mode: 'lines',
    //     line: { color: 'blue' },
    //     type: 'scatter',
    //     fill: 'tozeroy', // fills line down to x-axis
    //   };

    //   this.graph = {
    //     data: [trace],
    //     layout: {
    //       title: chart.title,
    //       xaxis: {
    //         title: 'm/z',
    //         type: 'linear'
    //       },
    //       yaxis: {
    //         title: 'Intensity'
    //       },
    //       margin: { t: 50, l: 60, r: 20, b: 50 },
    //     },
    //     config: { responsive: true }
    //   };
    // });

    // plotly example

    
  }


}