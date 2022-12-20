---
title: The Representation of Women in Movies
subtitle: From Behind the Camera to on the Screen
---

<head>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
      extensions: ["tex2jax.js"],
      tex2jax: {
          inlineMath: [ ['$','$'], ["\\(","\\)"] ],
          processEscapes: true,
          processRefs: true,
          processEnvironments: true
      },
      TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>
<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
</head>




# Introduction

The representation of women in media has long been a topic of debate and scrutiny. While society has made significant progress in terms of gender equality over the past century, it is important to examine whether these changes are reflected in the films we watch. Movies have the ability to reveal societal norms and ideals, as well as the underlying beliefs and attitudes that shape our culture.

For this data analysis project, we will be using the [CMU Movie Summary Corpus dataset](https://www.cs.cmu.edu/~ark/personas/), as well as additional datasets from Stanford CoreNLP, IMDb, Wikidata, IMDB, and Box Office Mojo, to explore the portrayal of women in film, including the roles of actresses, characters, and writers and directors. Through our analysis, we hope to gain a deeper understanding of how women have been depicted in media over time and how this representation may have evolved. By examining these factors, we can gain insight into the ways that society views and treats women, and consider how far we have come in addressing gender inequality.



# The Data
Our analysis is based on merging the [CMU Dataset](https://www.cs.cmu.edu/~ark/personas/), the [Stanford CoreNLP-processed summaries](http://www.cs.cmu.edu/~ark/personas/data/corenlp_plot_summaries.tar), [IMDb](https://www.imdb.com/interfaces/), [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page), [IMDB](https://www.imdb.com/interfaces/) and [Box office Mojo](https://www.boxofficemojo.com/).

We have separated the data in three tables: 

* The movies table, that contains titles, release year, runtime, box office revenue, average rating and number of votes on IMDb, genre, as well as the list of directors and writers. We have a total of 81'741 different movies.

{% include movie_percentage.html %}


* The characters table, that contains the ID of the movie, the character name and actor name, their height, ethnicity, birth and death year, the movie metric and the actor metric. We have 450'669 characters played by 135'761 different actors.

{% include characters_percentage.html %}

* The directors and writers table, that contains titles, role (either director or writer), name, gender, birth year and height. We have a total of 86'474 directors and 164'271 writers.

{% include directors_percentage.html %}

## The Impact Score metric
### Movies
We have created a metric in order to measure the impact a movie has, based on their average rating and the number of votes. Our assumption is that an impactful movie has a lot votes and has either an extremely good or bad average rating.

We apply a logarithmic transformation to the number of votes, as this follows a power-law distribution. This allows us to normalize the data and accurately compare the impact of different movies.
Next, we take the absolute value of the normalized average rating for each movie. This accounts for both very good and very bad movies, as both have a significant impact on audience reception.
By combining these two factors, we are able to calculate the overall impact a movie has on its audience and compare this across different films.

$$\textrm{Impact Score}_\textrm{Movies} = \textrm{normalized} (\log(\textrm{number of votes})) \cdot \textrm{abs}(\textrm{normalized}(\textrm{IMDB rating}))$$

According to this metric, those are the top 10 most impactful movies of our dataset:

{% include top20_movies.html %}

### Actors, writers and directors
In order to apply this metric to actors, writers and directors, we decided to use the [Discounted Cumulative Gain](https://en.wikipedia.org/wiki/Discounted_cumulative_gain). 

For each actor, writer, or director, we first rank the movies they are linked to according to the impact score, in decreasing order. Then, we compute the discounted cumulative gain on this subset of movies using the following formula:

$$\textrm{Impact Score}_\textrm{Actors, Directors, Writers} = \sum_{i=1}^{\textrm{number of movies}}\frac{\textrm{movie metric}_i}{\log_2(i + 1)}$$

Here are the top 10 actors, writers and directors with the highest impact score:

{% include impact_score.html %}



# Where are the Women?

When it comes to the representation of women in media, the numbers are not encouraging. In recent years, women have made up a small percentage of actors, directors, and screenwriters in the film industry.

<!-- ![Representation of women in various roles in media](representation_of_women.png) -->

When it comes to genre, women are most often represented in dramas and comedies, while they are underrepresented in action and sci-fi films.

<!-- ![Genres in which women are represented](genre_representation.png) -->

# Behind the Camera

When it comes to directors, men outnumber women by a significant margin. However, there are some female directors who have made a significant impact in the industry.

<!-- ![Top female directors by box office performance](top_female_directors.png) -->

Some of the most successful female directors in recent years include Patty Jenkins, who directed the critically-acclaimed Wonder Woman, and Ava DuVernay, who directed the Oscar-nominated Selma.

# In Front of the Camera

Similarly, women are underrepresented as actors in the film industry. However, there are some female actors who have made a significant impact and achieved great success in their careers.

<!-- ![Top female actors by box office performance](top_female_actors.png) -->

Some of the highest-grossing actresses in recent years include Gal Gadot, who starred in the Wonder Woman franchise, and Emma Stone, who won an Oscar for her role in La La Land.

# On the Screen

The representation of women on screen is also limited, with many female characters being relegated to supporting roles or falling into stereotypical tropes.

<!-- ![Top female characters by box office performance](top_female_characters.png) -->

Some of the most successful female characters in recent years include Wonder Woman, played by Gal Gadot, and Katniss Everdeen, played by Jennifer Lawrence in the Hunger Games series.

# Women of Impact

Despite the challenges facing women in the film industry, there are many women who have made a significant impact and achieved great success in their roles.

<!-- ![Carousel of top women in various roles in media](top_women.png) -->

These women have not only excelled in their careers, but have also challenged stereotypes and paved the way for future generations of women in media.

# That’s a Wrap!

In conclusion, the representation of women in media is limited and often stereotypical. However, there are many talented and successful women in the industry who are making a significant impact. It is important for the industry to continue to strive for greater diversity and representation, in order to create a more accurate and fair portrayal of women in media.
