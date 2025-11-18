import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { Header } from './header/header';
import { Footer } from './footer/footer';

// NoteService depends on HttpClient
// In standalone Angular apps, HttpClientModule must be explicitly imported wherever it’s needed. Angular no longer automatically provides it.

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, Header, Footer, HttpClientModule],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  // protected readonly title = signal('frontend');
}
