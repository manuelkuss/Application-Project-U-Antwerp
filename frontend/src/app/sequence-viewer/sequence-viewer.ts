import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { SequenceViewerService } from '../services/sequence-viewer-service';
import { MgfFile } from '../models/mgfFile.model';
import { FormsModule } from '@angular/forms';
import { SequenceModel } from '../models/sequence.model';
import vegaEmbed from 'vega-embed';
import { environment } from '../../environments/environment';

const CHART_HEIGHT = 300;

@Component({
  selector: 'app-sequence-viewer',
  imports: [CommonModule, HttpClientModule, FormsModule],
  providers: [SequenceViewerService],
  templateUrl: './sequence-viewer.html',
  styleUrl: './sequence-viewer.scss',
})
export class SequenceViewer {
  mgfFiles: MgfFile[] = [];
  mgfFileSelectedName: string | undefined;
  mgfFileSequences: SequenceModel[] = [];
  mgfFileSequencesIds: number[] = [];

  selectedSequenceId: number | null = null;
  sequenceData: SequenceModel | null = null;
  sequenceiPlotPath: string | null = null;
  columnKeys: (keyof SequenceModel)[] = ['id', 'title', 'sequence', 'PSH', 'PSM_ID', 'accession', 'unique', 'database', 'database_version', 'search_engine', 'search_engine_score_1', 'modifications', 'retention_time', 'charge_x', 'exp_mass_to_charge', 'calc_mass_to_charge', 'spectra_ref', 'pre', 'post', 'start', 'end', 'opt_ms_run_1_aa_scores', 'scan_number', 'pepmass', 'charge_y', 'scans', 'rtinseconds', 'seq', 'mz_array', 'intensity_array', 'charge_array'];

  errorMessage: string | null = null;
  errorOccurred: boolean = false;

  chartHeight: number = CHART_HEIGHT;


  constructor(private sequenceViewerService: SequenceViewerService) { }

  ngOnInit(): void {
    this.loadMgfFiles();
  }

  loadMgfFiles(): void {
    this.sequenceViewerService.getMgfFiles().subscribe({
      next: (data: MgfFile[]) => {
        console.log('Fetched mgf files:', data);
        this.mgfFiles = data;
        this.mgfFileSelectedName = this.mgfFiles[0].name;
        this.sequenceiPlotPath = environment.mediaUrl + "output_iplots/" + this.mgfFiles[0].name + "/sequence_"
        this.loadMgfFileInfo();
      },
      error: (err) => console.error('Error mgf files', err)
    });
  }

  loadMgfFileInfo(): void {
    console.log("loadMgfFileInfo: this.mgfFileSelectedName: ", this.mgfFileSelectedName);
    if (this.mgfFileSelectedName) {
      this.sequenceViewerService.getMgfFileInfo(this.mgfFileSelectedName).subscribe({
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
          this.errorMessage = "Information CSV file for this mgf file does not exist and could not be generated.";
          this.errorOccurred = true;
        }
      });
    }
  }

  onMgfFileChange(selectedMgfFile: string): void {
    this.mgfFileSelectedName = String(selectedMgfFile);
    this.sequenceiPlotPath = environment.mediaUrl + "output_iplots/" + String(selectedMgfFile) + "/sequence_"

    console.log("onMgfFileChange -> selected mgf file: ", this.mgfFileSelectedName);

    this.loadMgfFileInfo();
  }

  onSequenceChange(selectedId: string): void {

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

    if (this.sequenceiPlotPath) {
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
}
