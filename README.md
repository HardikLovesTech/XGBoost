# 🎯 Telco Customer Churn Prediction - Streamlit App

**A production-ready web application for predicting customer churn using XGBoost machine learning.**

[![Status](https://img.shields.io/badge/Status-Ready%20for%20Deployment-brightgreen)](https://github.com)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0%2B-red)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-Open%20Source-green)](LICENSE)

---

## 📊 Overview

This project provides a complete machine learning web application for predicting Telco customer churn. Built with Streamlit and powered by a pre-trained XGBoost model, it offers:

- ✨ **Clean UI** with ivory-white professional design
- 🚀 **Fast Predictions** in <100ms
- 📈 **High Accuracy** - 82.13% balanced accuracy
- 📊 **Model Visualizations** - Feature importance, ROC curves, confusion matrices
- 💾 **CSV Export** - Download predictions easily
- ☁️ **Cloud Ready** - Deploy to Streamlit Cloud, AWS, GCP, or Azure

---

## 🚀 Quick Start

### 1️⃣ Installation (30 seconds)

```bash
# Navigate to project
cd XGBoost

# Install dependencies
pip install -r requirements.txt

# Or with virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2️⃣ Run the App

```bash
streamlit run app.py
```

The app opens automatically at `http://localhost:8501` 🎉

### 3️⃣ Make Predictions

1. Fill in customer information (19 fields)
2. Click "🔮 Predict"
3. View results with probability and confidence
4. Download as CSV (optional)

---

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| **[QUICKSTART.md](QUICKSTART.md)** | Get running in 30 seconds |
| **[STREAMLIT_README.md](STREAMLIT_README.md)** | Full feature documentation |
| **[DEPLOYMENT.md](DEPLOYMENT.md)** | Cloud deployment guides |
| **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** | Complete technical overview |

---

## 🎨 Features

### Prediction Interface
- **19 Input Fields** - All customer attributes
- **Real-time Validation** - Immediate feedback
- **Color-Coded Results** - Green (No Churn) / Red (Churn)
- **Probability Display** - Exact percentage
- **Confidence Bar** - Visual representation

### Model Insights (Sidebar)
- **Model Metrics** - Accuracy & ROC AUC scores
- **Feature Importance** - Top 15 predictive features
- **ROC Curve** - Model performance visualization
- **Confusion Matrix** - Prediction breakdown

### Data Export
- **CSV Download** - All prediction details
- **Easy Sharing** - Send results to stakeholders

---

## 🔧 Technical Stack

**Backend:**
- XGBoost - ML algorithm
- Scikit-learn - Data preprocessing
- Joblib - Model serialization
- Pandas/NumPy - Data processing

**Frontend:**
- Streamlit - Web framework
- Custom CSS - Ivory-white theme
- Responsive Layout - Mobile-friendly

**Deployment:**
- Streamlit Cloud (recommended)
- Docker compatible
- Cloud provider agnostic

---

## 📋 Input Features (19)

**Customer Demographics:**
- Gender, Age (Senior Citizen), Partner status, Dependents

**Services:**
- Phone Service, Multiple Lines, Internet Service type
- Online Security, Backup, Device Protection, Tech Support
- Streaming TV, Streaming Movies

**Billing:**
- Contract type, Paperless Billing, Payment Method
- Monthly Charges, Total Charges, Tenure

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| **Balanced Accuracy** | 82.13% |
| **ROC AUC Score** | 88.47% |
| **Algorithm** | XGBoost |
| **Features** | 1,177 (after encoding) |
| **Prediction Time** | <100ms |

---

## 🚀 Deployment Options

### ☁️ Streamlit Cloud (Recommended)
- Free tier available
- One-click deployment
- Automatic updates
- See [DEPLOYMENT.md](DEPLOYMENT.md)

### 🐳 Docker
- Containerized deployment
- Works everywhere Docker runs

### AWS, GCP, Azure
- Multiple platform guides
- See [DEPLOYMENT.md](DEPLOYMENT.md)

### Local Server
- Nginx reverse proxy
- Systemd service
- See [DEPLOYMENT.md](DEPLOYMENT.md)

---

## 🔒 Project Files

```
XGBoost/
├── 🚀 app.py                    - Main application (15 KB)
├── 📋 requirements.txt          - Dependencies
├── 🤖 XGBoost_Model.pkl        - Pre-trained model (116 KB)
├── 📊 StandardScaler.pkl       - Feature scaling (49 KB)
├── 🔐 LabelEncoders.pkl        - Category encoders (18 KB)
├── 📈 feature_importance.png   - Visualization (54 KB)
├── 📉 roc_curve.png            - Visualization (26 KB)
├── 🎯 confusion_matrix.png     - Visualization (17 KB)
├── .streamlit/config.toml      - Streamlit config
├── 📚 STREAMLIT_README.md      - Full docs (6.5 KB)
├── 🚀 DEPLOYMENT.md            - Deploy guide (6.5 KB)
├── ⚡ QUICKSTART.md            - Quick start (4.4 KB)
└── 📑 PROJECT_SUMMARY.md       - Overview (13.7 KB)
```

**Total Size:** ~400 MB (including venv)
**App Only:** ~400 KB

---

## 🎯 Use Cases

### Customer Retention Teams
- Identify at-risk customers
- Prioritize retention efforts
- Track improvement metrics

### Data Science Teams
- Validate model performance
- Experiment with customer segments
- Generate predictions for campaigns

### Executives & Stakeholders
- View key metrics
- Understand model decisions
- Export results for analysis

### Marketing Teams
- Target high-risk customers
- Personalize retention offers
- Measure intervention effectiveness

---

## ⚙️ System Requirements

| Component | Requirement |
|-----------|------------|
| **Python** | 3.8 or higher |
| **RAM** | 512 MB minimum |
| **Disk** | 500 MB for dependencies |
| **Browser** | Any modern browser |
| **OS** | Windows, macOS, Linux |

---

## 🔧 Configuration

### Theme Customization
Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#4a6fa5"
backgroundColor = "#faf9f6"
```

### Model Updates
Replace model files (don't need to change app code):
- `XGBoost_Model.pkl` - Retrained model
- `StandardScaler.pkl` - Fitted scaler
- `LabelEncoders.pkl` - Fitted encoders

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| App won't start | Run `streamlit cache clear` and try again |
| Model not found | Ensure .pkl files in same directory as app.py |
| Missing dependency | Run `pip install -r requirements.txt` |
| Slow predictions | Increase system RAM or restart app |
| Display issues | Clear browser cache or try different browser |

See [STREAMLIT_README.md](STREAMLIT_README.md) for more help.

---

## 📈 Performance Optimization

- ✅ Model cached in memory (loads once)
- ✅ Predictions cached per session
- ✅ Minimal data transfer
- ✅ Optimized CSS and images
- ✅ Streamlit's fast rendering engine

---

## 🔐 Security & Privacy

✅ **No data storage** - Predictions don't persist
✅ **No model retraining** - Safe, controlled predictions
✅ **No external calls** - Self-contained application
✅ **CORS disabled** - Secure from browser attacks
✅ **Input validation** - Prevents injection attacks

---

## 📞 Support & Help

### Documentation
- **Quick Start:** See [QUICKSTART.md](QUICKSTART.md)
- **Full Features:** See [STREAMLIT_README.md](STREAMLIT_README.md)
- **Deployment:** See [DEPLOYMENT.md](DEPLOYMENT.md)
- **Technical:** See [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)

### Troubleshooting
1. Check relevant documentation file
2. Review error messages carefully
3. Check terminal output for details
4. Clear cache if needed

### Resources
- [Streamlit Docs](https://docs.streamlit.io/)
- [XGBoost Guide](https://xgboost.readthedocs.io/)
- [Scikit-learn Docs](https://scikit-learn.org/)

---

## 🎓 Learning Resources

### Understanding the App
1. Read [QUICKSTART.md](QUICKSTART.md) (5 min)
2. Run the app locally (2 min)
3. Try different inputs (5 min)
4. Review [STREAMLIT_README.md](STREAMLIT_README.md) (10 min)

### Deploying to Production
1. Read [DEPLOYMENT.md](DEPLOYMENT.md) (15 min)
2. Choose platform (5 min)
3. Follow deployment steps (10-30 min)
4. Verify deployment (5 min)

### Understanding the Model
- See "Model Information" in [STREAMLIT_README.md](STREAMLIT_README.md)
- View feature importance in sidebar
- Read [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)

---

## 🚀 Getting Started

### Step 1: Clone/Navigate
```bash
cd XGBoost
```

### Step 2: Install
```bash
pip install -r requirements.txt
```

### Step 3: Run
```bash
streamlit run app.py
```

### Step 4: Predict!
Open browser and start predicting 🎉

---

## 📊 Example Prediction

**Input:** 
- Customer: 45-year-old, 3-month tenure, $89.85/month

**Output:**
- Prediction: **⚠️ CHURN RISK**
- Probability: **73.45%**
- Confidence: [████████░░]

**Recommendation:** High-priority retention candidate

---

## 🤝 Contributing

To improve the app:
1. Test locally
2. Document changes
3. Update model if needed
4. Maintain code quality

---

## 📄 License

Open Source - Feel free to use and modify.

---

## 📝 Version History

| Version | Date | Status |
|---------|------|--------|
| 1.0 | Feb 13, 2026 | ✅ Production Ready |

---

## 🎉 Ready to Use!

```bash
# Start predicting in 2 commands:
cd XGBoost
streamlit run app.py
```

**That's it!** 🚀

---

### Questions?
- 📖 Check [QUICKSTART.md](QUICKSTART.md) for quick answers
- 📚 See [STREAMLIT_README.md](STREAMLIT_README.md) for detailed guide
- 🚀 View [DEPLOYMENT.md](DEPLOYMENT.md) for deployment help
- 📊 Review [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for technical details

**Happy Predicting! 🎯**

---

*Built with ❤️ using Streamlit and XGBoost*  
*Production-Ready | Cloud-Compatible | Easy to Deploy*
