<h1 align="center">The Representation of Women in Movies </h1>
<h3 align="center"><i>From Behind the Camera to on the Screen</i></h3>
<h4 align="center"><a href="https://epfl-ada.github.io/ada-2022-project-allgoatsaretroublemakers/">Visit our Website for the Data Story!</a></h4>

<br>

---

## Abstract
The representation of women in media has long been a topic of interest, as it reflects societal norms and attitudes towards gender equality. Despite the progress made in recent decades towards gender equality, it is important to examine whether these changes are reflected in the films we watch. Movies provide a unique insight into the subconscious ways in which society is conditioned to view women, and can capture the ideals and norms of the time in which they were produced. 

In this data analysis project, we will use the CMU Movie Summary Corpus dataset, completed with additional datasets, to explore the portrayal of women in film. We will not only analyze the roles of actresses and characters, but also of writers and directors. By analyzing these factors, we aim to gain a deeper understanding of how women are and have been represented in media, and how this has evolved through time.

---

## Research Questions
**Creative Direction: Who are telling the stories?**

How have movie directors and writers progressed in terms of gender? Where are women participating as directors and writers? What are the dynamics and are there any pivoting figures?

**Common Characters: What kinds of stories are being told?**

What types of female characters are prevalent in the data? How are Women portrayed? What are the common associations across female characters? 

**Character Portrayal: Who do we watch in the theatre?**

What women are portrayed in movies? How is age diversity evolving yearly? Do male and female actor play in the same genre of movies? Are females equally represented in leading and minor roles?

---

## Additional Datasets

* [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page): a free and open knowledge database with structured data from its Wikimedia sister projects, such as Wikipedia and Wikitionary. This database is used to crosscheck and complete our original CMU dataset. The database was queried using GET requests and wikidata IDs extracted from [Freebase ID - Wikidata ID mapping](https://developers.google.com/freebase#freebase-wikidata-mappings) and from the wikipedia page of movies. 
* [IMDB](https://www.imdb.com/interfaces/): an online database of information related to films, television series, cast and crews.Used for crosschecking and gaining additional movie data, character data, and director and writer data.
* [Stanford CoreNLP-processed summaries](http://www.cs.cmu.edu/~ark/personas/data/corenlp_plot_summaries.tar):
  42,306 plot summaries used in CMU Movie Summary Corpus dataset run through the Stanford CoreNLP pipeline. The data is stored per movie in XML format (structure shown in Data Handling.ipynb). The group can use this dataset to extract character descriptors as defined in [Learning Latent Personas of Film Characters](http://www.cs.cmu.edu/~dbamman/pubs/pdf/bamman+oconnor+smith.acl13.pdf) by David Bamman, Brendan O'Connor, and Noah A. Smith.

---

## Data collecting and cleaning ([Data Handling.ipynb](Data%20Handling.ipynb))
* **Wikidata**: This database is used to crosscheck and complete our original CMU dataset. We have queried the database using GET requests, with wikidata IDs extracted from [Freebase ID - Wikidata ID mapping](https://developers.google.com/freebase#freebase-wikidata-mappings) and from the wikipedia page of movies.
  * Movie release date, runtime, and box office revenue was extracted to crosscheck CMU dataset and the review score, IMDB ID and BoxOffice Mojo ID in order to supplement it.
  * Character gender, date of birth and ethnicity was extracted in order to crosscheck the CMU dataset, and number of notable movies and the IMDB ID to supplement it.
  * Director and Writer gender, date of birth, ethnicity, and height data was extracted to create a director and writers dataset to analyze alongside the CMU movie dataset to understand how Females are represented behind the camera.

* **IMDB**: Title.basics was used to get the release year, runtime, and genre of movies, title.crew was used for directors and writers biometrics, title.ratings for average ratings and number of votes for movies, and name.basics for crosschecking the year of birth of actors. Datasets were merged using the IMDB IDs extracted from Wikidata.

* **Stanford CoreNLP-processed summaries**:
XML data was handled using gzip and lxml etree. The descriptors are defined by the type of dependency that they have in relation to a character of interest (agent verbs: nsubj or agent, patient verbs: dobj, nsubjpass, iobj, or any prepositional argument prep*). Once a relevant word was found the lemma was also extracted.

* **Movie & Character datasets**: Wikidata and IMDb were used to complete and crosscheck the original CMU dataset. Overall, 12530 entries were added to existing categories of the CMU character dataset and 15793 entries were modified. 17937 new entries were added to existing categories in the CMU move dataset and 1554 were modified. 68341 ratings of movies and 74200 directors and writers were added as well.

---

## Analysis

### **Investigate trends in character descriptors ([Character Terms Analysis.ipynb](Character%20Terms%20Analysis.ipynb))**

**Qualitative analysis**:

- Analyzing wordclouds of gender-spefic character attributes per decade

- Clustering the attributes to get a better understanding of the trends (and to mitigate the lack of synonymity coverage using embeddings) 

Embeddings tested: glove50d, glove100d, bert base (cls), bert base (bpe averages), fasttext (trained on movie plots).

Clustering algorithms tested: DBScan, Agglomerative clustering (with a distance threshold).

**Quantitive analysis**:

- Character and main character distributions for genders per decade

- Numer and share of unique attributes for genders per decade

- Sentiment classification and topic detection

- Regression analysis based on the share of females for the targets of movie plot sentiment, lexical categories of aggression, dispute, violence



---

## Team Structure :goat:
* Ali - Analysis and visualization for RQ1, draft datastory
* Guillaume - Analysis and visualization for RQ2, final review and editing
* Arina - Analysis and visualization for RQ3, Help other members as needed
* Théo - Available for help, in charge of putting together webpage
