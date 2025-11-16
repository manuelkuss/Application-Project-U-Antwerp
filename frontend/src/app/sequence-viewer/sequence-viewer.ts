import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { SequenceViewerService } from '../services/sequence-viewer-service';
import { MgfFile } from '../models/mgfFile.model';
import { FormsModule } from '@angular/forms';
import { SequenceModel } from '../models/sequence.model';
import { Sequence } from '../sequence/sequence';
import vegaEmbed from 'vega-embed';

@Component({
  selector: 'app-sequence-viewer',
  imports: [CommonModule, HttpClientModule, FormsModule, Sequence],
  providers: [SequenceViewerService],
  templateUrl: './sequence-viewer.html',
  styleUrl: './sequence-viewer.scss',
})
export class SequenceViewer {
  mgfFiles: MgfFile[] = [];
  mgfFileSelected: MgfFile | undefined;
  mgfFileSequences: SequenceModel[] = [];
  mgfFileSequencesIds: number[] = [];

  sequenceData: SequenceModel | null = null;
  sequencePlotPath: string = "http://localhost:8000/api/media/output_plots/sequence_"
  columnKeys: (keyof SequenceModel)[] = ['id', 'title', 'sequence', 'PSH', 'PSM_ID', 'accession', 'unique', 'database', 'database_version', 'search_engine', 'search_engine_score_1', 'modifications', 'retention_time', 'charge_x', 'exp_mass_to_charge', 'calc_mass_to_charge', 'spectra_ref', 'pre', 'post', 'start', 'end', 'opt_ms_run_1_aa_scores', 'scan_number', 'pepmass', 'charge_y', 'scans', 'rtinseconds', 'seq', 'mz_array', 'intensity_array', 'charge_array'];

  errorMessage: string | null = null;


  constructor(private sequenceViewerService: SequenceViewerService) { }

  ngOnInit(): void {
    this.loadMgfFiles();
  }

  loadMgfFiles(): void {
    this.sequenceViewerService.getMgfFiles().subscribe({
      next: (data: MgfFile[]) => {
        console.log('Fetched mgf files:', data);
        this.mgfFiles = data;
        this.mgfFileSelected = this.mgfFiles[0];
        this.loadMgfFileInfo();
      },
      error: (err) => console.error('Error mgf files', err)
    });
  }

  loadMgfFileInfo(): void {
    if (this.mgfFileSelected) {
      this.sequenceViewerService.getMgfFileInfo(this.mgfFileSelected.name).subscribe({
        next: (data: any) => {
          console.log("Fetchend mgf file info data: ", data);
          var sequencesList: SequenceModel[] = [];
          var sequencesIdsList: number[] = [];
          data.forEach((sequence: any) => {
            // console.log("sequence: ", sequence);
            sequencesList.push({
              ...sequence,
              intensity_array: sequence['intensity array'],
              mz_array: sequence['m/z array'],
              charge_array: sequence['charge array']
            });
            sequencesIdsList.push(sequence.id);
          });
          this.mgfFileSequences = sequencesList;
          this.mgfFileSequencesIds = sequencesIdsList;
        },
        complete: () => {
          console.log(this.mgfFileSequences);
          this.sequenceData = this.mgfFileSequences[0];
          this.renderPlot();
        },
        error: (err) => {
          this.errorMessage = err;
        }
      });
    }
  }

  onMgfFileChange(selectedId: string): void {
    
    this.mgfFileSequences.forEach((sequenceModel: SequenceModel) => {
      if (sequenceModel.id == Number(selectedId)) {
        this.sequenceData = sequenceModel;
      }
    });
    
    this.renderPlot();

  }

  renderPlot() {

    var spec = 'http://localhost:8000/api/media/output_iplots/' + 'sequence_' + this.sequenceData?.id + '.json';

    var opt = { actions: true };

    vegaEmbed('#vis', spec, opt);
    
  }
}
