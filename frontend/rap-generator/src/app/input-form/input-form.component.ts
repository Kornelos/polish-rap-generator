import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
@Component({
  selector: 'app-input-form',
  templateUrl: './input-form.component.html',
  styleUrls: ['./input-form.component.css']
})
export class InputFormComponent implements OnInit {
  submitted = false;
  inputForm;

  constructor(private formBuilder: FormBuilder) {
    this.inputForm = this.formBuilder.group({
      seed: ''
    });
  }

  ngOnInit(): void {
  }

  onSubmit(seed: string) {
    this.submitted = true;
  //  communication model
  }
}
