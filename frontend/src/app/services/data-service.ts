import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ChartDataResponse, ChartSeries } from '../models/chartData.model';

@Injectable({
  providedIn: 'root',
})
export class DataService {
  private apiUrl = 'http://localhost:8000/api/chart-data/';

  constructor(private http: HttpClient) {}

  getChartData(): Observable<ChartDataResponse[]> {
    return this.http.get<ChartDataResponse[]>(this.apiUrl);
  }

}
