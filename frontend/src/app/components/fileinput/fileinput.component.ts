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
  selectedFace: boolean = false
  selectedEyes: boolean = false

  @Output() fileSelected = new EventEmitter<File | null>();
  @Output() faceSelected = new EventEmitter<boolean>()
  @Output() eyesSelected = new EventEmitter<boolean>()

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0]
    this.fileSelected.emit(this.selectedFile)
  }

  onFaceSelected() {
    this.selectedFace = true
    this.faceSelected.emit(this.selectedFace)
  }
  onEyesSelected() {
    this.selectedEyes = true
    this.eyesSelected.emit(this.selectedEyes)
  }

}
