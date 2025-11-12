import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChartsPlotly } from './charts-plotly';

describe('ChartsPlotly', () => {
  let component: ChartsPlotly;
  let fixture: ComponentFixture<ChartsPlotly>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ChartsPlotly]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ChartsPlotly);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
