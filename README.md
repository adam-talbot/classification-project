# Telco Churn Classification Project

<img src="https://23x6xj3o92m9361dbu2ij362-wpengine.netdna-ssl.com/wp-content/uploads/2019/02/thumbnail-3ac78ae8dc4ab8e78d3937d8a6b35326-1200x370.jpeg" alt="Iris" title="Iris Dataset" width="500" height="200" />

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Project Summary

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

#### Project Objectives
> - Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report
> - Create modules (acquire.py, prepare.py) that make your process repeateable
> - Construct a model to predict customer churn using classification techniques
> - Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience
> - Answer panel questions about your code, process, findings and key takeaways, and model

#### Business Goals
> - Find drivers for customer churn at Telco
> - Construct a ML classification model that accurately predicts customer churn
> - Document your process well enough to be presented or read like a report

#### Audience
> - The Codeup Data Science team

#### Project Deliverables
> - A Jupyter Notebook Report showing process and analysis with the goal of finding drivers for customer churn 
> - A README.md file containing the project description with goals, initial hypotheses, a data dictionary, project planning, instructions or an explanation of how someone else can recreate your project and findings, answers to your hypotheses, key findings, recommendations, and takeaways from your project
> - A CSV file with customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn). These predictions are from the best performing model ran on X_test. 
> - Individual modules, .py files, that hold your functions to acquire and prepare your data
> - A notebook walkthrough presentation with a high-level overview of your project (5 minutes max)

#### Project Context
> - The Telco dataset I'm using came from the Codeup database.


#### Data Dictionary

---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
|payment\_type\_id |How a customer pays their bill each month | int64 |
|contract\_type\_id|Which contract type a customer has | int64 |
|internet\_service\_type_id|Type of internet service a customer has | int64 |
|customer\_id|Alpha-numeric ID that identifies each customer| object |
gender|Gender of the customer| object |
senior_citizen|If customer is 65 or older| int64 |
partner|If customer is married| object | 
dependents|If a customer lives with dependents| object |
tenure|The length of a customers relationship with Telco™ measured in months|  int64 |
phone_service|If a customer has phone service| object |
multiple_lines|If a customer has multiple phone lines| object |
online_security|If a customer has online security add-on| object |
online_backup|If a customer has online backups add-on| object |
device_protection|If a customer has a protection plan for Telco™ devices| object |
tech_support|Whether a customer has technical support add-on| object |
streaming_tv|If a customer uses internet to stream tv| object |
streaming_movies|If a customer uses internet to stream movies| object |
paperless_billing|If a customer is enrolled in paperless billing| object |
monthly_charges|The amount a customer pays each month| object |
total_charges|The total amount a customer has paid for Telco™ services| object |
|internet\_service\_type|Type of internet service a customer has| object |
|contract_type|The type of contract a customer has| object |
|payment_type|How a customer pays their bill| object |

| Target | Definition | Data Type |
| ----- | ----- | ----- |
|churn|Indicates whether a customer has terminated service| object |

#### Initial, Informal Hypotheses
> - Customers are more likely to churn within first 12 months of tenure
> - Customers that pay via manual payment methods are more likely to churn
> - Month-to-month customers will have highest churn rate
> - Fiber customers are more likely to churn that other those with other internet types
> - Customers with more than one phone line will be more likely to churn 

#### Formal Hypotheses

>  **Hypothesis 1 -**
> - alpha = .05
> - $H_0$: Sepal length is the same in virginica and versicolor. $\mu_{virginica} == \mu_{versicolor}$.  
> - $H_a$: Sepal length significantly different in virginica and versicolor. $\mu_{virginica} != \mu_{versicolor}$. 
> - Outcome: I rejected the Null Hypothesis; there is a difference in sepal length between the Virginica and Vericolor Species.

>  **Hypothesis 2 -** 
> - alpha = .05
> - $H_0$: Sepal width is the same in virginica and versicolor. $\mu_{virginica} == \mu_{versicolor}$.  
> - $H_a$: Sepal width significantly different in virginica and versicolor. $\mu_{virginica} != \mu_{versicolor}$. 
> - Outcome: I rejected the Null Hypothesis; there is a difference in sepal width between the Virginica and Versicolor Species.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary - Conclusions & Next Steps

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> - I found that all of the classification models I created, LogisticRegression, DecisionTree, RandomForest, and KNeighbors predicted the species of Iris equally well using the features `sepal_width`, `sepal_length`, `petal_length`, `petal_width`.
> - I chose my DecisionTree model as my best model with a 90% accuracy rate for predicting my target value, species. This model outperformed my baseline score of 33% accuracy, so it has value.
> - Some initial exploration and statistical testing revealed that engineering some new features like petal area or sepal area might help my models predict with even more accuracy, and with more time, I would like to test this hypothesis.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

##### Plan
- [x] Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- [x] Acquire data from the Codeup Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
- [x] Clearly define two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [x] Establish a baseline accuracy and document well.
- [x] Train three different classification models.
- [x] Evaluate models on train and validate datasets.
- [x] Choose the model with that performs the best and evaluate that single model on the test dataset.
- [x] Create csv file with the measurement id, the probability of the target values, and the model's prediction for each observation in my test dataset.
- [x] Document conclusions, takeaways, and next steps in the Final Report Notebook.

___

##### Plan -> Acquire
> - Store functions that are needed to acquire data from the measures and species tables from the iris database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
> - The final function will return a pandas DataFrame.
> - Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
> - Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, ...).
> - Plot distributions of individual variables.
___

##### Plan -> Acquire -> Prepare
> - Store functions needed to prepare the iris data; make sure the module contains the necessary imports to run the code. The final function should do the following:
> - Split the data into train/validate/test.
> - Handle any missing values.
> - Handle erroneous data and/or outliers that need addressing.
> - Encode variables as needed.
> - Create any new features, if made for this project.
> - Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.
___

##### Plan -> Acquire -> Prepare -> Explore
> - Answer key questions, my hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, churn. 
> - Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
> - Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). The goal is to identify features that are related to species (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
> - Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model
> - Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
> - Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
> - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
> - Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
> - Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
> - Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver
> - Introduce myself and my project goals at the very beginning of my notebook walkthrough.
> - Summarize my findings at the beginning like I would for an Executive Summary. (Don't throw everything out that I learned from Storytelling) .
> - Walk Codeup Data Science Team through the analysis I did to answer my questions and that lead to my findings. (Visualize relationships and Document takeaways.) 
> - Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.
> - Finish with key takeaways, recommendations, and next steps and be prepared to answer questions from the data science team about your project.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_report.ipynb notebook