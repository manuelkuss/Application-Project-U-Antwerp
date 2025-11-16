import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InteractivePlot } from './interactive-plot';

describe('InteractivePlot', () => {
  let component: InteractivePlot;
  let fixture: ComponentFixture<InteractivePlot>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [InteractivePlot]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InteractivePlot);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
