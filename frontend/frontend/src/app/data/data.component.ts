import { Component, OnInit } from '@angular/core';


export interface PeriodicElement {
 value:string;
 strength:string;
}

const ELEMENT_DATA: PeriodicElement[] = [
  { value: '0-25', strength: 'Absent or Weak Trend' },
  { value: '25-50', strength: 'Strong Trend' },
  { value: '50-75', strength: 'Very Strong Trend' },
  { value: '75-100', strength: 'Extremely Strong Trend' }
];

@Component({
  selector: 'app-data',
  templateUrl: './data.component.html',
  styleUrls: ['./data.component.css'],
})
export class DataComponent {
  displayedColumns: string[] = ['value','strength'];
  dataSource = ELEMENT_DATA;
}
