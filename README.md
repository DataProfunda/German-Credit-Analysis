# German Credit Analysis
Creditability Analysis of german bank clients.

# Conclusion

The biggest surprise for me was that younger clients tend to take bigger credits. Main credit purpose for them is education.
Even though their creditability is low, "An investment in education always pays the highest returns". 
In a longer period of time their creditability will increase.
It looks like older are more aware of the risk that they are taking and know the value of the money.

![ddelo](https://user-images.githubusercontent.com/69935274/110676424-3c522b80-81d4-11eb-807c-d88f3c22a4a0.jpg) <br>

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

Majority of the clients take credits for 'radio / television' and 'new car'. <br>
Least of the credit request are for 'retraining' and 'domestic appliances'.  <br>

# Average Credit Amount
![avg_credit](https://user-images.githubusercontent.com/69935274/110663960-47eb2580-81c7-11eb-9d64-7261ae71af2b.png)

Biggest average credit amount concerns purposes such as 'others' and 'used car'. <br>
Smallest average credit amount relate to 'retraining' and 'domestic appliances'.  <br>

Nevertheless average credit amount for 'used car' is bigger than for 'new car'. <br> 
In my opinion, this is a mistake in the source file, because all of available datasets contains same information about 'credit amount' and 'purposes'.

<br>

# Average Creditability 
![avg_Creditability](https://user-images.githubusercontent.com/69935274/110665722-e9bf4200-81c8-11eb-9ea5-a9deae8f3893.png)

Clients that applied for 'used car' and 'retraining' are marked by high creditability. <br>
Clients that applied for 'education' and 'others' are marked by low creditability.  <br>

Credits for education are usually taken by students. <br>
That would explain low creditability. <br>

# Average Profit
![Avg_Profit](https://user-images.githubusercontent.com/69935274/110664338-9ac4dd00-81c7-11eb-9047-f5b776e20365.png)  <br>

Credits for 'used car' and other purposes are the most profitable credits. <br>
Credits forretraining and domestic appliances are the least profitable credits. <br>

# Risk vs Client's Age and Credit Amount

We can see that creditability is lower when amount of credit is higher. <br>
Most of credit amount are up to 5000. <br>
Younger clients tend to apply for bigger credits than older. <br>
Blue dot - creditable  <br>
Red dot - discreaditable  <br>

![pobrane (1)](https://user-images.githubusercontent.com/69935274/110395313-36423a80-806e-11eb-8d91-9f312198e5dd.png)

To show trend more cleary I've perform anomaly detection(on Age and Credit amount) with GaussianMixture.
![pobrane (2)](https://user-images.githubusercontent.com/69935274/110395458-73a6c800-806e-11eb-8479-9cedaaa9934e.png)

Also I've perform anomaly detection with all features.
In the bigger picture those clients that we classified ealier as an anomaly, are just regular clients.

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

The biggest surprise for me was that younger clients tend to take bigger credits. Main credit purpose for them is education.
Even though their creditability is low, "An investment in education always pays the highest returns". 
In a longer period of time their creditability will increase.
It looks like older are more aware of the risk that they are taking and know the value of the money.







