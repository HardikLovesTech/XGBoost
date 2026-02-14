# 📊 Telco Customer Churn Prediction - Streamlit App

A modern web application built with Streamlit to predict customer churn using a pre-trained XGBoost machine learning model.

## Features

✨ **Key Capabilities:**
- **Real-time Predictions**: Predict customer churn with a single click
- **User-Friendly Interface**: Clean, intuitive design with ivory-white theme
- **Model Insights**: View feature importance, ROC curves, and confusion matrices
- **Result Export**: Download predictions as CSV files
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Cloud-Ready**: Compatible with Streamlit Cloud deployment

## Project Structure

```
XGBoost/
├── app.py                      # Main Streamlit application
├── XGBoost_Model.pkl          # Pre-trained XGBoost model
├── StandardScaler.pkl         # Fitted StandardScaler for feature scaling
├── LabelEncoders.pkl          # Fitted LabelEncoders for categorical features
├── feature_importance.png     # Feature importance visualization
├── roc_curve.png              # ROC curve visualization
├── confusion_matrix.png       # Confusion matrix visualization
├── requirements.txt           # Python dependencies
└── README.md                  # Documentation
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install pandas numpy matplotlib xgboost scikit-learn streamlit>=1.28.0 joblib
```

## Usage

### Run the Application Locally

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### Using the App

1. **Fill Customer Information**:
   - Select or enter customer details in the form
   - All fields are required

2. **Make Prediction**:
   - Click the "🔮 Predict" button
   - Wait for the model to process the input

3. **View Results**:
   - See the churn prediction (Churn / No Churn)
   - Check the probability percentage
   - View the confidence progress bar

4. **Export Results**:
   - Click "📥 Download Prediction as CSV" to save the result

5. **View Model Metrics**:
   - Check the sidebar for model performance metrics
   - View visualizations: feature importance, ROC curve, confusion matrix

## Input Features

The model uses the following 19 features for prediction:

### Categorical Features
- **Gender**: Male, Female
- **SeniorCitizen**: Yes, No
- **Partner**: Yes, No
- **Dependents**: Yes, No
- **PhoneService**: Yes, No
- **MultipleLines**: Yes, No, No phone service
- **InternetService**: DSL, Fiber optic, No
- **OnlineSecurity**: Yes, No, No internet service
- **OnlineBackup**: Yes, No, No internet service
- **DeviceProtection**: Yes, No, No internet service
- **TechSupport**: Yes, No, No internet service
- **StreamingTV**: Yes, No, No internet service
- **StreamingMovies**: Yes, No, No internet service
- **Contract**: Month-to-month, One year, Two year
- **PaperlessBilling**: Yes, No
- **PaymentMethod**: Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic)

### Numeric Features
- **Tenure**: 0-72 months
- **MonthlyCharges**: 0-150 (USD)
- **TotalCharges**: 0-10000 (USD)

## Model Performance

- **Balanced Accuracy**: 82.13%
- **ROC AUC Score**: 88.47%

## Deployment

### Deploy on Streamlit Cloud

1. **Prepare Your Repository**:
   - Push your code to a GitHub repository
   - Ensure all required files are present

2. **Connect to Streamlit Cloud**:
   - Go to [Streamlit Cloud](https://share.streamlit.io/)
   - Click "New app"
   - Select your repository and branch
   - Set main file path to `XGBoost/app.py`

3. **Deploy**:
   - Click "Deploy"
   - Your app will be live in minutes

### Deploy on Other Platforms

The app can also be deployed on:
- **Heroku**: Use `Procfile` for configuration
- **AWS**: Using EC2 or AppRunner
- **Google Cloud**: Using Cloud Run
- **Azure**: Using App Service
- **Digital Ocean**: Using App Platform

## Technical Details

### Model Architecture
- **Algorithm**: XGBoost (Extreme Gradient Boosting)
- **Task**: Binary Classification
- **Objective**: binary:logistic
- **Evaluation Metric**: Area Under the Precision-Recall Curve (AUCPR)

### Data Processing Pipeline
1. **Input Validation**: Ensures all inputs are within valid ranges
2. **Categorical Encoding**: Uses pre-trained LabelEncoders
3. **Feature Scaling**: Applies StandardScaler to normalize numerical features
4. **Prediction**: XGBoost model generates prediction and probability

### Code Structure
```python
# Key Functions
load_model_and_preprocessing()    # Load pre-trained objects
get_feature_config()              # Define feature schema
encode_and_scale_input()          # Process user inputs
validate_inputs()                 # Validate input data
make_prediction()                 # Generate predictions
create_prediction_csv()           # Export results
main()                            # Main app logic
```

## Error Handling

The application includes robust error handling for:
- ❌ Missing or invalid input files
- ❌ Invalid input values
- ❌ Data type mismatches
- ❌ Model prediction errors
- ❌ File I/O errors

## Security Notes

- ✅ No model retraining within the app
- ✅ No sensitive data storage
- ✅ Uses read-only model files
- ✅ No external API calls
- ✅ Safe for cloud deployment

## Browser Compatibility

Works with:
- Chrome/Chromium
- Firefox
- Safari
- Edge
- Mobile browsers (iOS Safari, Chrome Mobile)

## Troubleshooting

### App won't start
```bash
# Clear Streamlit cache
streamlit cache clear

# Try running again
streamlit run app.py
```

### Model files not found
- Ensure `XGBoost_Model.pkl`, `StandardScaler.pkl`, and `LabelEncoders.pkl` are in the same directory as `app.py`
- Check file permissions

### Prediction errors
- Verify all input fields are filled
- Check that numeric inputs are within valid ranges
- Ensure model files are not corrupted

## Performance

- **Startup Time**: < 3 seconds
- **Prediction Time**: < 100ms per prediction
- **Memory Usage**: ~150MB

## Requirements File Content

```
pandas
numpy
matplotlib
xgboost
scikit-learn
streamlit>=1.28.0
joblib
```

## License

This project is provided as-is for educational and commercial purposes.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the model documentation
3. Verify all files are in the correct location
4. Check Python version compatibility

---

**Last Updated**: February 2026
**Python Version**: 3.8+
**Streamlit Version**: 1.28.0+
