import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SequenceViewer } from './sequence-viewer';

describe('SequenceViewer', () => {
  let component: SequenceViewer;
  let fixture: ComponentFixture<SequenceViewer>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SequenceViewer]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SequenceViewer);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
