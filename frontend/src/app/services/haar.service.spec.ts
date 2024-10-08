import { TestBed } from '@angular/core/testing';

import { HaarService } from './haar.service';

describe('HaarService', () => {
  let service: HaarService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HaarService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
