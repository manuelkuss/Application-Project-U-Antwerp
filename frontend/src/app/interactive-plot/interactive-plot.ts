import { Component, Input, AfterViewInit, OnChanges, SimpleChanges } from '@angular/core';
import vegaEmbed from 'vega-embed';
import { tooltip } from 'vega-lite/types_unstable/compile/mark/encode/tooltip.js';

@Component({
  selector: 'app-interactive-plot',
  imports: [],
  templateUrl: './interactive-plot.html',
  styleUrl: './interactive-plot.scss',
})
export class InteractivePlot {
  hasRendered = false;

  ngAfterViewInit() {
    this.renderPlot();
  }

  ngOnChanges(changes: SimpleChanges) {
    if (this.hasRendered) {
      this.renderPlot();
    }
  }

  renderPlot() {
    var spec = 'https://raw.githubusercontent.com/vega/vega/master/docs/examples/bar-chart.vg.json';
    
    var spec2 = 'http://localhost:8000/api/media/iplot_spectrum.json';

    var opt = {actions: true}; 

    // const data = fetch('./iplot_spectrum.json');
    // console.log(data);

    vegaEmbed('#vis', spec2, opt);
  }

  // renderPlot() {
  //   var spec = 'https://raw.githubusercontent.com/vega/vega/master/docs/examples/bar-chart.vg.json';

  //   this.hasRendered = true;

  //   const mz = this.spectrumData.mz;
  //   const intensity = this.spectrumData.intensity;

  //   const data = mz.map((value: number, index: number) => ({
  //     mz: value,
  //     intensity: intensity[index]
  //   }));

  //   const spec: any = {
  //     "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  //     "width": "container",
  //     "height": 400,
  //     "data": { "values": data },
  //     "mark": "bar",
  //     "encoding": {
  //       "x": {
  //         "field": "mz",
  //         "type": "quantitative",
  //         "title": "m/z"
  //       },
  //       "y": {
  //         "field": "intensity",
  //         "type": "quantitative",
  //         "title": "Intensity"
  //       },
  //       "tooltip": [
  //         {"field": "mz", "type": "quantitative"},
  //         {"field": "intensity", "type": "quantitative"}
  //       ]
  //     }
  //   };

  //   embed('#vis', spec, { actions: false });
  // }
}
