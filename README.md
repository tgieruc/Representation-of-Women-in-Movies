# ADA 2022 Project :  ALL Goats Are Troublemakers

# Representation of Women in Movies: Behind the Camera to on the Screen

## Abstract
Society has made massive progress regarding women’s rights within the last century, but can we see that change in the movies that we watch? Laws and general societal outlook has changed, but the way women are viewed by everyday people around them may not have changed as much. Movies provide us a unique insight into the subconscious ways that society is conditioned to view women and capture the ideals and norms of the time they were produced. From actresses on screen to the story itself, within film there potentially lies some hidden truth about how far we have come to addressing gender inequality. Through the exploratory analysis of directors and writers, movie characters, and actors centered around the CMU Movie Summary Corpus dataset, the group aims to get a better understanding of how women are and have been represented in media.

## Research Questions
**Creative Direction: Who is telling the stories?**
How have movie directors and writers progressed in terms of gender? Where are women participating as directors and writers? What are the dynamics and are there any pivoting figures?

**Common Characters: What kinds of stories are being told?**
What types of female characters are prevalent in the data? How are Women portrayed? What are the common associations across female characters? 

**Character Portrayal: Who do we watch in the theatre?**
What women are portrayed in movies? How is age diversity evolving yearly? Are females equally represented in leading and minor roles? How do actresses affect the success of a movie?
  
## Additional Datasets

* [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page): a free and open knowledge database with structured data from its Wikimedia sister projects, such as Wikipedia and Wikitionary. This database is used to crosscheck and complete our original CMU dataset. We have queried the database using GET requests, with wikidata IDs extracted from [Freebase ID - Wikidata ID mapping](https://developers.google.com/freebase#freebase-wikidata-mappings) and from the wikipedia page of movies.
  * For the movies, we have extracted the release date, the runtime and the box office revenue in order to crosscheck the CMU dataset, and the review score, IMDB ID and BoxOffice Mojo ID in order to complete it.
  * For the characters, we have extracted the gender, date of birth and ethnicity in order to crosscheck the CMU dataset, and the number of notable movies and the IMDB ID to complete the dataset.
  * For the directors and writers, we have extracted the gender, date of birth, ethnicity, and height data to create a directors and wrtiers dataset to analyze along side the CMU moviedata set. This was done to understand how Females are represented behind the camera.

* [Stanford CoreNLP-processed summaries](http://www.cs.cmu.edu/~ark/personas/data/corenlp_plot_summaries.tar)
 contains all 42,306 plot summaries used in CMU Movie Summary Corpus dataset analysis run through the Stanford CoreNLP pipeline (tagging, parsing, NER and coref). The data is stored per movie in XML format (XML structure shown in Data Handling.ipynb). The group can use this data set to extract character descriptors as defined in the paper [Learning Latent Personas of Film Characters](http://www.cs.cmu.edu/~dbamman/pubs/pdf/bamman+oconnor+smith.acl13.pdf) by David Bamman, Brendan O'Connor, and Noah A. Smith.

  
## Methods
### Initial data collection and cleaning
**Wikidata**

**Stanford CoreNLP-processed summaries**
XML data was handled and parsed using gzip and lxml etree. The descriptors are defined by the type of dependency that they have in relation to a character of interest (agent verbs: nsubj or agent, patient verbs: dobj, nsubjpass, iobj, or any prepositional argument prep*). Once a relvent word was found the lemma of the word was also extracted.

**Movie dataset**

**Character dataset**

### Analysis
**Investigate trends in director and writer data:** Director Dataset Analysis.ipynb
Exploratory analysis was done in the dataset to understand the proportion of female and male directors and writers as well as the biometric breakdown of each group (male directors, female directors, male writers, female writers). Data was visualized over the entire dataset and then broken down by year, movie genre, and top 1000 rated movies. The top 1000 movies over the entire dataset were analyzed to understand what trends may exist within the most successful movies and if those differ from the trends seen overall.
**Investigate trends in character descriptors**

**Investigate trends in actor data**


## Proposed Timeline
* 19.11.2022:  brainstorm data visualizations and begin homework 2
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
* Team member 4 - Available for help, incharge of putting together webpage
