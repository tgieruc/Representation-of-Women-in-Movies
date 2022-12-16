---
title: The Representation of Women in Movies
subtitle: From Behind the Camera to on the Screen
---

# Introduction

Society has made massive progress regarding women’s rights within the last century, but can we see that change in the movies that we watch? Laws and general societal outlook has changed, but the way women are viewed by everyday people around them may not have changed as much. Movies provide us a unique insight into the subconscious ways that society is conditioned to view women and capture the ideals and norms of the time they were produced. From actresses on screen to the story itself, within film there potentially lies some hidden truth about how far we have come to addressing gender inequality. Through the exploratory analysis of directors and writers, movie characters, and actors centered around the CMU Movie Summary Corpus dataset, the group aims to get a better understanding of how women are and have been represented in media.



# The Data

Our analysis is based on merging the [CMU Dataset](https://www.cs.cmu.edu/~ark/personas/), the [Stanford CoreNLP-processed summaries](http://www.cs.cmu.edu/~ark/personas/data/corenlp_plot_summaries.tar), [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page), [IMDB](https://www.imdb.com/interfaces/) and [Box office Mojo](https://www.boxofficemojo.com/).

We have separated the data in three tables: 

* The movies, that contains 

{% include movie_percentage.html %}


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

<!-- Load the D3 library -->
<script src="https://d3js.org/d3.v5.min.js"></script>

<!-- Create a container element for the chart -->
<div id="chart"></div>

<!-- Create the chart using D3 -->
<script>
// Set the dimensions of the chart
var width = 600;
var height = 400;

// Set the margins
var margin = {
  top: 20,
  right: 20,
  bottom: 30,
  left: 50
};

// Set the data
var data = [
  { role: "Actors", percent: 28 },
  { role: "Directors", percent: 8 },
  { role: "Screenwriters", percent: 11 }
];

// Set the ranges
var x = d3.scaleBand().range([0, width]).padding(0.1);
var y = d3.scaleLinear().range([height, 0]);

// Create the SVG element
var svg = d3.select("#chart")
  .append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// Scale the range of the data
x.domain(data.map(function(d) { return d.role; }));
y.domain([0, d3.max(data, function(d) { return d.percent; })]);

// Add the x-axis
svg.append("g")
  .attr("transform", "translate(0," + height + ")")
  .call(d3.axisBottom(x));

// Add the y-axis
svg.append("g")
  .call(d3.axisLeft(y));

// Add the bars
svg.selectAll(".bar")
  .data(data)
  .enter()
  .append("rect")
  .attr("class", "bar")
  .attr("x", function(d) { return x(d.role); })
  .attr("width", x.bandwidth())
  .attr("y", function(d) { return y(d.percent); })
  .attr("height", function(d) { return height - y(d.percent); });
</script>
