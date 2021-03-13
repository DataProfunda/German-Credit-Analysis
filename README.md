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







