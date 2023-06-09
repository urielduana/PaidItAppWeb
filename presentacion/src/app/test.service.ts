import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { catchError } from 'rxjs/internal/operators/catchError';

@Injectable({
  providedIn: 'root'
})
export class TestService {

  constructor(private http: HttpClient) { }
  public gettest():Observable<any>{
    return this.http.get("http://localhost:8000/test")
  }
  public posttest():Observable<any>{
    return this.http.post("http://localhost:8000/test",{
      nick_name: "test",
      full_name: "test2"
    })
  }
}
