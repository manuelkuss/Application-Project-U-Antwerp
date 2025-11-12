import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChartsNxt } from './charts-nxt';

describe('ChartsNxt', () => {
  let component: ChartsNxt;
  let fixture: ComponentFixture<ChartsNxt>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ChartsNxt]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ChartsNxt);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
