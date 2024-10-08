import { Component } from '@angular/core';
import { ButtonComponent } from '../../components/button/button.component';
import { FileinputComponent } from '../../components/fileinput/fileinput.component';
import { ResultComponent } from '../../components/result/result.component';

import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';

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

  constructor(private http: HttpClient) {}

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
    const formData = new FormData();
    formData.append('image', this.submittedFile);

    this.http.post('http://localhost:5000/upload_image', formData).subscribe({
      next: () => this.getProcessedImage(),
      error: (err) => console.error(err)
    })
  }

  getProcessedImage() {
    this.http.get('http://localhost:5000/get_image', {responseType: 'blob'}).subscribe({
      next: (blob) => {
        const url = URL.createObjectURL(blob);
        this.resultImageUrl = url
      },
      error: (err) => console.log(err)
    })
  }

}
