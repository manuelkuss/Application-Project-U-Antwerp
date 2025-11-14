import { TestBed } from '@angular/core/testing';

import { Sequence } from './sequence';

describe('Sequence', () => {
  let service: Sequence;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Sequence);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
