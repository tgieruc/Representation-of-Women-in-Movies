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

The representation of women in media has long been a topic of interest, as it reflects societal norms and attitudes towards gender equality. Despite the progress made in recent decades towards gender equality, it is important to examine whether these changes are reflected in the films we watch. Movies provide a unique insight into the subconscious ways in which society is conditioned to view women, and can capture the ideals and norms of the time in which they were produced. 

In this data analysis project, we will use the CMU Movie Summary Corpus dataset, completed with additional datasets, to explore the portrayal of women in film. We will not only analyze the roles of actresses and characters, but also of writers and directors. By analyzing these factors, we aim to gain a deeper understanding of how women are and have been represented in media, and how this has evolved through time.



# The Data

Our analysis is based on merging the [CMU Movie Summary Corpus dataset](https://www.cs.cmu.edu/~ark/personas/), the [Stanford CoreNLP-processed summaries](http://www.cs.cmu.edu/~ark/personas/data/corenlp_plot_summaries.tar), [IMDb](https://www.imdb.com/interfaces/), [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page), [IMDB](https://www.imdb.com/interfaces/) and [Box office Mojo](https://www.boxofficemojo.com/). We have separated the data into three tables: the movies table, the characters table, and the directors and writers table.

* The movies table contains titles, release year, runtime, box office revenue, average rating and number of votes on IMDb, genre, as well as the list of directors and writers. There are a total of 81,741 different movies.

{% include movie_percentage.html %}

* The characters table contains the ID of the movie, the character name and actor name, their height, ethnicity, birth and death year, the movie metric and the actor metric. There are 450,669 characters played by 135,761 different actors.

{% include characters_percentage.html %}

* The directors and writers table contains titles, role (either director or writer), name, gender, birth year, and height. There are a total of 86,474 directors and 164,271 writers.

{% include directors_percentage.html %}



## The Impact Score metric
### Movies
We have created a metric in order to measure the impact of a movie on the average rating and the number of votes. Our assumption is that an impactful movie has a lot of votes and has either an extremely good or bad average rating.

We apply a logarithmic transformation to the number of votes in order to turn its heavy-tailed distribution into a gaussian distribution, then we normalize the data and accurately compare the impact of different movies. We then take the absolute value of the normalized average rating for each movie. This accounts for both very good and very bad movies, as both have a significant impact on audience reception. By combining these two factors, we are able to calculate the overall impact a movie has on its audience and compare this across different films.

$$\textrm{Impact Score}_\textrm{Movies} = \textrm{normalized} (\log(\textrm{number of votes})) \cdot \textrm{abs}(\textrm{normalized}(\textrm{IMDB rating}))$$

According to this metric, those are the top 10 most impactful movies of our dataset:

{% include top20_movies.html %}


### Actors, writers and directors
For actors, writers, and directors, we use the [Discounted Cumulative Gain](https://en.wikipedia.org/wiki/Discounted_cumulative_gain) to rank the movies they are linked to according to the impact score and compute their overall impact.

$$\textrm{Impact Score}_\textrm{Actors, Directors, Writers} = \sum_{i=1}^{\textrm{number of movies}}\frac{\textrm{movie metric}_i}{\log_2(i + 1)}$$

Here are the top 10 actors, writers and directors with the highest impact score:

{% include impact_score.html %}

We can see that the top 10 actors, writers and directors are all male, which is a leads to the following question: *where are the women?*

# Where are the Women?


As our project focuses on the representation of women in movies, it can be interesting to look at the evolution of the presence of women in movies, as characters and as part of the crew.


{% include actress_crew_percentage.html %}

From the graph above, we can see that women in crews have always been even more underrepresented than actresses.

Let's break the data down by genre, to see if there is any difference in the distribution of women in film across genres.

{% include percentage_per_genre_per_decade.html %}
{% include male_vs_female_presence_in_movie_genre.html %}


From the graphs above, we can see that when it comes to genre, women are most often represented in dramas, comedies and romances, while they are underrepresented in action adventure and sci-fi films.

When considering the representation of women among directors and writers, we found that the pattern is similar, although the overall percentage of women in these roles is significantly lower than for actresses, as shown below.

{% include directors_writers_percentage_per_genre_per_decade.html %}


# Behind the Camera

Put the director analysis here. Who are the most impactful directors for the most common genres? What are their best movies? What are they about? how does the impact of female directors compare with male directors?

# In Front of the Camera

Put the Actor analysis here

# On the Screen

Put the character analysis here

# Women of Impact

Maybe highlight the top women in each role that have made the highest impact? the bag of words for their characters? make this in a carousel? 

# That’s a Wrap!

In conclusion, the representation of women in media is limited and often stereotypical. However, there are many talented and successful women in the industry who are making a significant impact. It is important for the industry to continue to strive for greater diversity and representation, in order to create a more accurate and fair portrayal of women in media.
