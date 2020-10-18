import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class CsvService {
  constructor(private http: HttpClient) {}

  fetchCsv(file) {
    const data = new FormData();
    data.append('file', file);
    data.append('resource_type', 'raw');
    data.append('upload_preset', environment.UPLOAD_PRESET);
    data.append('cloud_name', environment.CLOUD_NAME);
    return this.http.post(environment.URL, data);
  }

  fetchResult(url) {
    return this.http.post('https://adx-api-by-sai.herokuapp.com/', { url });
  }
}
