import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private  httpClient:  HttpClient) { }

  is_authenticated(){
    return this.httpClient.get('/api/login');
  }

  login(username:string, password:string){
    return this.httpClient.post('/api/login',
      {'username': username,
             'password':password});

  }
}
