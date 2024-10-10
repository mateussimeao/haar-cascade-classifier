import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HaarService {

  private apiUrl = 'http://localhost:5000'

  constructor(private http: HttpClient) { }

  // Post
  uploadImage(file: File, choice: string): Observable<any> {
    const formData = new FormData()
    formData.append('image', file)
    formData.append('choice', choice)
    return this.http.post(`${this.apiUrl}/upload_image`, formData)
  }

  // Get
  getProcessedImage(): Observable<Blob> {
    return this.http.get(`${this.apiUrl}/get_image`, {responseType: 'blob'})
  }

}
