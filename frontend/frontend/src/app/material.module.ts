import { NgModule } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatDividerModule } from '@angular/material/divider';
import { MatTableModule } from '@angular/material/table';

@NgModule({
  exports: [MatButtonModule, MatDividerModule, MatTableModule],
})
export class MaterialModule {}
