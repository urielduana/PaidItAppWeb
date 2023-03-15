import { Component } from '@angular/core';
  import { TestService } from './test.service'; 

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  
  title = 'presentacion';

  constructor(private t: TestService) {}



  public ngOnInit () {
    this.t.gettest().subscribe(
      error => {console.log(error)},
      success => {console.log(success)}
    );
    
  }
}
