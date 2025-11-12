// type from Django
export interface ChartDataResponse {
  title: string;
  mz: number[];
  intensity: number[];
}

export interface ChartSeries {
  name: string;
  series: { name: number; value: number }[]; // numeric x-axis
}

// type for displaying charts
// export interface ChartData {
//   title: string;
//   data: { name: string; value: number }[];
// }