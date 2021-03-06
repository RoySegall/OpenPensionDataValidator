import {Component, OnInit, Injectable} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {HttpClient} from '@angular/common/http';
import {ResultsService} from "../results.service";
import {ResultsInterface} from "../ResultsInterface";


@Component({
  selector: 'op-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.scss']
})

@Injectable()
export class ResultsComponent implements OnInit {

  results: any;
  id = '';
  stats = {
    filesCount: 0,
    errors: [],
  };
  originalResults: any;
  showEmptyResults = false;
  processing: boolean;

  constructor(private route: ActivatedRoute, private http: HttpClient, private resultsService: ResultsService) {
  }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.id = params.id;

      // Todo: handle if not found.
      this.resultsService.getResults(params.id).subscribe( (response: ResultsInterface) => {
        this.results = Object.keys(response.results);
        this.originalResults = this.results;
        this.stats = {
        'filesCount': Object.keys(this.results).length,
        'errors': [
          {'text': 'מטבע לא מזוהה - שקל חדש', 'times': 5},
          {'text': 'מטבע לא מזוהה - כתר שבדי', 'times': 10},
          {'text': 'אחרי 0 צריכים להיות 2 מספרים', 'times': 9},
          {'text': 'DD/MM/YYYY הוא לא פורמט תקין', 'times': 30},
        ],
      };
      });
    });
  }

  filterFiles(event: any) {
    let text = event.target.value;
    this.results = this.originalResults;
    this.showEmptyResults = false;

    if (text == '') {
      this.results = this.originalResults;
      return;
    }

    this.results = this.results.filter(item => item.indexOf(text) != -1);

    if (this.results.length == 0) {
      this.showEmptyResults = true;
    }
  }

}
