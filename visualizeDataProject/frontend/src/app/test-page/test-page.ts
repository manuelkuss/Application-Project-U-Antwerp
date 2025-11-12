import { Component } from '@angular/core';
import { NgxChartsModule } from '@swimlane/ngx-charts';

@Component({
  selector: 'app-test-page',
  imports: [NgxChartsModule],
  templateUrl: './test-page.html',
  styleUrl: './test-page.scss',
})
export class TestPage {
  chartData = [
    { name: 'Germany', value: 8940000 },
    { name: 'USA', value: 5000000 },
    { name: 'France', value: 7200000 }
  ];
}
