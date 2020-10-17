import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { UPLOAD_PRESET, CLOUD_NAME, URL } from '../constants';

@Injectable({
  providedIn: 'root',
})
export class CsvService {
  constructor(private http: HttpClient) {}

  fetchCsv(file) {
    const data = new FormData();
    data.append('file', file);
    data.append('resource_type', 'raw');
    data.append('upload_preset', UPLOAD_PRESET);
    data.append('cloud_name', CLOUD_NAME);
    return this.http.post(URL, data);
  }
}
