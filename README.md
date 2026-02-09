<h1>🏠 House Price Prediction Using Machine Learning</h1>

<h2>📌 Project Overview</h2>
<p>
This project focuses on developing an end-to-end <b>House Price Prediction System using Machine Learning</b>.
The system predicts the price of a house based on various influencing features such as size, number of rooms,
construction year, and other related attributes. The main goal of the project is to apply Machine Learning
techniques to real-world data and deploy the trained model as a web application.
</p>

<h2>📊 Dataset</h2>
<p>
The dataset used in this project was collected from <b>Kaggle</b>. It contains historical house sales data
with multiple attributes that influence house prices.
</p>
<ul>
  <li>Number of bedrooms</li>
  <li>Number of bathrooms</li>
  <li>Square footage of the house</li>
  <li>Year built and renovation details</li>
  <li>Date of sale</li>
</ul>
<p>
The target variable is the <b>house price</b>.
</p>

<h2>🧹 Data Cleaning and Preprocessing</h2>
<p>
Data cleaning is a crucial step in this project. The dataset contains a <b>date column</b> that cannot be
directly used by Machine Learning models. The date column was converted into a datetime format and then split
into meaningful components such as <b>year, month, and day</b>. The original date column was removed to avoid redundancy.
</p>
<p>
The dataset was also checked for missing values and irrelevant columns. Features that did not contribute
to price prediction or had zero variance were removed. After preprocessing, the data was separated into
independent variables (X) and the dependent variable (y).
</p>

<h2>✂️ Train–Test Split</h2>
<p>
The cleaned dataset was divided into training and testing sets using an <b>80:20 ratio</b>.
</p>
<ul>
  <li>80% of the data was used for training the model</li>
  <li>20% of the data was used for testing the model</li>
</ul>
<p>
This approach helps evaluate the model’s performance on unseen data and prevents overfitting.
</p>

<h2>🤖 Model Training</h2>
<p>
A <b>Linear Regression</b> algorithm was used to train the model. Linear Regression is a supervised learning
algorithm suitable for predicting continuous values such as house prices.
</p>
<p>
The model learns the relationship between input features and the target variable using the equation:
</p>

<pre>
y = m₁x₁ + m₂x₂ + ... + mₙxₙ + c
</pre>

<p>
Where <b>y</b> is the predicted house price, <b>x</b> represents input features,
<b>m</b> represents coefficients, and <b>c</b> is the intercept.
</p>

<h2>📈 Model Evaluation</h2>
<p>
The model performance was evaluated using:
</p>
<ul>
  <li><b>Mean Squared Error (MSE)</b> as the loss function</li>
  <li><b>R² Score</b> as the accuracy metric</li>
</ul>
<p>
These metrics confirmed that the model provides reliable and accurate predictions.
</p>

<h2>🏆 Best Model Selection</h2>
<p>
Linear Regression was selected as the best model due to its simplicity, interpretability,
and good performance on both training and testing data. It effectively predicts continuous
house price values with minimal overfitting.
</p>

<h2>💾 Model Saving</h2>
<p>
After training, the model was saved using the <b>Pickle</b> library. Saving the model allows it
to be reused for prediction without retraining, which is essential for deployment.
</p>

<h2>🖥️ Frontend & Backend</h2>
<p>
The frontend of the application was developed using <b>HTML and CSS</b> to collect user inputs.
The backend was implemented using the <b>Flask</b> framework, which handles user requests,
loads the trained model, and returns predictions.
</p>

<h2>🚀 Deployment</h2>
<p>
The complete application was deployed on the <b>Render</b> cloud platform.
Users can access the system through a web browser and obtain real-time house price predictions.
</p>

<p>
<b>Live Demo:</b>
<a href="https://house-price-prediction-using-ml-6lpw.onrender.com/" target="_blank">
https://house-price-prediction-using-ml-6lpw.onrender.com/
</a>
</p>

<h2>✅ Results</h2>
<p>
The deployed system successfully predicts house prices based on user inputs.
The integration of Machine Learning, Flask backend, and cloud deployment
demonstrates a complete real-world ML application.
</p>

<h2>🔮 Future Enhancements</h2>
<ul>
  <li>Use advanced algorithms like Random Forest or XGBoost</li>
  <li>Add location-based features</li>
  <li>Improve UI with modern frameworks</li>
  <li>Integrate a database for storing predictions</li>
</ul>

<h2>📚 Conclusion</h2>
<p>
This project demonstrates a complete end-to-end Machine Learning pipeline,
from data preprocessing and model training to deployment as a web application.
It provides practical exposure to real-world Machine Learning implementation.
</p>
