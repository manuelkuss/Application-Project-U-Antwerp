import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { DataService } from '../services/data-service';
import { ChartDataResponse, ChartSeries } from '../models/chartData.model';
import { NgxChartsModule } from '@swimlane/ngx-charts';

@Component({
  selector: 'app-charts-ngx',
  standalone: true,
  imports: [CommonModule, HttpClientModule, NgxChartsModule],
  providers: [DataService],
  templateUrl: './charts-ngx.html',
  styleUrl: './charts-ngx.scss',
})
export class ChartsNGX {
  chartData: ChartSeries[] = [];

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
  }
}