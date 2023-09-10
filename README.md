# FinalProject
Wine quality prediction

# Project Inspiration

My past work experiences had been a lot about improving productivity in manufacturing operations. I have realized that using data-driven approaches to identify bottlenecks, streamlining and standardizing processes, could save time and resources and also enhance the overall quality of process delivering better results to customers.
Machine learning it is a great path that could help to go beyond manual efforts and  traditional process optimization and achieve results that were previously unattainable. I believe that through automating decision-making, predictive analytics,  continuously improving processes and best practices we can empower organizations to achieve greater efficiency, reduce costs, and improve their overall performance.

# Project Goal
Optimized the wine quality prediction process using machine supervised learning model.

# Project Features, Techniques and Steps
Variables available in the data set: 
fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol,  and quality2.

Target variable: quality2 (good quality = 1 and bad quality = 0)

1. Data Preparation: data exploration, cleaning, feature engineering . 
During the steps of data preparation two methods were used to identify outliers: the Interquartile range and the Z-score. Z-score was the technique selected to identify and removed outliers.
Also during the data prepartion the duplicates were identified; despite that since duplicates could represent the data of a different wine with the same values and since keeping the duplicates increased the accuracy of the models on in this project, the duplicates were not removed for the final model.


2. Models, Tuning, Evaluation, Deployment 

Machine learning models used: Logistic Regression, Random Forest, Support Vector, Naive Bayes, and XGBoost

Techniques used for tuning parameters: GridSerachCV and RandomizedSearchCV
These two methods are currently commented (#) in the code due the long time that takes to run them 

Evaluation metrics used: 
ROC_AUC  - model’s ability to distinguish between high-quality and low-quality wines
Accuracy   -  calculates the correct predictions made by the model

Model Deployment: tools used were pickle for saving the model and flask to deploy the model

3. Conclusions



# Future steps
1. Despite that Random Forest model performed well, there is room for improvement. It  is recommended, for the current model, collect additional data and explore more the feature selection to further enhance its accuracy.
2. Explore more the parameters in some of the  other 4 models to try to fine a better tune.


# Tech Stack: 
1. Data preparation: Pandas, Numpy and Scipy.stats, sklearn.preprocessing
2. Models and Tuning: Sklearn (various models), sklearn.model_selection
3. Evaluation:Sklearn metrics
4. Visualization: Matplotlib, Seaborn
5. Model deployment: Pickle and flasks











