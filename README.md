# Telco Churn Classification Project

<img src="https://23x6xj3o92m9361dbu2ij362-wpengine.netdna-ssl.com/wp-content/uploads/2019/02/thumbnail-3ac78ae8dc4ab8e78d3937d8a6b35326-1200x370.jpeg" alt="Iris" title="Iris Dataset" width="500" height="200" />

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Project Summary

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

#### Project Objectives
> - Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report
> - Create modules (acquire.py, prepare.py) that make my process repeateable
> - Construct a model to predict customer churn using classification techniques
> - Deliver a 5-minute, audience-appropriate presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above
> - Answer panel questions about your code, process, findings and key takeaways, and model

#### Business Goals
> - Find drivers for customer churn at Telco
> - Construct a ML classification model that accurately predicts customer churn
> - Document process well enough to be presented or read like a report

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
| Attribute | Definition | Data Type | Notes |
| ----- | ----- | ----- | ----- |
|payment\_type\_id |How a customer pays their bill each month | int64 | Dropped for modeling |
|contract\_type\_id|Which contract type a customer has | int64 | Dropped for modeling |
|internet\_service\_type_id|Type of internet service a customer has | int64 | Dropped for modeling |
|customer\_id|Alpha-numeric ID that identifies each customer| object | Dropped for modeling |
gender|Gender of the customer| object | Dropped for modeling, statistical testing showed independence from target |
senior_citizen|If customer is 65 or older| int64 | Used in model |
partner|If customer is married| object | Used in model |
dependents|If a customer lives with dependents| object | Used in model |
tenure|The length of a customers relationship with Telco™ measured in months|  int64 | Used in model |
phone_service|If a customer has phone service| object | Dropped for modeling, statistical testing showed independence from target |
multiple_lines|If a customer has multiple phone lines| object | Used in model, one category removed to reduce redundancy |
online_security|If a customer has online security add-on| object | Used in model, one category removed to reduce redundancy |
online_backup|If a customer has online backups add-on| object | Used in model, one category removed to reduce redundancy |
device_protection|If a customer has a protection plan for Telco™ devices| object | Used in model, one category removed to reduce redundancy |
tech_support|Whether a customer has technical support add-on| object | Used in model, one category removed to reduce redundancy |
streaming_tv|If a customer uses internet to stream tv| object | Used in model, one category removed to reduce redundancy |
streaming_movies|If a customer uses internet to stream movies| object | Used in model, one category removed to reduce redundancy |
paperless_billing|If a customer is enrolled in paperless billing| object | Used in model |
monthly_charges|The amount a customer pays each month| object | Used in model |
total_charges|The total amount a customer has paid for Telco™ services| object | Used in model, data type changed to float |
|internet\_service\_type|Type of internet service a customer has| object | Used in model |
|contract_type|The type of contract a customer has| object | Used in model |
|payment_type|How a customer pays their bill| object | Used in model |

| Target | Definition | Data Type | Notes |
| ----- | ----- | ----- | ----- |
|churn|Indicates whether a customer has terminated service| object | For exploration and modeling, 1=churn and 0=not_churn |

#### Initial, Informal Hypotheses
> - Some categorical variables will be related to the target (I can test this with the Chi-Square Test)
>> - Those that are related should be used in model, those that aren't, shouldn't be used
> - Some quantitative variables will be related to the target (I can test this with the Mann-Whitney Test)
>> - Those that are related should be used in model, those that aren't, shouldn't be used

#### Formal Hypotheses

>  **Hypotheses (Categorical Variables):**
> - alpha = .05

> Null Hypotheses:
> 1. H_0: `Churn` is independent of `gender`
> 2. H_0: `Churn` is independent of `senior_citizen`
> 3. H_0: `Churn` is independent of `partner`
> 4. H_0: `Churn` is independent of `dependents`
> 5. H_0: `Churn` is independent of `phone_service`
> 6. H_0: `Churn` is independent of `multiple_lines`
> 7. H_0: `Churn` is independent of `online_security`
> 8. H_0: `Churn` is independent of `online_backup`
> 9. H_0: `Churn` is independent of `device_protection`
> 10. H_0: `Churn` is independent of `tech_support`
> 11. H_0: `Churn` is independent of `streaming_tv`
> 12. H_0: `Churn` is independent of `streaming_movies`
> 13. H_0: `Churn` is independent of `paperless_billing`
> 14. H_0: `Churn` is independent of `internet_service_type`
> 15. H_0: `Churn` is independent of `contract_type`
> 16. H_0: `Churn` is independent of `payment_type`

> Alternative Hypotheses:
> 1. H_0: `Churn` is not independent of `gender`
> 2. H_0: `Churn` is not independent of `senior_citizen`
> 3. H_0: `Churn` is not independent of `partner`
> 4. H_0: `Churn` is not independent of `dependents`
> 5. H_0: `Churn` is not independent of `phone_service`
> 6. H_0: `Churn` is not independent of `multiple_lines`
> 7. H_0: `Churn` is not independent of `online_security`
> 8. H_0: `Churn` is not independent of `online_backup`
> 9. H_0: `Churn` is not independent of `device_protection`
> 10. H_0: `Churn` is not independent of `tech_support`
> 11. H_0: `Churn` is not independent of `streaming_tv`
> 12. H_0: `Churn` is not independent of `streaming_movies`
> 13. H_0: `Churn` is not independent of `paperless_billing`
> 14. H_0: `Churn` is not independent of `internet_service_type`
> 15. H_0: `Churn` is not independent of `contract_type`
> 16. H_0: `Churn` is not independent of `payment_type`

> **Conclusions:**
> 1. We **fail to reject the null**, evidence suggests that `gender` is independent of `churn`
> 2. We **reject the null**, evidence suggests that `senior_citizen` is not independent of `churn`
> 3. We **reject the null**, evidence suggests that `partner` is not independent of `churn`
> 4. We **reject the null**, evidence suggests that `dependents` is not independent of `churn`
> 5. We **fail to reject the null**, evidence suggests that `phone_service` is independent of `churn`
> 6. We **reject the null**, evidence suggests that `multiple_lines` is not independent of `churn`
> 7. We **reject the null**, evidence suggests that `online_security` is not independent of `churn`
> 8. We **reject the null**, evidence suggests that `online_backup` is not independent of `churn`
> 9. We **reject the null**, evidence suggests that `device_protection` is not independent of `churn`
> 10. We **reject the null**, evidence suggests that `tech_support` is not independent of `churn`
> 11. We **reject the null**, evidence suggests that `streaming_tv` is not independent of `churn`
> 12. We **reject the null**, evidence suggests that `streaming_movies` is not independent of `churn`
> 13. We **reject the null**, evidence suggests that `paperless_billing` is not independent of `churn`
> 14. We **reject the null**, evidence suggests that `internet_service_type` is not independent of `churn`
> 15. We **reject the null**, evidence suggests that `contract_type` is not independent of `churn`
> 16. We **reject the null**, evidence suggests that `payment_type` is not independent of `churn`


>  **Hypotheses (Quantitative Variables):** 
> - alpha = .05

> Null Hypotheses:
> 1. H_0: Mean `tenure values` are equal for `churn` subgroups
> 2. H_0: Mean `monthly_charges` values are equal for `churn` subgroups
> 3. H_0: Mean `total_charges` values are equal for `churn` subgroups

> Alternative Hypotheses:
> 1. H_a: Mean `tenure values` are not equal for `churn` subgroups
> 2. H_a: Mean `monthly_charges` values are not equal for `churn` subgroups
> 3. H_a: Mean `total_charges` values are not equal for `churn` subgroups

> **Conclusions:**
> 1. We **reject the null**, evidence suggests that mean `tenure` values are different for `churn` subgroups
> 2. We **reject the null**, evidence suggests that mean `monthly_charges` values are different for `churn` subgroups
> 3. We **reject the null**, evidence suggests that mean `total_charges` values are different for `churn` subgroups

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary - Conclusions & Next Steps

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> **Conclusions:**
> - I found that my KNN Classification model best predicted churn when evaluated using accuracy and defining overfit as a >5% decrease in accuracy from train to validate evaluation
> - This model outperformed the baseline by 4.4%, so it has value.

> **Next Steps:**
> - Some initial exploration and statistical testing revealed that engineering some new features might help my models predict with even more accuracy, and with more time, I would like to test this hypothesis.
> - Scaling numeric columns would likely improve performance for the KNN model. I would implement this with more time.
> - Because of the imbalance of classes for the target variable, sampling methods might also improve model peformance. I would implement this with more time. 

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

##### ***Plan***
- [x] Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- [x] Acquire data from the Codeup Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
- [x] Clearly define at least two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [x] Establish a baseline accuracy and document well.
- [x] Train three different classification models.
- [x] Evaluate models on train and validate datasets.
- [x] Choose the model with that performs the best and evaluate that single model on the test dataset.
- [x] Create csv file with the measurement id, the probability of the target values, and the model's prediction for each observation in my test dataset.
- [x] Document conclusions, takeaways, and next steps in the Final Report Notebook.

___

##### Plan -> ***Acquire***
> - Store functions that are needed to acquire Telco data from the database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
> - The final function will return a pandas DataFrame.
> - Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
> - Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, ...).
___

##### Plan -> Acquire -> ***Prepare***
> - Store functions needed to prepare the Telco data; make sure the module contains the necessary imports to run the code. The final function should do the following:
>> - Split the data into train/validate/test.
>> - Handle any missing values.
>> - Handle erroneous data and/or outliers that need addressing.
>> - Encode variables as needed.
> - Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.
> - Plot distributions of individual variables.
___

##### Plan -> Acquire -> Prepare -> ***Explore***
> - Answer key questions, my hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, churn. 
> - Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
> - Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). The goal is to identify features that are related to species (the target), identify any data integrity issues, and understand 'how the data works'. If there appears to be some sort of interaction or correlation, assume there is no causal relationship and brainstorm (and document) ideas on reasons there could be correlation.
> - Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
___

##### Plan -> Acquire -> Prepare -> Explore -> ***Model***
> - Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
> - Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
> - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
> - Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
> - Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
> - Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model -> ***Deliver***
> - Introduce myself and my project goals at the very beginning of my notebook walkthrough.
> - Summarize my findings at the beginning like I would for an Executive Summary.
> - Walk Codeup Data Science Team through the analysis I did to answer my questions and that lead to my findings. (Visualize relationships and Document takeaways.) 
> - Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.
> - Finish with key takeaways, recommendations, and next steps and be prepared to answer questions from the data science team about your project.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [ ] Download the aquire.py, prepare.py, explore.py, and final_report.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_report.ipynb notebook