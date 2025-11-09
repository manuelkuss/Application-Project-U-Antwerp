import { Component } from '@angular/core';
import { Header } from '../header/header';
import { BrowserModule } from '@angular/platform-browser';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-test-page',
  imports: [RouterOutlet, Header, NgxChartsModule],
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
