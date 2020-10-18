import { Component, OnInit } from '@angular/core';
import { CsvService } from '../services/csv.service';

@Component({
  selector: 'app-csv',
  templateUrl: './csv.component.html',
  styleUrls: ['./csv.component.css'],
})
export class CsvComponent implements OnInit {
  constructor(private csv: CsvService) {}

  ngOnInit(): void {}

  selected: boolean = false;
  loading: boolean = false;
  error: string = null;
  url: string = null;

  start(): void {
    this.loading = true;
    this.selected = true;
  }

  fetchCsv(e): void {
    const file = e.target.files[0];
    if (file && file.size < 10000000) {
      this.csv.fetchCsv(file).subscribe((res) => {
        console.log(res['secure_url']);
        this.csv.fetchResult(res['secure_url']).subscribe((result) => {
          console.log(result['result']);
          this.url = result['result'];
          this.loading = false;
        });
      });
    }
  }
}
