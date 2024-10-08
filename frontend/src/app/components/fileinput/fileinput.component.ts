import { Component, Output, EventEmitter } from '@angular/core';
import { ButtonComponent } from '../button/button.component';

@Component({
  selector: 'app-fileinput',
  standalone: true,
  imports: [ButtonComponent],
  templateUrl: './fileinput.component.html',
  styleUrl: './fileinput.component.scss'
})
export class FileinputComponent {
  selectedFile: File | null = null;

  @Output() fileSelected = new EventEmitter<File | null>();

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0]
    this.fileSelected.emit(this.selectedFile)
  }

}
