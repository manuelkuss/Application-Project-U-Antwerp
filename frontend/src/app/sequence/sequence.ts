import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SequenceService } from '../services/sequence-service';
import { SequenceModel } from '../models/sequence.model';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-sequence',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  providers: [SequenceService],
  templateUrl: './sequence.html',
  styleUrl: './sequence.scss',
})
export class Sequence {
  sequenceId: number | null = null;
  sequenceData: SequenceModel | null = null;
  errorMessage: string | null = null;

  constructor(
    private route: ActivatedRoute, 
    private router: Router,
    private sequenceService: SequenceService
  ) {}

  ngOnInit() {
    const id = this.route.snapshot.paramMap.get('id');
    console.log("id: ", id);
    if (id) {  
      this.sequenceId = +id;
      this.fetchSequence(+id);
    }
  }

  onIdChange(id: number | null) {
    if (!id) return;

    // Update URL without reloading
    this.router.navigate(['/sequence', id]);

    // Fetch data
    this.fetchSequence(id);
  }

  fetchSequence(id: number | null) {
    if (this.sequenceId == null) {
      this.errorMessage = 'Please enter a valid ID';
      this.sequenceData = null;
      return;
    }

    this.sequenceService.getSequence(this.sequenceId).subscribe({
      next: (data) => {
        this.sequenceData = data;
        this.errorMessage = null;
      },
      error: (err) => {
        this.sequenceData = null;
        this.errorMessage = 'Sequence not found';
      }
    });
  }
}
