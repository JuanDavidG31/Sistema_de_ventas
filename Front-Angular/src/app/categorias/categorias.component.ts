import { Component } from '@angular/core';

@Component({
  selector: 'app-categorias',
  templateUrl: './categorias.component.html',
  styleUrl: './categorias.component.scss'
})
export class CategoriasComponent {
  show1 = false;
  show2 = false;
  show3 = false;
  show4 = false;

  toggle(n: number) {
    this.show1 = n === 1;
    this.show2 = n === 2;
    this.show3 = n === 3;
    this.show4 = n === 4;
  }
}
