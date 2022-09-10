## Student Adaptability in Online Learning

![Head Banner](./img/readme_frontbanner.png)

The task is to build a model to predict the outcome of students adaptability level in online education using machine learning approaches.

### Language Used : Python --version: 3.8.11

## Repo Contents

1. data : folder containing all datasets.
2. img: folder containing all images used.
3. pipeline: folder containing pipelines and target encoder saved to disk.
4. app.py
5. Data Prep and model.ipynb : Data prep and model development.
6. streamlit.py: streamlit python script.
7. functions.py: python script containing all functions used in project.
8. requirements.txt

## Data Source
Kaggle - https://bit.ly/3BsNUbA

## Approach

1. Exploring All Dataset
Here we load the data.csv file as a pandas dataframe to get familiar with the dataframe, and to get a quick look into the dataframe.

2. Data Cleaning
Here we clean up the data, trying to look out for any missing values or Nan in the columns. I did a brief cleaning of the data, replcaing all Nan's in the dataframe columns and drop all ages 1-5 from the data


3. Pipelines
The pipeline contains:
<ol>
<li> Ordinal Encoding</li>
<li> Gradient Boosted Trees </li>
</ol>

For the pipeline, I encoded the 'Gender','Institution Type','IT Student','Financial Condition','Internet Type','Age','Education Level','Network Type','Class Duration','Device' columns using the Ordinal Encoder.


## To Run

1. Read the READ.md file
2. `pip install -r requirements.txt`
3. run the jupyter Notebook (Data Prep and model)
4. To test streamlit file locally run `streamlit run streamlit.py` in terminal
