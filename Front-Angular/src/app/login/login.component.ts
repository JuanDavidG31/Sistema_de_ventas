import {Component} from '@angular/core';
import {InicioService} from "../inicio/inicio.service";
import {AuthService} from "../guards/auth.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  standalone: false,
  styleUrl: './login.component.scss'
})
export class LoginComponent {
   username:string='';
   password: string='';

  constructor(private inicioService: InicioService, private auth: AuthService, private router: Router) {
  }
  login() {
    this.auth.login(this.username, this.password).subscribe({
      next: () => this.router.navigate(['/inicio']),
      error: () => {
        console.log('Error');
      }
    });
  }

}
