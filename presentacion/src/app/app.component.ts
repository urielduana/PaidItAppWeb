import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { UserInsertService } from './user-insert.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  
  title = 'presentacion';

  constructor(private userInsertService: UserInsertService) {}

  public ngOnInit () {
    const formData = new FormData();
    formData.append('nick_name', 'a');
    formData.append('full_name', 'a');

    this.userInsertService.postFormData(formData).subscribe(
      error => {console.log(error)},
      success => {console.log(success)}
    );
  }
}
