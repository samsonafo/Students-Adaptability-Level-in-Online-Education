## Student Adaptability in Online Learning

![Head Banner](./img/readme_frontbanner.png)


The Task is a Regression Problem. We intend to build a regression model on the training data, maximising performance on the test data.
The target variable is 'amount_n26_currency'.

### Language Used : Python --version: 3.8.11

## Repo Contents

1. descriptives.ipynb : Descriptive Analysis of train data.
2. model_development.ipynb: Pipeline building.
3. data : folder containing all datasets.
4. img: folder containing all images used.
5. pipeline: folder containing pipelines saved to disk.
6. pipeline.py: python script to run new predictions.
7. functions.py: python script containing all functions used in project.

## Approach

1. Exploring All Dataset
Here we load the csv files('training.csv','mcc_group_definition.csv','transaction_types.csv') as a pandas dataframe to get familiar with the dataframe, and to get a quick look into the dataframe.

2. Data Cleaning
Here we clean up the data, trying to look out for any missing values or Nan in the columns. I did a brief cleaning of the data, replcaing all Nan's in mcc_group (dataframe from mcc_group_definition.csv) with a new category '18' encoded as 'Unknown' as explanation.

3. Visualizations
Here we make visualizations (Pie chart and bar graphs) showing:
a. A Comparison of Total Income and Total Expense by users.
b. A Comparison of Mean Income and Mean Expense by users.
c. Pie chart showing the distribution of the Transaction Directions
d. chart showing the distribution of the transaction types
e. Distribution of Credit/Debit Explanations
f. Agents for transactions between Feburary to July

** Incase there any challenges with viewing the plotly charts, pls use jupyter notebook in place of Jupyter Lab.

4. Pipelines
Here I built 2 Pipelines.
<ol>
<li> Baseline Pipeline using Linear Regression </li>
<li> Pipeline using Gradient Boosted Trees </li>
</ol>

For each pipeline, I encoded the 'transaction_type','explanation','explanation_mcc_group' columns using the BaseNEncoder, while the 'agent','direction' columns were encoded using the OneHot-encoder.

## Analysis Questions
1. At the moment, the accuracy of the model needs to be improved and then the prediction results may be trusted and useful for our initial plan.
2. I used the r2_score(coefficient of determination) to measure the performance on the model. Best score is 1 and worst score is 0.

## Other Observations
1. From the visualizations, I noticed that the mean and total expenses was more mean and total income. 
2. Except for March and April, total monthly income exceeds total expense.



## TO Do

If I had more time I could have

1. Model Improvement
- compare other models like Random Forest, SVM etc.
- grid search or bayesian optimization for best hyper-parameters
- using pre-calculated monthly averages over the categories.
2. More Descriptives and Visualization
- Add more graphs and to see more into the Data at the Data Cleaning Stage.


## To Run

1. Read the READ.md file
2. `pip install -r requirements.txt`
3. run the jupyter Notebook (descriptives, model_development etc.)
4. To make new predictions with holdout (August data) run `python pipeline.py` in terminal
-- insert holdout data address.


## To Integrate results into App
-- Using Flask
1. import Flask and all needed libraries
2. define the app route for the web-app
3. This can be deployed/hosted on virtual machines. (Heroku, AWS etc.)
-- For complex pipelines, to avoid different parts of the pipeline breakdown affecting other parts, docker and kubernetes can be used.



## Possible Problems
** In case of problems installing matplotlib on a new environment, pls see this: https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python

or try `conda install matplotlib` and then run `pip install -r requirements.txt` again.

** Incase there any challenges with viewing the plotly charts, pls use jupyter notebook in place of Jupyter Lab.
