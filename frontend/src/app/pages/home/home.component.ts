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
  choiceValue: string | null = null;

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

  onFaceSelected() {
    this.choiceValue = "Face"
  }

  onEyesSelected() {
    this.choiceValue = "Eyes"
  }

  onSubmit() {
    if(!this.submittedFile) {
      alert("Nenhum arquivo encontrado")
      return
    }else if(!this.choiceValue) {
      alert("Nenhuma opção de detecção selecionada")
      return
    }


    this.haarService.uploadImage(this.submittedFile, this.choiceValue).subscribe({
      next: () => this.getProcessedImage(),
      error: (err) => alert("Não foi possível enviar imagem. Erro: " + err)
    })
  }

  getProcessedImage() {
    this.haarService.getProcessedImage().subscribe({
      next: (blob) => {
        const url = URL.createObjectURL(blob);
        this.resultImageUrl = url
      },
      error: (err) => alert("Não foi possivel receber imagem processada. Erro: " + err)
    })
  }

}
