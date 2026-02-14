# Quick Start Guide

## 🚀 Run the App in 30 Seconds

### Option 1: With Virtual Environment (Recommended)

```bash
# Navigate to project directory
cd XGBoost

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

**Result:** App opens at `http://localhost:8501` 🎉

---

### Option 2: Quick Install (System Python)

```bash
cd XGBoost
pip install -r requirements.txt
streamlit run app.py
```

---

## 📝 How to Use the App

1. **Fill in Customer Details**
   - Select or enter all required fields
   - All fields have sensible defaults

2. **Click "🔮 Predict"**
   - Model processes your input instantly
   - Results appear in seconds

3. **View Results**
   - See prediction: **Churn** or **No Churn**
   - Check probability percentage
   - View confidence bar

4. **Download Results**
   - Click "📥 Download Prediction as CSV"
   - Share results with stakeholders

5. **Explore Model**
   - Check sidebar for model metrics
   - View feature importance chart
   - See ROC curve and confusion matrix

---

## 📊 Features at a Glance

| Feature | Details |
|---------|---------|
| **Model** | Pre-trained XGBoost (no retraining) |
| **Accuracy** | 82.13% balanced accuracy |
| **Speed** | <100ms per prediction |
| **Theme** | Clean ivory-white design |
| **Export** | Download predictions as CSV |
| **Mobile** | Works on all devices |

---

## ⚙️ System Requirements

- **Python**: 3.8 or higher
- **RAM**: 512MB minimum
- **Disk**: 500MB for dependencies
- **Browser**: Any modern browser

---

## 🐛 Troubleshooting

### App won't start?
```bash
# Clear cache
streamlit cache clear

# Try again
streamlit run app.py
```

### Missing model files?
Ensure these files are in the same directory as `app.py`:
- `XGBoost_Model.pkl`
- `StandardScaler.pkl`
- `LabelEncoders.pkl`
- `feature_importance.png`
- `roc_curve.png`
- `confusion_matrix.png`

### Dependencies not installing?
```bash
# Try with pip upgrade
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📚 Input Guide

### Customer Information
All fields are required:

**Selection Fields** (Choose from dropdown):
- Gender: Male / Female
- Contract: Month-to-month / One year / Two year
- Internet Service: DSL / Fiber optic / No
- Payment Method: 4 options
- And more... (see form for all options)

**Number Fields** (Enter values):
- Tenure: 0-72 months
- Monthly Charges: $0-150
- Total Charges: $0-10,000

---

## 📊 Model Information

**Algorithm:** XGBoost (Extreme Gradient Boosting)

**Performance Metrics:**
- Balanced Accuracy: **82.13%**
- ROC AUC Score: **88.47%**

**Features Used:** 19 customer attributes

**Prediction Time:** < 100ms

---

## 🌐 Deploy to Cloud

### Streamlit Cloud (Free)
```bash
# 1. Push to GitHub
# 2. Go to https://share.streamlit.io/
# 3. Click "New app"
# 4. Select repo & branch
# 5. Set main file: XGBoost/app.py
# 6. Deploy!
```

More options? See `DEPLOYMENT.md`

---

## 📝 Project Structure

```
XGBoost/
├── app.py                      ← Run this
├── requirements.txt            ← Dependencies
├── XGBoost_Model.pkl          ← Pre-trained model
├── StandardScaler.pkl         ← Feature scaler
├── LabelEncoders.pkl          ← Category encoders
├── feature_importance.png     ← Visualization
├── roc_curve.png              ← Visualization
├── confusion_matrix.png       ← Visualization
├── .streamlit/config.toml     ← Streamlit config
├── STREAMLIT_README.md        ← Full documentation
└── DEPLOYMENT.md              ← Deployment guide
```

---

## ✨ Pro Tips

1. **Experiment with Different Inputs**
   - Try edge cases to understand predictions
   - See how different features affect churn risk

2. **Analyze Patterns**
   - View feature importance in sidebar
   - Understand what drives churn decisions

3. **Export Multiple Predictions**
   - Run multiple scenarios
   - Download all results as CSV

4. **Share Results**
   - Screenshots capture the results
   - CSV downloads work on all devices

---

## 🆘 Support

- Check `STREAMLIT_README.md` for detailed documentation
- See `DEPLOYMENT.md` for deployment options
- Review error messages carefully
- Check terminal output for debugging

---

**Ready to predict customer churn? Run the app now!** 🚀

```bash
streamlit run app.py
```

---

*Version 1.0 | February 2026*
