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
  sequencePlotPath: string = "http://localhost:8000/api/media/output_plots/sequence_"
  errorMessage: string | null = null;
  columnKeys: (keyof SequenceModel)[] = ['id', 'title', 'sequence', 'PSH', 'PSM_ID', 'accession', 'unique', 'database', 'database_version', 'search_engine', 'search_engine_score_1', 'modifications', 'retention_time', 'charge_x', 'exp_mass_to_charge', 'calc_mass_to_charge', 'spectra_ref', 'pre', 'post', 'start', 'end', 'opt_ms_run_1_aa_scores', 'scan_number', 'pepmass', 'charge_y', 'scans', 'rtinseconds', 'seq', 'mz_array', 'intensity_array', 'charge_array'];

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private sequenceService: SequenceService
  ) { }

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
      next: (data: any) => {
        this.sequenceData = {
          ...data,
          intensity_array: data['intensity array'],
          mz_array: data['m/z array'],
          charge_array: data['charge array']
        };
        // this.sequenceData = data;
        this.errorMessage = null;
        console.log(this.sequenceData)
      },
      error: (err) => {
        this.sequenceData = null;
        this.errorMessage = 'Sequence not found';
      }
    });
  }
}
