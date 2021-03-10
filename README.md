# German Credit Analysis
Analysis of creditability of german bank clients.
![ssad](https://user-images.githubusercontent.com/69935274/110396065-9ab1c980-806f-11eb-8f03-d2dcf83468ad.jpg) <br>

# Introduction

Hello! I am Konstanty and in this kernel we will explore German Credit Dataset. <br>
What client's features determines creditability? <br>
How well can we predict if someone is creditable? <br>

Number of Instances:  1000
Number of Columns: 21

Target:
Creditability
1 - Creditable
0 - Non Creditable

Columns:

Account Balance:
1 -  <    0 DM
2 - <  200 DM
3 - salary assignments for at least 1 year
4 - no checking account

Duration of Credit (month): Numerical

Payment Status of Previous Credit:
0 - no credits taken / all credits paid back duly
1 - all credits at this bank paid back duly
2 - existing credits paid back duly till now
3 - delay in paying off in the past
4 - critical account / other credits existing (not at this bank)

Purpose:
0 - car (new)
1 - car (used)
2 - furniture/equipment
3 - radio/television
4 - domestic appliances
5 - repairs
6 - education
7 - (vacation - does not exist?)
8 - retraining
9 - business
10 - others

Credit Amount: Numerical

Value Savings/Stocks:
1 -          ... <  100 DM
2 -   100 <= ... <  500 DM
3 -   500 <= ... < 1000 DM
4 -          .. >= 1000 DM
5 -   unknown/ no savings account

Present employment since
1 - unemployed
2 -       ... < 1 year
3 - 1  <= ... < 4 years  
4 - 4  <= ... < 7 years
5 -       .. >= 7 years


Installment rate in percentage of disposable income: Numerical

Personal status and sex
1 - male   , divorced/separated
2 - female , divorced/separated/married
3 - male   , single
4 - male   , married/widowed
5 - female , single


Other debtors / guarantors
1 : none
2 : co-applicant
3 : guarantor
          
         
Present residence since: Numerical

Property
1 : real estate
2 : building society savings agreement/life insurance
3 : car or other, not in attribute 6
4 : unknown / no property
          
Age in years: numerical

Other installment plans 
1 : bank
2 : stores
3 : none


Housing
1 : rent
2 : own
3 : for free
          
Number of existing credits at this bank: Numerical

Job
1 : unemployed/ unskilled  - non-resident
2 : unskilled - resident
3 : skilled employee / official
4 : management/ self-employed/  highly qualified employee/ officer
             
Number of people being liable to provide maintenance for: numerical

Telephone
1 : none
2 : yes, registered under the customers name
          
foreign worker
1 : yes
2 : no


# Analysis
Creditability
70% of clients have creditability
30% don't

![pobrane](https://user-images.githubusercontent.com/69935274/110395133-eb282780-806d-11eb-8c73-c5fe5b7c3a75.png)

# Purpose 
![books_read](https://user-images.githubusercontent.com/69935274/110550652-63f1b700-8134-11eb-87b5-aa667f15af2a.png)

# Average Credit Amount
![avg_credit](https://user-images.githubusercontent.com/69935274/110663960-47eb2580-81c7-11eb-9d64-7261ae71af2b.png)

# Average Creditability 
![avg_creditability](https://user-images.githubusercontent.com/69935274/110664154-76690080-81c7-11eb-9069-22386eaf7002.png)

# Average Profit
![Avg_Profit](https://user-images.githubusercontent.com/69935274/110664338-9ac4dd00-81c7-11eb-9047-f5b776e20365.png)

# Credit Count
![books_read](https://user-images.githubusercontent.com/69935274/110664466-b4662480-81c7-11eb-99fc-41795fcb5f18.png)


# Age and Credit Amount

We can see that creditability is lower when amount of credit is higher. <br>
Most of credit amount are up to 5000. <br>
Younger clients tend to apply for bigger credits than older. <br>

![pobrane (1)](https://user-images.githubusercontent.com/69935274/110395313-36423a80-806e-11eb-8d91-9f312198e5dd.png)

To show trend more cleary I've perform anomaly detection(on Age and Credit amount) with GaussianMixture.
![pobrane (2)](https://user-images.githubusercontent.com/69935274/110395458-73a6c800-806e-11eb-8479-9cedaaa9934e.png)

Also I've perform anomaly detection with all features.
In the bigger picture those clients that we classified ealier as an anomaly, are regular clients.

![pobrane (3)](https://user-images.githubusercontent.com/69935274/110396205-e2d0ec00-806f-11eb-8354-d404edaf79a9.png)

Can correlation matrix tell us more about the data?

6 first features(instead of purpose) are strongly correlated. <br>
Account Balance, duly payment status of previous credit and Saving /Stock are positively correlated with Creditability. <br>
Credit amount and duration of the credit are negatively correlated. <br>
![pobrane (4)](https://user-images.githubusercontent.com/69935274/110396317-20ce1000-8070-11eb-9c2e-1bfe643fba42.png)


# Client Classifier<br>
To build Classifier I've written two files.<br>

CreditAnalysis.py - data preprocessing, anomalies detection, train/test split <br>

MultiClassifierModule.py - contain class MultiClassifier. We do classification with 3 algorithm(ExtraTreesClassifier, RandomForestClassifier, VotingClassifier)<br>
For hyperparameters we are using GridSearchCV. To improve accuracy we do n repetition of training and choose the best model.

Accuracy ≈ 80% 

# Conclusion
The biggest surprise for me was that younger tend to take big credits that they can't pay back. It looks like older are more aware of the risk that they are taking and know the value of the money.







