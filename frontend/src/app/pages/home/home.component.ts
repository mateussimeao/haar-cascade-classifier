import { Component } from '@angular/core';
import { ButtonComponent } from '../../components/button/button.component';
import { FileinputComponent } from '../../components/fileinput/fileinput.component';
import { ResultComponent } from '../../components/result/result.component';

import { CommonModule } from '@angular/common';
import { HaarService } from '../../services/haar.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [ButtonComponent, FileinputComponent, ResultComponent, CommonModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {
  submittedFile: File | null = null;
  submittedImageUrl: string | null = null;
  resultImageUrl: string | null = null;

  constructor(private haarService: HaarService) {}

  onFileSelected(file: File | null) {
    this.submittedFile = file
    if(file) {
      const reader = new FileReader()
      reader.onload = () => {
        this.submittedImageUrl = reader.result as string
      }
      reader.readAsDataURL(file)
    }else {
      this.submittedImageUrl = null
    }
  }

  onSubmit() {
    if(!this.submittedFile) {
      console.log("Nenhum arquivo encontrado")
      return
    }

    this.haarService.uploadImage(this.submittedFile).subscribe({
      next: () => this.getProcessedImage(),
      error: (err) => console.error(err)
    })
  }

  getProcessedImage() {
    this.haarService.getProcessedImage().subscribe({
      next: (blob) => {
        const url = URL.createObjectURL(blob);
        this.resultImageUrl = url
      },
      error: (err) => console.log(err)
    })
  }

}
