import { Component, OnInit } from '@angular/core';
import { NoteService } from '../services/note-service';
import { Note } from '../models/note.model';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-notes',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  providers: [NoteService],
  templateUrl: './notes.html',
  styleUrls: ['./notes.scss'],
})
export class Notes implements OnInit {
  notes: Note[] = [];

  constructor(private noteService: NoteService) { }

  ngOnInit(): void {
    this.loadNotes();
  }

  loadNotes(): void {
    this.noteService.getNotes().subscribe({
      next: (data: Note[]) => {
        console.log('Fetched notes:', data);
        this.notes = data;
      },
      error: (err) => console.error('Error loading notes', err)
    });
  }

  add(title: string, content: string): void {
    if (!title || !content) {
      return;
    }
    const newNote: Note = { title, content };
    this.noteService.addNote(newNote).subscribe(note => {
      this.notes.push(note);
    });
  }
}
