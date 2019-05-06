import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class HelloService {

  API_URL  =  '/api';
  constructor(private  httpClient:  HttpClient) { }

  hello(){
    return this.httpClient.get('/api/hello');
  }
}
