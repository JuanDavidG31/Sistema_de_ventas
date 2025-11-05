import { Component, OnInit } from '@angular/core';

interface TableItem {
  id: number;
  name: string;
  description: string;
  status: 'activo' | 'inactivo' | 'pendiente';
  date: Date;
}

@Component({
  selector: 'app-reportes',
  templateUrl: './reportes.component.html',
  styleUrls: ['./reportes.component.scss']
})
export class ReportesComponent implements OnInit {

  data: TableItem[] = [
    { id: 1, name: 'Matriz de Riesgos', description: 'Evaluación de riesgos del proyecto X.', status: 'activo', date: new Date('2023-01-15') },
    { id: 2, name: 'Matriz de Habilidades', description: 'Análisis de competencias del equipo de desarrollo.', status: 'pendiente', date: new Date('2023-02-20') },
    { id: 3, name: 'Matriz de Decisiones', description: 'Soporte para la toma de decisiones estratégicas.', status: 'inactivo', date: new Date('2023-03-01') },
    { id: 4, name: 'Matriz FODA', description: 'Análisis DAFO para el lanzamiento del nuevo producto.', status: 'activo', date: new Date('2023-03-10') },
    { id: 5, name: 'Matriz de Trazabilidad', description: 'Seguimiento de requisitos desde el inicio hasta la implementación.', status: 'pendiente', date: new Date('2023-03-25') },
    { id: 6, name: 'Matriz RACI', description: 'Definición de roles y responsabilidades en el proyecto Y.', status: 'activo', date: new Date('2023-04-05') },
    { id: 7, name: 'Matriz de Eisenhower', description: 'Priorización de tareas para mejorar la productividad.', status: 'inactivo', date: new Date('2023-04-12') },
    { id: 8, name: 'Matriz BCG', description: 'Análisis de cartera de productos de la empresa.', status: 'activo', date: new Date('2023-04-18') },
    { id: 9, name: 'Matriz de Ansoff', description: 'Estrategias de crecimiento para nuevos mercados.', status: 'pendiente', date: new Date('2023-05-01') },
    { id: 10, name: 'Matriz de Kraljic', description: 'Análisis de la cartera de proveedores.', status: 'activo', date: new Date('2023-05-10') },
   { id: 24, name: 'Adquisición de Equipos', description: 'Compra de hardware para el laboratorio.', status: 'activo', date: new Date('2023-07-30') }
  ];

  filteredData: TableItem[] = []; // Datos después de aplicar filtros y búsqueda
  paginatedData: TableItem[] = []; // Datos que se muestran en la página actual

  searchText: string = '';
  filterStatus: string = '';

  currentPage: number = 1;      // Página actual
  itemsPerPage: number = 10;    // Cantidad de elementos por página, por defecto 10
  totalPages: number = 0;       // Total de páginas

  constructor() { }

  ngOnInit(): void {
    this.applyFilter(); // Al inicio, aplica el filtro (que también inicializará la paginación)
  }

  applyFilter(): void {
    let tempFilteredData = [...this.data];

    // 1. Filtrado por texto de búsqueda
    if (this.searchText) {
      const lowerSearchText = this.searchText.toLowerCase();
      tempFilteredData = tempFilteredData.filter(item =>
        item.name.toLowerCase().includes(lowerSearchText) ||
        item.description.toLowerCase().includes(lowerSearchText) ||
        item.status.toLowerCase().includes(lowerSearchText)
      );
    }

    // 2. Filtrado por estado
    if (this.filterStatus) {
      tempFilteredData = tempFilteredData.filter(item =>
        item.status === this.filterStatus
      );
    }

    this.filteredData = tempFilteredData; // Actualiza los datos filtrados

    // Reinicia la página a la primera cuando se aplican nuevos filtros
    this.currentPage = 1;
    this.calculateTotalPages(); // Recalcula el total de páginas
    this.paginateData();       // Aplica la paginación
  }

  calculateTotalPages(): void {
    this.totalPages = Math.ceil(this.filteredData.length / this.itemsPerPage);
    // Asegura que si no hay datos, haya al menos 1 página para evitar divisiones por cero o NaN
    if (this.totalPages === 0 && this.filteredData.length > 0) {
      this.totalPages = 1;
    } else if (this.filteredData.length === 0) {
      this.totalPages = 1; // Si no hay datos, mostrar 1 página para evitar "Página 0 de 0"
    }
  }

  paginateData(): void {
    const startIndex = (this.currentPage - 1) * this.itemsPerPage;
    const endIndex = startIndex + this.itemsPerPage;
    this.paginatedData = this.filteredData.slice(startIndex, endIndex);
  }

  nextPage(): void {
    if (this.currentPage < this.totalPages) {
      this.currentPage++;
      this.paginateData();
    }
  }

  prevPage(): void {
    if (this.currentPage > 1) {
      this.currentPage--;
      this.paginateData();
    }
  }

  onItemsPerPageChange(): void {
    // Al cambiar la cantidad de elementos por página,
    // volvemos a la primera página y recalculamos todo
    this.currentPage = 1;
    this.calculateTotalPages();
    this.paginateData();
  }
}
