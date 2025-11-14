import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { SequenceModel } from '../models/sequence.model';

@Injectable({
  providedIn: 'root',
})
export class SequenceService {

    private apiUrl = environment.apiUrl + 'sequence/';

    constructor(private http: HttpClient) { }

    getSequence(id: number): Observable<SequenceModel> {
      return this.http.get<SequenceModel>(`${this.apiUrl}${id}/`);
    }
}
