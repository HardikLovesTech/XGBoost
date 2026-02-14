# 🚀 Deployment Guide - Telco Churn Prediction App

## Local Development

### Prerequisites
- Python 3.8+
- pip or conda

### Setup Steps

1. **Clone or navigate to the project**
   ```bash
   cd /path/to/XGBoost/XGBoost
   ```

2. **Create and activate virtual environment** (optional but recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. **Access the app**
   - Open your browser to `http://localhost:8501`

---

## Streamlit Cloud Deployment

### Step 1: Prepare GitHub Repository

1. Fork or create a GitHub repository with your project
2. Structure should be:
   ```
   your-repo/
   ├── XGBoost/
   │   ├── app.py
   │   ├── requirements.txt
   │   ├── .streamlit/
   │   │   └── config.toml
   │   ├── XGBoost_Model.pkl
   │   ├── StandardScaler.pkl
   │   ├── LabelEncoders.pkl
   │   ├── feature_importance.png
   │   ├── roc_curve.png
   │   └── confusion_matrix.png
   └── README.md
   ```

3. Commit and push to GitHub
   ```bash
   git add .
   git commit -m "Add Streamlit app for churn prediction"
   git push origin main
   ```

### Step 2: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit https://share.streamlit.io/
   - Sign in with your GitHub account (or create one)

2. **Create New App**
   - Click "New app"
   - Select your repository
   - Select branch (usually `main`)
   - Set main file path: `XGBoost/app.py`

3. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete (usually 1-3 minutes)
   - Your app will be live at: `https://your-app-name.streamlit.app`

### Step 3: Monitor and Manage

- View logs and app management at https://share.streamlit.io/
- Redeploy by pushing new changes to GitHub
- Update settings or secrets in the Streamlit Cloud dashboard

---

## Alternative Cloud Platforms

### Heroku Deployment

1. **Create Procfile**
   ```
   web: sh setup.sh && streamlit run app.py
   ```

2. **Create setup.sh**
   ```bash
   mkdir -p ~/.streamlit/
   echo "[server]
   headless = true
   port = $PORT
   enableCORS = false
   " > ~/.streamlit/config.toml
   ```

3. **Deploy**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

### Google Cloud Run

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 8080
   CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.enableCORS=false"]
   ```

2. **Deploy**
   ```bash
   gcloud run deploy telco-churn-app \
     --source . \
     --platform managed \
     --region us-central1
   ```

### AWS EC2

1. **Launch EC2 instance** (Ubuntu 20.04 or later)

2. **SSH into instance**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

3. **Setup application**
   ```bash
   sudo apt update && sudo apt install python3-pip python3-venv git
   git clone your-repo-url
   cd your-repo/XGBoost
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Run with systemd**
   - Create `/etc/systemd/system/churn-app.service`:
   ```ini
   [Unit]
   Description=Telco Churn Prediction App
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/your-repo/XGBoost
   ExecStart=/home/ubuntu/your-repo/XGBoost/venv/bin/streamlit run app.py --server.port 8080
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

   - Start service:
   ```bash
   sudo systemctl start churn-app
   sudo systemctl enable churn-app
   ```

5. **Setup reverse proxy with Nginx**
   - Configure Nginx to forward traffic to localhost:8080

---

## Environment Variables

If you need to use environment variables (for Streamlit Cloud secrets):

1. **In Streamlit Cloud Dashboard**
   - Go to app settings
   - Add secrets in TOML format:
   ```toml
   api_key = "your-secret-key"
   ```

2. **Access in app**
   ```python
   import streamlit as st
   api_key = st.secrets["api_key"]
   ```

---

## Performance Optimization

### For Production:

1. **Enable Caching**
   - Already implemented with `@st.cache_resource`
   - Models load once and reuse

2. **Minimize File Size**
   - Use Pickle for model serialization
   - Compress images if needed

3. **Memory Management**
   - Models cached in memory
   - Predictions are fast (~100ms)

### Scalability Notes:

- **Streamlit Cloud Free Tier**: Up to 3 apps, good for demos
- **Paid Tier**: Faster hardware, more apps, better support
- **Custom Deployment**: Full control, higher cost
- **Typical Concurrent Users**: 50+ users on single instance

---

## Monitoring and Troubleshooting

### Check App Status
```bash
# Streamlit Cloud - check logs in dashboard
# Local/Custom - check terminal output
```

### Common Issues

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Install missing package: `pip install package-name` |
| `FileNotFoundError` | Ensure model files are in same directory as app.py |
| `Out of memory` | Increase server resources or optimize data processing |
| `Timeout` | Increase timeout in Streamlit config |
| `CORS errors` | Already disabled in config.toml |

### Debug Mode
```bash
# Run with debug output
streamlit run app.py --logger.level=debug
```

---

## Maintenance

### Regular Updates
```bash
# Update dependencies
pip install --upgrade -r requirements.txt

# Test before deployment
streamlit run app.py
```

### Backup Important Files
- Model files (.pkl)
- Configuration files (.toml)
- Training data (if needed)

### Version Control
- Keep clean git history
- Use meaningful commit messages
- Tag releases: `git tag v1.0.0`

---

## Security Checklist

✅ **Before Deployment:**
- [ ] No hardcoded API keys
- [ ] All model files present
- [ ] Requirements.txt is complete
- [ ] .gitignore includes sensitive files
- [ ] No personal data in code
- [ ] CORS disabled for Streamlit
- [ ] Error handling in place

✅ **For Public Deployment:**
- [ ] Use HTTPS (auto with Streamlit Cloud)
- [ ] Add rate limiting if needed
- [ ] Monitor for suspicious activity
- [ ] Keep dependencies updated
- [ ] Review logs regularly

---

## Getting Help

- **Streamlit Docs**: https://docs.streamlit.io/
- **GitHub Issues**: Check project repository
- **Streamlit Community**: https://discuss.streamlit.io/

---

**Last Updated**: February 2026
