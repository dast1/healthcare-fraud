<div tabindex="-1" id="notebook" class="border-box-sizing">

<div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

# Detecting Healthcare Fraud Using Machine Learning[¶](#Detecting-Healthcare-Fraud-Using-Machine-Learning)

## 1\. Background and Motivation[¶](#1.-Background-and-Motivation)

The Institute of Medicine estimated that 30 percent of U.S. health spending (public and private) in 2009 — roughly `$750 billion — was wasted` on unnecessary services, excessive administrative costs, `fraud`, and other problems. And according to the 2016 Ernst and Young audit report of the US Department of Health and Human Services, HHS did not achieve an `improper payment rate` of less than `10 percent` for the Medicare Fee-for-Service and Medicaid programs.  

The primary motivation of this project is to explore the viability of using `Machine Learning and Artificial Intelegence to detect potential fraud` using publicly available data sources.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

## 2\. Methodology and Technology Stack[¶](#2.-Methodology-and-Technology-Stack)

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

### Data Sources[¶](#Data-Sources)

* * *

![](images/data_sources.png)  
The are plenty of data sources that can be incorporated into the Machine Learning model but given the time constraints, I imposed to initially limit the scope to:

> *   Drug Prescription Data from Medicare as **predictors**, and
> *   List of Excluded Individuals and Entities as my **targets**.

The exploratory data analysis into these data sets can be found [here](notebooks/EDA.ipynb).

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

### Technology Stack[¶](#Technology-Stack)

* * *

![](images/tech_stack.png)  
I used the standard Python based Data Science tech stack. Also, given that I had large data set, I used a very powerful EC2/Sagemaker instances on the AWS.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

### Preserving the Signal[¶](#Preserving-the-Signal)

* * *

![](images/number_of_records.png)  
Generally, imbalanced classes is common in fraud detection. In other words, we'd expect to see far fewer fraudulent transactions relative to the non-fraudulent ones. In my case, the ratio is roughly 1-to-1000\.  

A common strategy to balance out the labels is to either undersample the majority class or oversample the minority target class. I chose the latter and I used Random Bootstrap Sampling and SMOTE. The implementation of the code can be found [here](src/over_sample.py).  

Since a large number of excluded healthcare providers didn't have a National Provider Identifier, I tried matching the pairs up by their name and specialty using fuzzy-wuzzy. Over 25 million pairs were compared but the results didn't yield in a significant contribution to address the `imbalanced classes` issue, so I didn't incorporate any of the resulting records into my model. You may still find the notebook with the implementation of fuzzy-wuzzy string matching [here](notebook/fuzzy-wuzzy.py).  

And finally, to maximize the presence of the target signal, i.e. the ratio of excluded providers relative to the total number of providers, I considered to limit the scope of the model only to the States with the highest exclusion ratios. The implementation of this strategy can be found in [this](notebook/exclusion_ratio.py) notebook.

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

## 3\. Model Results[¶](#3.-Model-Results)

* * *

![](images/model_results.png)  
Since my model had a significant class imbalance, to assess model perforamance I used Area Under the Curve (AUC). This is a common measure to evaluate the trade-off between correctly identifying the true signal relative to incorrectly identifying false signals as we increase the acceptance threshold.  

I initially ran the model through the `Random Forest` and the performance was:

> AUC score: 0.72  
> Cross Validation score (mean): 0.61

Next, I ran the model through other ensemble algorithms but the `Gradient Boosted Trees` came in first with:

> AUC score: 0.78  
> Cross Validation score (mean): 0.63

Also, the model picked up on these 2 features as most predective:

> 30-day fill count  
> total day supply

And finally, the implementation of the model can be found [here](notebook/model.py).

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

## 4\. Next Steps[¶](#4.-Next-Steps)

* * *

![](images/next_steps.png)  
I found this project very interesting and I know the results can further be improved upon by incorporating other data sets.

</div>

</div>

</div>

</div>

</div>
