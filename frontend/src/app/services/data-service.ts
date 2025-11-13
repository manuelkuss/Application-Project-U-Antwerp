import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ChartDataResponse, ChartSeries } from '../models/chartData.model';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class DataService {
  private apiUrl = environment.apiUrl + 'chart-data/';

  constructor(private http: HttpClient) {}

  getChartData(): Observable<ChartDataResponse[]> {
    return this.http.get<ChartDataResponse[]>(this.apiUrl);
  }

}
