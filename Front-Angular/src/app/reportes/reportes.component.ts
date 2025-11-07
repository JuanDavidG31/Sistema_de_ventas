import { Component, ElementRef, ViewChild, AfterViewInit } from '@angular/core';
import ApexCharts from 'apexcharts';

@Component({
  selector: 'app-reportes',
  templateUrl: './reportes.component.html',
  styleUrls: ['./reportes.component.scss']
})
export class ReportesComponent implements AfterViewInit {

  @ViewChild('ventasMesChart') ventasMesChart!: ElementRef;
  @ViewChild('productosVendidosChart') productosVendidosChart!: ElementRef;
  @ViewChild('ventasDepartamentoChart') ventasDepartamentoChart!: ElementRef;
  @ViewChild('gravadasChart') gravadasChart!: ElementRef;
  @ViewChild('tipoPagoChart') tipoPagoChart!: ElementRef;

  ngAfterViewInit(): void {
    this.cargarVentasMes();
    this.cargarProductosVendidos();
    this.cargarVentasDepartamento();
    this.cargarGravadas();
    this.cargarTipoPago();
  }

  // 6.1 Ventas por mes
  cargarVentasMes() {
    const options = {
      chart: { type: 'line', height: 330 },
      series: [{ name: 'Ventas', data: [45, 60, 80, 75, 95, 110] }],
      xaxis: { categories: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'] },
      stroke: { curve: 'smooth' }
    };

    new ApexCharts(this.ventasMesChart.nativeElement, options).render();
  }

  // 6.2 Productos más vendidos
  cargarProductosVendidos() {
    const options = {
      chart: { type: 'bar', height: 330 },
      series: [{ name: 'Cantidad', data: [120, 90, 75, 60] }],
      xaxis: { categories: ['Oso', 'Carro', 'Puzzle', 'Construcción'] }
    };

    new ApexCharts(this.productosVendidosChart.nativeElement, options).render();
  }

  // 6.3 Ventas por departamento
  cargarVentasDepartamento() {
    const options = {
      chart: { type: 'bar', height: 330 },
      series: [{ name: 'Ventas', data: [300, 240, 180, 150] }],
      xaxis: { categories: ['Antioquia', 'Valle', 'Cundinamarca', 'Santander'] }
    };

    new ApexCharts(this.ventasDepartamentoChart.nativeElement, options).render();
  }

  // 6.4 Gravadas vs no gravadas
  cargarGravadas() {
    const options = {
      chart: { type: 'pie', height: 330 },
      series: [70, 30],
      labels: ['Gravadas', 'No Gravadas']
    };

    new ApexCharts(this.gravadasChart.nativeElement, options).render();
  }

  // 6.5 Tipo de pago de clientes
  cargarTipoPago() {
    const options = {
      chart: { type: 'donut', height: 330 },
      series: [40, 35, 25],
      labels: ['Efectivo', 'Tarjeta', 'Transferencia']
    };

    new ApexCharts(this.tipoPagoChart.nativeElement, options).render();
  }
}
