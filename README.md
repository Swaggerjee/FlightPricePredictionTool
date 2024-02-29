# Flight Price Prediction Tool

## Overview
This is a term project completed for the course DS 3010 (Computational Data Intelligence) at Worcester Polytechnic Institute in C-term of 2024. Our group aimed to increase transparency in flight pricing and help consumers make informed decisions when booking flights. By analyzing the [Flight Price Prediction dataset](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction) posted by Shubham Bathwal on Kaggle, collected via the octoparse tool from the “Ease My Trip” website between February 11, 2022, and March 31, 2022, we developed models that can be used to predict flight prices. Our analysis covers 300,261 distinct flight bookings, including details such as airline, flight code, departure and arrival cities, times, class, duration, and days until the flight. Our goal is to demystify flight pricing, aiding travelers in finding affordable prices and boosting their confidence in travel planning.

## Dataset
The dataset includes information on:
- Airline name
- Flight code
- Source and destination cities
- Departure and arrival times
- Number of stops
- Class (business or economy)
- Flight duration
- Days left until flight
- Ticket price

## Tools and Technologies
- **Python**: For all backend operations and data analysis.
- **Pandas and NumPy**: For data manipulation and numerical analysis.
- **Matplotlib**: For data visualization. We considered Seaborn as well, but did not have time to fully utilize it.
- **Scikit-learn**: For developing LinearRegression and Random Forest Regressor predictive models.
- **XGBoost**: For developing an XGBoost predictive model.
- **IPyWidgets**: For creating a simple user interface to test the models like a real flight price prediction tool

## Project Workflow
0. **Setup**: Initial configuration, including library imports and dataset loading.
1. **Data cleaning**: Cleaning the dataset to ensure accuracy for analysis.
2. **Descriptive statistics**: Conducting statistical analysis to summarize the dataset's characteristics.
3. **Data visualization and notes**: Visualizing the data to identify patterns and noting key observations.
4. **Building the models**: Developing models to predict flight prices.
5. **Testing and improving the models**: Evaluating and refining model performance.
6. **(Extra, unfinished) Using GridSearch to optimize**: Optimizing model parameters for better accuracy.
7. **Interface integration**: Creating a simple user interface so users can adjust flight-related factors and get a price prediction.

## How to Use
1. Clone this repository.
2. Ensure you have Python and the required libraries installed.
3. Run the cells in the main Jupyter notebook (`airData.ipynb`) to explore the dataset, model development, and optimization.
4. Follow the instructions within the notebook to use the predictive models and application.

## License
This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Shubham Bathwal on Kaggle, for providing the “Flight Price Prediction” dataset.
- The developers of the tools and libraries we used.
- Professor Kyumin Lee, our course's instructor
- Yiqing Zhang, our course's teaching assistant

## Contact
For any questions or suggestions, feel free to contact us.

---
Happy flying!
