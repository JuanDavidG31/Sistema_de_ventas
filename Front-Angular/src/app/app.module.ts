import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {LoginComponent} from "./login/login.component";
import {FormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";
import {PasswordComponent} from "./password/password.component";
import {InicioComponent} from "./inicio/inicio.component";
import {DashboardLayoutComponent} from "./layouts/dashboard-layout/dashboard-layout.component";
import {AuthLayoutComponent} from "./layouts/auth-layout/auth-layout.component";
import {ReportesComponent} from "./reportes/reportes.component";
import { ProductosComponent } from './productos/productos.component';
import { VentasComponent } from './resumen/ventas.component';
import { UsuariosComponent } from './usuarios/usuarios.component';



@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    PasswordComponent,
    InicioComponent,
    DashboardLayoutComponent,
    AuthLayoutComponent,
    ReportesComponent,
    ProductosComponent,
    VentasComponent,
    UsuariosComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
