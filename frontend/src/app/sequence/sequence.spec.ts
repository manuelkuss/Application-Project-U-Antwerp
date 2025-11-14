import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Sequence } from './sequence';

describe('Sequence', () => {
  let component: Sequence;
  let fixture: ComponentFixture<Sequence>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Sequence]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Sequence);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
