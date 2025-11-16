import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { MgfFile } from '../models/mgfFile.model';
import { environment } from '../../environments/environment';
import { SequenceModel } from '../models/sequence.model';

@Injectable({
  providedIn: 'root',
})
export class SequenceViewerService {
  private apiUrlMgfFile = environment.apiUrl + 'mgf-files/';
  private apiUrlMgfFileInfo = environment.apiUrl + 'mgf-file-info/';

  constructor(private http: HttpClient) {}

  getMgfFiles(): Observable<MgfFile[]> {
    return this.http.get<MgfFile[]>(this.apiUrlMgfFile);
  }

  getMgfFileInfo(mgfFileName: string): Observable<SequenceModel[]> {
    return this.http.get<SequenceModel[]>(`${this.apiUrlMgfFileInfo}${mgfFileName}`);
  }
}

