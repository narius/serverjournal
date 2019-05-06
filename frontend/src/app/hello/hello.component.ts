import {Component, OnInit} from '@angular/core';
import {HelloService} from "../services/hello.service";
import {AuthService} from "../services/auth.service";
import {timer} from "rxjs";

@Component({
  selector: 'app-hello',
  templateUrl: './hello.component.html',
  styleUrls: ['./hello.component.css']
})
export class HelloComponent implements OnInit {
  text: string;
  tick: number

  constructor(private hs: HelloService,
              private ls: AuthService) {
  }

  ngOnInit() {
    this.tick = 0;
    console.log('Hello ngOnInit');
    this.hs.hello().subscribe((data) => {
      console.log('hello');
      console.log(data);
      this.text = data['test'];
    })

    this.ls.is_authenticated().subscribe((data) => {
      console.log("is authenticated")
      console.log(data)
      console.log(data['user'])
      console.log(data['is_authenticated'])
    })
    this.ls.login('marcus', '880515').subscribe((data) => {
      console.log('login')
      console.log(data)
    })

    timer(0, 500).subscribe(() => {
        this.tick++;
      }
    )
  }

}
