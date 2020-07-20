# Search Engine Report
## Overview
Overview of how your code works

This search engine returns the importance/authentic scores for certain documents which contains the query words. We implement this process by the following three classes: 
- TFIDF.py is a class which creates a search engine from a clean corpus based on the tf-idf scores.
- PageRank.py is a class which creates a search engine based on a link dictionary.
- processing.py is a class which process xml file to clean corpus.

## Known Bugs
Description and example inputs and outputs for any known bugs.
- currently no bugs (for a while)

## Report Questions &  Answers
### Q1  
<!-- Respond to your boss’s suggestions to “store word frequencies the way you compute”.  
(See original question above for more detail.) 
--> 
- The boss's method would have a larger time complexity as we need to loop through the entire documents for each query words, also the method makes it harder for us the get all the documents contains certain query word.  

### Q2
<!--Explain the following equation in terms of probability notation if PR(X) is the probability of arriving at node X, 
and L(X) is the number of outbound links from X. (i.e., What does d  represent, what does (1 - d)/N represent and, 
what does the sum represents.)-->  
- d is the probability that an average surfer will continue at any step.
- (1 - d)/N the probability that an average surfer will stop at certain step.
- the sum is the pagerank score which is contributed by the pages with incoming links, which means we might click a link with higher rank more often than a link with lower rank. 

<!-- If 32% of traffic to a webpage comes from non-inlink sources what should the value of d be? -->
- 68%

### Q3 
<!-- Explain how extract_links operates and what it returns. 
In addition, What would be different if we don’t return the second return value (words extract from display texts)?-->
- For the links in all_links, we strip [] to get the links; If the number of "|" is greater than 1, we ignore the link; if the number of "|" equals 1, we process the link into two parts: link_text and link_pages, and add them to their main list/set; otherwise we add the link to link_text and link_pages.
- If we don't return the extra 


### Q4 
<!-- Explain why process_text is also applied to query strings.-->
- Because query strings normally would contain punctuations, stop words, and they also need to be stemmed. Thus we apply process_text to query strings. 


### Q5
<!--Web spiders continuously find new web pages and revisit old web pages.  When a new page is added or an old page is 
revisited an incremental update to the TF-IDF and PageRank must be made.  Explain how you might implement be able to 
implement an incremental SearchEngine update() method. --> 
- we can update the corpus and the tf-idf score accordingly. In the pageRank.py, we can update the xml files which contains all the links as well as the reverse_index so that we can update pagerank score accordingly. 

## Smart Search
<!--Description of how you implemented the 'smart' search mode. Include at least two examples that show that it makes sense, and explains why it can potentially be better than just PageRank or TF-IDF.
 -->
- Smart search is a search engine which takes both tf-idf score and pagerank score into account. The documents returned by certain query word should have a high tf-idf score as well as a high authenticity. Thus, it makes sense to add there two scores as the condition of smart research. The result returned is a combination of the two scores as it takes both scores into account. Thus, smart search is better than just PageRank or TF-IDF. 


![](image/1.png)
![](image/2.png)
![](image/3.png)


## Testing
<!-- 
Description of how you tested your code, include details on what you did beyond running the basic tests included with the stencil.
-->

- In TFIDF.py, I used unit testing to check whether calc_term_frequence and calc_tf_idf return the correct value for certain input corpus. Also I checked whether the search function works correctly by checking the tf-idf score of certain words in the giving corpus. 
- In PageRank.py, I used unit testing to check whether the calc_page_rank returns the correct pagerank score. I also checked whether teh search function works correctly and return the page rank scores correctly for certain query words. 
- In processing.py, I used intergration testing to check whether process_text and build_corpus work correctly and pass all the assertion tests. I did not test extract_links as it is provided by the instructor. 
 
 
 


![](image/4.png)

```python

```

```python

```
