export interface SequenceModel {
  id: number;
  title: string;
  sequence: string;
  PSH?: string;
  PSM_ID?: number;
  accession?: string | null;
  unique?: string | null;
  database?: string | null;
  database_version?: string | null;
  search_engine?: string;
  search_engine_score_1?: number;
  modifications?: string | null;
  retention_time?: number | null;
  charge_x?: number;
  exp_mass_to_charge?: number;
  calc_mass_to_charge?: number;
  spectra_ref?: string;
  pre?: string | null;
  post?: string | null;
  start?: number | null;
  end?: number | null;
  opt_ms_run_1_aa_scores?: string;
  scan_number?: number;
  pepmass?: string;
  charge_y?: string;
  scans?: string;
  rtinseconds?: number;
  seq?: string;
  mz_array?: number[];         // converted from m/z array
  intensity_array?: number[];  // converted from intensity array
  charge_array?: (number | null)[]; // charge array may have '--' -> null
}
