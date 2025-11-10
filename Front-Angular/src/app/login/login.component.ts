import { Component } from '@angular/core';
import {InicioService} from "../inicio/inicio.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  standalone: false,
  styleUrl: './login.component.scss'
})
export class LoginComponent {

  constructor(private inicioService: InicioService) {}


}
