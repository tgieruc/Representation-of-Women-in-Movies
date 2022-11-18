# ADA 2022 Project :  ALL Goats Are Troublemakers

# The Representation of Women in Movies 
___Behind the Camera to on the Screen__

## Abstract
Society has made massive progress regarding women’s rights within the last century, but can we see that change in the movies that we watch? Laws and general societal outlook has changed, but the way women are viewed by everyday people around them may not have changed as much. Movies provide us a unique insight into the subconscious ways that society is conditioned to view women and capture the ideals and norms of the time they were produced. From actresses on screen to the story itself, within film there potentially lies some hidden truth about how far we have come to addressing gender inequality. Through the exploratory analysis of directors and writers, movie characters, and actors centered around the CMU Movie Summary Corpus dataset, the group aims to get a better understanding of how women are and have been represented in media.

## Research Questions
**Creative Direction: Who are telling the stories?**

How have movie directors and writers progressed in terms of gender? Where are women participating as directors and writers? What are the dynamics and are there any pivoting figures?

**Common Characters: What kinds of stories are being told?**

What types of female characters are prevalent in the data? How are Women portrayed? What are the common associations across female characters? 

**Character Portrayal: Who do we watch in the theatre?**

What women are portrayed in movies? How is age diversity evolving yearly? Do male and female actor play in the same genre of movies? Are females equally represented in leading and minor roles?
  
## Additional Datasets

* [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page): a free and open knowledge database with structured data from its Wikimedia sister projects, such as Wikipedia and Wikitionary. This database is used to crosscheck and complete our original CMU dataset. The database was queried using GET requests and wikidata IDs extracted from [Freebase ID - Wikidata ID mapping](https://developers.google.com/freebase#freebase-wikidata-mappings) and from the wikipedia page of movies. 
* [IMDB](https://www.imdb.com/interfaces/): an online database of information related to films, television series, cast and crews.Used for crosschecking and gaining additional movie data, character data, and director and writer data.
* [Stanford CoreNLP-processed summaries](http://www.cs.cmu.edu/~ark/personas/data/corenlp_plot_summaries.tar):
  42,306 plot summaries used in CMU Movie Summary Corpus dataset run through the Stanford CoreNLP pipeline. The data is stored per movie in XML format (structure shown in Data Handling.ipynb). The group can use this dataset to extract character descriptors as defined in [Learning Latent Personas of Film Characters](http://www.cs.cmu.edu/~dbamman/pubs/pdf/bamman+oconnor+smith.acl13.pdf) by David Bamman, Brendan O'Connor, and Noah A. Smith.

  
## Methods
### Initial data collection and cleaning (Data Handling.ipynb)
* **Wikidata**: This database is used to crosscheck and complete our original CMU dataset. We have queried the database using GET requests, with wikidata IDs extracted from [Freebase ID - Wikidata ID mapping](https://developers.google.com/freebase#freebase-wikidata-mappings) and from the wikipedia page of movies.
  * Movie release date, runtime, and box office revenue was extracted to crosscheck CMU dataset and the review score, IMDB ID and BoxOffice Mojo ID in order to supplement it.
  * Character gender, date of birth and ethnicity was extracted in order to crosscheck the CMU dataset, and number of notable movies and the IMDB ID to supplement it.
  * Director and Writer gender, date of birth, ethnicity, and height data was extracted to create a director and writers dataset to analyze alongside the CMU movie dataset to understand how Females are represented behind the camera.

* **IMDB**: Title.basics was used to get the release year, runtime, and genre of movies, title.crew was used for directors and writers biometrics, title.ratings for average ratings and number of votes for movies, and name.basics for crosschecking the year of birth of actors. Datasets were merged using the IMDB IDs extracted from Wikidata.

* **Stanford CoreNLP-processed summaries**:
XML data was handled using gzip and lxml etree. The descriptors are defined by the type of dependency that they have in relation to a character of interest (agent verbs: nsubj or agent, patient verbs: dobj, nsubjpass, iobj, or any prepositional argument prep*). Once a relevant word was found the lemma was also extracted.

* **Movie & Character datasets**: Wikidata and IMDb were used to complete and crosscheck the original CMU dataset. Overall, 12530 entries were added to existing categories of the CMU character dataset and 15793 entries were modified. 17937 new entries were added to existing categories in the CMU move dataset and 1554 were modified. 68341 ratings of movies and 74200 directors and writers were added as well.


### Analysis
**Investigate trends in director and writer data (Director Dataset Analysis.ipynb)**

Exploratory analysis was done to understand the proportion of female and male directors and writers as well as biometric breakdown of each group (male directors, female directors, male writers, female writers). Data was visualized over the entire dataset and then broken down by year, movie genre, and top 1000 rated movies. The top 1000 movies were analyzed to understand what trends may exist within the most successful movies and if those differ from the trends seen overall.

**Investigate trends in character descriptors (Character Terms Analysis.ipynb)**

Qualitative analyses:
Looked at most frequent descriptors for different genres broken down by decade. Sampled genres and performed analysis within the genre. Checked for trends and if they were consistent within genres. Visualized with word clouds.

Clustering: clustering terms for different genres to get interpretable clusters

Embeddings tested: glove50d, glove100d, bert base (cls), bert base (bpe averages)

Clustering algorithms tested: DBScan, Agglomerative clustering (with a distance threshold), since a prior for a reasonable amount of clusters is not available. (cosine distance used as metric)

currently interpretable clusters have not been found, planning on doing a hyperparameter search for clustering algorithms. 
On the data side, planning on separating the descriptors based on the part of speech.
- Topic modelling
- Possibly, sentiment classification (on full sentences)
Quantitative analysis:
For each gender per decade analyze number of terms per decade, unique terms per character, share of positive / negative terms (paired with sentiment classification), diversity within clusters and of the clusters themselves


**Investigate trends in actor data (Actor Analysis.ipynb)**

movie and characters dataset was used to understand proportion of male and female actress in the industry as well as their age differences. The genres provided by IMDB were used to understand if actors and actresses played in different kinds of movies. Using webscraping a metric to evaluate the presence of females in major/minor roles was found.


## Proposed Timeline
* 19.11.2022:  Brainstorm data visualizations and begin homework 2
* 25.11.2022:  Finalize project direction given feedback for milestone 2
* 02.12.2022:  Hand in Homework 2 and begin final analyses
* 09.12.2022:  Draft outline for datastory, discuss what data visualization will be required
* 16.12.2022:  Have all analysis finished, final draft of datastory, begin website
* 21.12.2022:  complete website and start final review
* 22.12.2022:  Final tweaks
* 23.12.2022:  Hand in Milestone 3

## Team Structure
* Team member 1 - Analysis and visualization for RQ1, draft datastory
* Team member 2 - Analysis and visualization for RQ2, final review and editing
* Team member 3 - Analysis and visualization for RQ3, Help other members as needed
* Team member 4 - Available for help, in charge of putting together webpage