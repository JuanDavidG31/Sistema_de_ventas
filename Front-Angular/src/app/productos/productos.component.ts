import { Component } from '@angular/core';
import {ProductosService} from "./productos.service";

@Component({
  selector: 'app-productos',
  templateUrl: './productos.component.html',
  styleUrls: ['./productos.component.scss']
})
export class ProductosComponent {

  constructor(private productosService: ProductosService) {}

  show21 = false;
  show22 = false;
  show23 = false;
  show24 = false;

  toggle(section: number) {

    // Primero ocultar todas
    this.show21 = false;
    this.show22 = false;
    this.show23 = false;
    this.show24 = false;

    // Luego abrir solo la que se presionó
    if (section === 21) this.show21 = true;
    if (section === 22) this.show22 = true;
    if (section === 23) this.show23 = true;
    if (section === 24) this.show24 = true;
  }
}
