# ADA 2022 Project :  ALL Goats Are Troublemakers

## The role of female characters throughout time.
Our society has made massive progress regarding female rights within the last century. But is the media field reflective of that? To consider this question, one can look at the problem from three different angles: movie production, cast and portrayed characters.
* How did the movie production landscape change during the last century? Are women participating in the creation process as directors, screenwriters and operators? What are the dynamics and are there any pivoting figures in this movement?
* What types of women are portrayed in movies? How are racial and age diversity evolving year by year? Are females equally represented in leading and minor roles?
* What types of female characters are prevalent in the films in each period? Are females portrayed as weak or strong? Primitive or complex? Helpless or independent? Are they usually positive or negative characters? How does this depend on the time the movie was produced and on the genre?


## Organisation of the repo
```
.
├── data *all the data*
│   ├── MovieSummaries *the original CMU dataset*
│   ├── IMDB *IMDB dataset*
│   └── pickles *the processed pickle files*
├── pipelines *jupyter notebooks for dataprocessing*
└── demo_jupyters *jupyter notebooks explaining dataprocessing steps*
```  
## Additional Datasets

* [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page): a free and open knowledge database with structured data from its Wikimedia sister projects, such as Wikipedia and Wikitionary. This database is used to crosscheck and complete our original CMU dataset. We have queried the database using GET requests, with wikidata IDs extracted from [Freebase ID - Wikidata ID mapping](https://developers.google.com/freebase#freebase-wikidata-mappings) and from the wikipedia page of movies.
  * For the movies, we have extracted the release date, the runtime and the box office revenue in order to crosscheck the CMU dataset, and the review score, IMDB ID and BoxOffice Mojo ID in order to complete it.
  * For the characters, we have extracted the gender, date of birth and ethnicity in order to crosscheck the CMU dataset, and the number of notable movies and the IMDB ID to complete the dataset.
  * For the directors and writers, we have extracted the gender, date of birth, ethnicity, and height data to create a directors and wrtiers dataset to analyze along side the CMU moviedata set. This was done to understand how Females are represented behind the camera.


  
## Methods


