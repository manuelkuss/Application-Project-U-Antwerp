import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { SequenceViewerService } from '../services/sequence-viewer-service';
import { MgfFile } from '../models/mgfFile.model';
import { FormsModule } from '@angular/forms';
import { SequenceModel } from '../models/sequence.model';
import { Sequence } from '../sequence/sequence';
import vegaEmbed from 'vega-embed';
import { environment } from '../../environments/environment';

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

  selectedSequenceId: number | null = null;
  sequenceData: SequenceModel | null = null;
  sequenceiPlotPath: string = environment.mediaUrl + "output_iplots/sequence_"
  columnKeys: (keyof SequenceModel)[] = ['id', 'title', 'sequence', 'PSH', 'PSM_ID', 'accession', 'unique', 'database', 'database_version', 'search_engine', 'search_engine_score_1', 'modifications', 'retention_time', 'charge_x', 'exp_mass_to_charge', 'calc_mass_to_charge', 'spectra_ref', 'pre', 'post', 'start', 'end', 'opt_ms_run_1_aa_scores', 'scan_number', 'pepmass', 'charge_y', 'scans', 'rtinseconds', 'seq', 'mz_array', 'intensity_array', 'charge_array'];

  errorMessage: string | null = null;
  errorOccurred: boolean = false;

  chartHeight: number = 100;


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
          this.selectedSequenceId = this.sequenceData.id;

          setTimeout(() => this.renderPlot(), 0);
        },
        error: (err) => {
          this.errorMessage = err;
          this.errorOccurred = true;
        }
      });
    }
  }

  onMgfFileChange(selectedId: string): void {

    this.mgfFileSequences.forEach((seqModel: SequenceModel) => {
      if (seqModel.id == Number(selectedId)) {
        this.sequenceData = seqModel;
        
        setTimeout(() => this.renderPlot(), 0);
      }
    });
  }

  onHeightChange() {
    this.renderPlot();
  }

  renderPlot() {

    var spec = this.sequenceiPlotPath + this.sequenceData?.id + '.json';

    console.log("path: ", spec);

    var opt = {
      actions: true,
      height: this.chartHeight,
    };

    this.errorOccurred = false;
    vegaEmbed('#vis', spec, opt)
      .catch((err) => {
        this.errorMessage = "Sequence json " + spec + " not found!";
        this.errorOccurred = true;
        console.log("test", err);
      });

  }
}
