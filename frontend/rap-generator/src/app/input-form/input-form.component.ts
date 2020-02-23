import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { MlService } from '../ml.service';
import {Observable} from 'rxjs';

@Component({
  selector: 'app-input-form',
  templateUrl: './input-form.component.html',
  styleUrls: ['./input-form.component.css']
})
export class InputFormComponent implements OnInit {
  submitted = false;
  inputForm;
  generatedText: string;

  constructor(private formBuilder: FormBuilder, private mlService: MlService) {
    this.inputForm = this.formBuilder.group({
      seed: ''
    });
  }

  ngOnInit(): void {
  }

  onSubmit(seed: string) {
    this.submitted = true;
  //  communication model
    this.mlService.sendSeed(seed).subscribe(
      x => this.onSuccessResponse(x)
    );
  }

  onSuccessResponse(response) {
    this.generatedText = response;
  }

}
