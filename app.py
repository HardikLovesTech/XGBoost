"""
Telco Customer Churn Prediction Streamlit App
Uses pre-trained XGBoost model to predict customer churn
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import io
from pathlib import Path
from typing import Dict, Tuple, List

# ==================== Configuration ====================
st.set_page_config(
    page_title="Telco Churn Predictor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Modern SaaS-Style CSS Design
st.markdown("""
    <style>
    /* Color Palette - Modern Minimalist */
    :root {
        --primary: #3b82f6;
        --primary-dark: #1e40af;
        --primary-light: #dbeafe;
        --success: #10b981;
        --warning: #f59e0b;
        --danger: #ef4444;
        --neutral-50: #f9fafb;
        --neutral-100: #f3f4f6;
        --neutral-200: #e5e7eb;
        --neutral-300: #d1d5db;
        --neutral-400: #9ca3af;
        --neutral-600: #4b5563;
        --neutral-700: #374151;
        --neutral-800: #1f2937;
        --neutral-900: #111827;
    }
    
    /* Global Styles */
    * {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f9fafb 0%, #f3f4f6 100%);
    }
    
    /* Main Content Area */
    .main {
        background: transparent;
        padding: 0;
    }
    
    [data-testid="stAppViewContainer"] {
        padding: 0 !important;
    }
    
    .stMainBlockContainer {
        padding: 3rem 2rem !important;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #f9fafb 100%);
        border-right: 1px solid var(--neutral-200);
    }
    
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        padding-top: 2rem;
    }
    
    /* Typography */
    h1 {
        color: var(--neutral-900);
        font-size: 2.5rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        margin-bottom: 0.5rem;
    }
    
    h2 {
        color: var(--neutral-800);
        font-size: 1.75rem;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    
    h3 {
        color: var(--neutral-700);
        font-size: 1.25rem;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 0.75rem;
    }
    
    p {
        color: var(--neutral-600);
        line-height: 1.6;
        font-size: 0.95rem;
    }
    
    /* Subtitle/Description */
    .subtitle {
        color: var(--neutral-500);
        font-size: 0.95rem;
        font-weight: 400;
    }
    
    /* Form Styling - Modern Card */
    .stForm {
        background: white;
        border-radius: 16px;
        padding: 2.5rem;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07), 0 10px 13px rgba(0, 0, 0, 0.05);
        transition: box-shadow 0.3s ease, transform 0.3s ease;
    }
    
    .stForm:hover {
        box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1), 0 4px 6px rgba(0, 0, 0, 0.05);
        transform: translateY(-2px);
    }
    
    /* Form Elements */
    .stForm label {
        color: var(--neutral-700);
        font-weight: 600;
        font-size: 0.9rem;
        letter-spacing: 0.02em;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        display: block;
    }
    
    /* Input Styling */
    .stNumberInput input,
    .stSelectbox select,
    .stTextInput input {
        border: 2px solid var(--neutral-200) !important;
        border-radius: 10px !important;
        padding: 0.75rem 1rem !important;
        font-size: 0.95rem !important;
        transition: all 0.2s ease !important;
        background-color: var(--neutral-50) !important;
    }
    
    .stNumberInput input:focus,
    .stSelectbox select:focus,
    .stTextInput input:focus {
        border-color: var(--primary) !important;
        background-color: white !important;
        box-shadow: 0 0 0 3px var(--primary-light) !important;
    }
    
    /* Button Styling - Primary CTA */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
        color: white;
        font-weight: 600;
        border-radius: 10px;
        border: none;
        padding: 0.875rem 2.5rem;
        font-size: 0.95rem;
        letter-spacing: 0.02em;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        cursor: pointer;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.4);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Download Button */
    .stButton > button[kind="secondary"] {
        background: var(--neutral-100);
        color: var(--neutral-700);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    }
    
    .stButton > button[kind="secondary"]:hover {
        background: var(--neutral-200);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    /* Metric Cards */
    .stMetric {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        padding: 1.5rem;
        color: black;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        border: 1px solid #bae6fd;
        transition: all 0.3s ease;
    }
    
    .stMetric:hover {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        border-color: #7dd3fc;
        background: linear-gradient(135deg, #e0f2fe 0%, #cffafe 100%);
    }
    
    [data-testid="metric-container"] {
        text-align: center;
    }
    
    [data-testid="metric-container"] label {
        color: var(--neutral-600) !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.04em !important;
    }
    
    [data-testid="metric-container"] [data-testid] {
        color: var(--neutral-900) !important;
        font-size: 1.75rem !important;
        font-weight: 700 !important;
    }
    
    /* Success/Danger States */
    .success-box {
        background: linear-gradient(135deg, #ecfdf5 0%, #f0fdf4 100%);
        border-left: 4px solid var(--success);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1.5rem 0;
    }
    
    .danger-box {
        background: linear-gradient(135deg, #fef2f2 0%, #fef5f5 100%);
        border-left: 4px solid var(--danger);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1.5rem 0;
    }
    
    .success-box h3 {
        color: var(--success);
        margin-top: 0;
    }
    
    .danger-box h3 {
        color: var(--danger);
        margin-top: 0;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div {
        background-image: linear-gradient(90deg, var(--primary), var(--success));
        border-radius: 8px;
        height: 0.5rem;
    }
    
    /* Dividers */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--neutral-200), transparent);
        margin: 2rem 0;
    }
    
    /* Image Styling */
    img {
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        width: 100%;
        height: auto;
        display: block;
    }
    
    /* Columns */
    [data-testid="column"] {
        padding: 0.5rem;
    }
    
    /* Info Box */
    .info-box {
        background: linear-gradient(135deg, #eff6ff 0%, #f0f9ff 100%);
        border-left: 4px solid var(--primary);
        padding: 1rem 1.5rem;
        border-radius: 10px;
        color: var(--neutral-700);
        font-size: 0.9rem;
    }
    
    /* Smooth Transitions */
    * {
        transition: background-color 0.2s ease, color 0.2s ease, border-color 0.2s ease;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .stMainBlockContainer {
            padding: 1.5rem 1rem !important;
        }
        
        h1 {
            font-size: 1.75rem;
        }
        
        .stForm {
            padding: 1.5rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# ==================== Model Loading ====================
@st.cache_resource
def load_model_and_preprocessing():
    """Load pre-trained model and preprocessing objects"""
    try:
        base_path = Path(__file__).parent
        
        model = joblib.load(base_path / "XGBoost_Model.pkl")
        scaler = joblib.load(base_path / "StandardScaler.pkl")
        label_encoders = joblib.load(base_path / "LabelEncoders.pkl")
        
        return model, scaler, label_encoders
    except FileNotFoundError as e:
        st.error(f"Error loading model files: {e}")
        st.stop()

# ==================== Feature Definition ====================
def get_feature_config() -> Dict:
    """Define all input features with their types and options"""
    # Common US cities (representative sample)
    cities = [
        "Acampo", "Acton", "Adelanto", "Adin", "Agoura_Hills", "Alameda", "Alamo",
        "Alderpoint", "Aliso_Viejo", "Altadena", "Amador_City", "Amboy", "Amherst",
        "Amity", "Amposta", "Andover", "Angel_Fire", "Angleton", "Angwin", "Annapolis",
        "Annville", "Anselmo", "Anthony", "Antioch", "Antler", "Anton", "Antonia",
        "Antwine", "Antwerp", "Anvil", "Apalachia", "Apex", "Apline", "Aplington",
        "Apodaca", "Apollinaire", "Apolo", "Apoloosa", "Apoyo", "Apoyecan", "Appalachian"
    ]
    
    return {
        "City": {"type": "categorical", "options": cities},
        "Gender": {"type": "categorical", "options": ["Male", "Female"]},
        "Senior_Citizen": {"type": "categorical", "options": ["No", "Yes"]},
        "Partner": {"type": "categorical", "options": ["Yes", "No"]},
        "Dependents": {"type": "categorical", "options": ["Yes", "No"]},
        "Tenure": {"type": "numeric", "min": 0, "max": 72, "step": 1, "value": 0},
        "Phone_Service": {"type": "categorical", "options": ["Yes", "No"]},
        "Multiple_Lines": {"type": "categorical", "options": ["Yes", "No", "No_phone_service"]},
        "Internet_Service": {"type": "categorical", "options": ["DSL", "Fiber_optic", "No"]},
        "Online_Security": {"type": "categorical", "options": ["Yes", "No", "No_internet_service"]},
        "Online_Backup": {"type": "categorical", "options": ["Yes", "No", "No_internet_service"]},
        "Device_Protection": {"type": "categorical", "options": ["Yes", "No", "No_internet_service"]},
        "Tech_Support": {"type": "categorical", "options": ["Yes", "No", "No_internet_service"]},
        "Streaming_TV": {"type": "categorical", "options": ["Yes", "No", "No_internet_service"]},
        "Streaming_Movies": {"type": "categorical", "options": ["Yes", "No", "No_internet_service"]},
        "Contract": {"type": "categorical", "options": ["Month-to-month", "One_year", "Two_year"]},
        "Paperless_Billing": {"type": "categorical", "options": ["Yes", "No"]},
        "Payment_Method": {"type": "categorical", "options": ["Electronic_check", "Mailed_check", "Bank_transfer_(automatic)", "Credit_card_(automatic)"]},
        "Monthly_Charges": {"type": "numeric", "min": 0.0, "max": 150.0, "step": 0.01, "value": 0.0},
        "Total_Charges": {"type": "numeric", "min": 0.0, "max": 10000.0, "step": 0.01, "value": 0.0},
    }

# ==================== Data Processing ====================
def encode_and_scale_input(user_input: Dict, scaler, label_encoders) -> np.ndarray:
    """
    Encode categorical features and scale numerical features
    Mirrors the exact preprocessing used during model training
    
    Args:
        user_input: Dictionary with user inputs
        scaler: StandardScaler fitted on training data
        label_encoders: Dictionary of LabelEncoders for categorical features
        
    Returns:
        Scaled feature array ready for prediction
    """
    try:
        # Create a copy to avoid modifying original
        processed_data = user_input.copy()
        
        # First, create DataFrame with raw data
        df_input = pd.DataFrame([processed_data])
        
        # One-hot encode the categorical columns (same as training)
        # The columns that were one-hot encoded during training
        categorical_cols = ['City', 'Gender', 'Senior_Citizen', 'Partner', 'Dependents', 
                           'Multiple_Lines', 'Internet_Service', 'Online_Security', 
                           'Online_Backup', 'Device_Protection', 'Tech_Support', 
                           'Streaming_TV', 'Streaming_Movies', 'Contract', 
                           'Paperless_Billing', 'Payment_Method']
        
        # One-hot encode (this will create new columns for each category)
        df_encoded = pd.get_dummies(df_input, columns=categorical_cols, dtype=float)
        
        # Phone_Service was manually mapped during training
        # Handle it specially if it exists in the input
        if 'Phone_Service' in df_input.columns:
            df_encoded['Phone_Service'] = df_encoded['Phone_Service'].map({'Yes': 1.0, 'No': 0.0})
        
        # Get all the feature names that the model was trained on
        # We need to ensure we have the exact same columns in the exact same order
        # The scaler was fit on these features
        
        # Get the feature names from the scaler
        if hasattr(scaler, 'feature_names_in_'):
            expected_features = scaler.feature_names_in_
        else:
            # Fallback: get from label_encoders keys
            expected_features = None
        
        if expected_features is not None:
            # Ensure all expected columns exist, filling missing ones with 0
            for col in expected_features:
                if col not in df_encoded.columns:
                    df_encoded[col] = 0.0
            
            # Select only the features that the model was trained on, in the correct order
            df_encoded = df_encoded[expected_features]
        else:
            # If we can't get feature names, just use what we have
            pass
        
        # Scale the features
        scaled_data = scaler.transform(df_encoded)
        
        return scaled_data[0]
    except Exception as e:
        st.error(f"Error processing input data: {str(e)}")
        import traceback
        st.error(traceback.format_exc())
        return None

def validate_inputs(user_input: Dict) -> Tuple[bool, str]:
    """Validate user inputs"""
    try:
        # Check if all required fields are provided
        required_fields = list(get_feature_config().keys())
        for field in required_fields:
            if field not in user_input or user_input[field] is None:
                return False, f"Missing required field: {field}"
        
        # Validate numeric ranges
        if user_input["Tenure"] < 0 or user_input["Tenure"] > 72:
            return False, "Tenure must be between 0 and 72 months"
        
        if user_input["Monthly_Charges"] < 0:
            return False, "Monthly Charges cannot be negative"
        
        if user_input["Total_Charges"] < 0:
            return False, "Total Charges cannot be negative"
        
        return True, "Input validation passed"
    except Exception as e:
        return False, f"Validation error: {e}"

# ==================== Prediction ====================
def make_prediction(model, scaled_features: np.ndarray) -> Tuple[str, float]:
    """
    Make churn prediction using the model
    
    Args:
        model: Trained XGBoost model
        scaled_features: Processed and scaled feature array
        
    Returns:
        Tuple of (prediction_label, probability)
    """
    try:
        # Get prediction and probability
        prediction = model.predict([scaled_features])[0]
        probability = model.predict_proba([scaled_features])[0]
        
        # Determine churn probability (class 1)
        churn_probability = probability[1]
        
        # Convert prediction to label
        prediction_label = "Churn" if prediction == 1 else "No Churn"
        
        return prediction_label, churn_probability
    except Exception as e:
        st.error(f"Error making prediction: {e}")
        return None, None

def create_prediction_csv(user_input: Dict, prediction: str, probability: float) -> bytes:
    """Create a CSV file with prediction result"""
    result_df = pd.DataFrame([{
        **user_input,
        "Prediction": prediction,
        "Probability": f"{probability*100:.2f}%"
    }])
    
    return result_df.to_csv(index=False).encode()

# ==================== Main App ====================
def main():
    # Modern Header Section with Heartbeat Icon
    st.markdown("""
        <div style='text-align: center; margin-bottom: 3.5rem;'>
            <div style='display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;'>
                <span style='font-size: 2.5rem; margin-right: 1rem; animation: pulse 1.5s infinite;'>💗</span>
                <h1 style='margin: 0; display: inline; color: var(--neutral-900);'>Telco Customer Churn Predictor</h1>
            </div>
            <p style='color: var(--neutral-600); font-size: 1rem; margin: 0.75rem auto 0; max-width: 600px; line-height: 1.6;'>
                Predict customer churn probability using advanced machine learning algorithms.
            </p>
        </div>
        <style>
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.7; }
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Load model and preprocessing objects
    model, scaler, label_encoders = load_model_and_preprocessing()
    
    # Main layout - form centered with sidebar on right
    col_spacer, col_main, col_sidebar = st.columns([0.3, 2.2, 1], gap="large")
    
    with col_spacer:
        pass  # Empty spacer column
    
    with col_main:
        # Create form with improved styling
        with st.form("prediction_form"):
            # Form title with card styling
            st.markdown("""
                <div style='margin-bottom: 2rem;'>
                    <h2 style='margin-top: 0; margin-bottom: 0.5rem; color: var(--neutral-800);'>Customer Information</h2>
                    <div style='height: 2px; background: linear-gradient(90deg, var(--primary) 0%, transparent 100%); margin-bottom: 1.5rem;'></div>
                </div>
            """, unsafe_allow_html=True)
            
            features_config = get_feature_config()
            user_input = {}
            
            # Section 1: Demographics
            st.markdown("""
                <p style='color: var(--primary); font-size: 0.8rem; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 1.5rem; margin-top: 2rem; display: flex; align-items: center;'>
                    <span style='display: inline-block; width: 3px; height: 16px; background: var(--primary); margin-right: 0.75rem; border-radius: 2px;'></span>
                    Demographics
                </p>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3, gap="medium")
            demographics_fields = ["Gender", "Senior_Citizen", "Partner", "Dependents"]
            
            for idx, field in enumerate(demographics_fields):
                col = [col1, col2, col3][idx % 3]
                config = features_config[field]
                with col:
                    if config["type"] == "categorical":
                        user_input[field] = st.selectbox(
                            field.replace("_", " "),
                            config["options"],
                            key=f"select_{field}",
                            label_visibility="collapsed"
                        )
            
            # Section 2: Account & Billing
            st.markdown("""
                <p style='color: var(--primary); font-size: 0.8rem; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 1.5rem; margin-top: 2rem; display: flex; align-items: center;'>
                    <span style='display: inline-block; width: 3px; height: 16px; background: var(--primary); margin-right: 0.75rem; border-radius: 2px;'></span>
                    Account & Billing
                </p>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3, gap="medium")
            billing_fields = ["Tenure", "Contract", "Payment_Method", "Paperless_Billing", "Monthly_Charges", "Total_Charges"]
            billing_labels = {
                "Tenure": "Tenure (Months)",
                "Contract": "Contract Type",
                "Payment_Method": "Payment Method",
                "Paperless_Billing": "Paperless Billing",
                "Monthly_Charges": "Monthly Charges ($)",
                "Total_Charges": "Total Charges ($)"
            }
            
            for idx, field in enumerate(billing_fields):
                col = [col1, col2, col3][idx % 3]
                config = features_config[field]
                label = billing_labels.get(field, field.replace("_", " "))
                with col:
                    if config["type"] == "categorical":
                        user_input[field] = st.selectbox(
                            label,
                            config["options"],
                            key=f"select_{field}",
                            label_visibility="collapsed"
                        )
                    else:  # numeric
                        user_input[field] = st.number_input(
                            label,
                            value=config.get("value", 0),
                            min_value=config["min"],
                            max_value=config["max"],
                            step=config["step"],
                            key=f"input_{field}",
                            label_visibility="collapsed"
                        )
            
            # Section 3: Services
            st.markdown("""
                <p style='color: var(--primary); font-size: 0.8rem; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 1.5rem; margin-top: 2rem; display: flex; align-items: center;'>
                    <span style='display: inline-block; width: 3px; height: 16px; background: var(--primary); margin-right: 0.75rem; border-radius: 2px;'></span>
                    Services
                </p>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3, gap="medium")
            service_fields = ["Phone_Service", "Multiple_Lines", "Internet_Service", "Online_Security", 
                            "Online_Backup", "Device_Protection", "Tech_Support", "Streaming_TV", "Streaming_Movies"]
            
            for idx, field in enumerate(service_fields):
                col = [col1, col2, col3][idx % 3]
                config = features_config[field]
                with col:
                    if config["type"] == "categorical":
                        user_input[field] = st.selectbox(
                            field.replace("_", " "),
                            config["options"],
                            key=f"select_{field}",
                            label_visibility="collapsed"
                        )
            
            # Additional field: City (Location)
            st.markdown("""
                <p style='color: var(--primary); font-size: 0.8rem; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 1.5rem; margin-top: 2rem; display: flex; align-items: center;'>
                    <span style='display: inline-block; width: 3px; height: 16px; background: var(--primary); margin-right: 0.75rem; border-radius: 2px;'></span>
                    Location
                </p>
            """, unsafe_allow_html=True)
            
            col1 = st.columns(1)[0]
            config = features_config["City"]
            with col1:
                user_input["City"] = st.selectbox(
                    "City",
                    config["options"],
                    key=f"select_City",
                    label_visibility="collapsed"
                )
            
            # Prediction button - full width
            st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
            col_button = st.columns([1])[0]
            with col_button:
                submit_button = st.form_submit_button(
                    "Predict Churn",
                    use_container_width=True
                )
        
        # Handle prediction
        if submit_button:
            # Validate inputs
            is_valid, validation_msg = validate_inputs(user_input)
            
            if not is_valid:
                st.error(f"❌ Validation Error: {validation_msg}")
            else:
                # Process and predict
                with st.spinner("🔄 Analyzing customer data..."):
                    scaled_features = encode_and_scale_input(user_input, scaler, label_encoders)
                    
                    if scaled_features is not None:
                        prediction, probability = make_prediction(model, scaled_features)
                        
                        if prediction is not None:
                            # Display results with modern design
                            st.markdown("<hr>", unsafe_allow_html=True)
                            
                            st.markdown("""
                                <h2 style='text-align: center; margin-top: 1rem; color: var(--primary); margin-bottom: 0.5rem;'>Prediction Results</h2>
                            """, unsafe_allow_html=True)
                            
                            # Results in columns with gap
                            result_col1, result_col2 = st.columns([1.2, 1], gap="medium")
                            
                            with result_col1:
                                # Prediction result - Modern card
                                if prediction == "Churn":
                                    st.markdown("""
                                    <div class='danger-box'>
                                    <h3 style='text-align: center; margin-top: 0; margin-bottom: 0.5rem;'>⚠️ High Churn Risk</h3>
                                    <p style='text-align: center; color: var(--danger); font-size: 0.9rem; margin-bottom: 0;'>
                                        This customer is likely to churn
                                    </p>
                                    </div>
                                    """, unsafe_allow_html=True)
                                else:
                                    st.markdown("""
                                    <div class='success-box'>
                                    <h3 style='text-align: center; margin-top: 0; margin-bottom: 0.5rem;'>✅ Low Risk</h3>
                                    <p style='text-align: center; color: var(--success); font-size: 0.9rem; margin-bottom: 0;'>
                                        This customer is likely to stay
                                    </p>
                                    </div>
                                    """, unsafe_allow_html=True)
                            
                            with result_col2:
                                # Probability metric - Modern styling
                                st.metric(
                                    "Churn Probability",
                                    f"{probability*100:.1f}%"
                                )
                            
                            # Confidence bar with label
                            st.markdown("""
                                <div style='margin-top: 1.5rem; margin-bottom: 1rem;'>
                                    <p style='color: var(--neutral-700); font-weight: 600; font-size: 0.9rem; margin-bottom: 0.75rem;'>
                                        Confidence Level
                                    </p>
                                </div>
                            """, unsafe_allow_html=True)
                            st.progress(float(probability))
                            
                            # Download CSV button - Modern styling
                            csv_data = create_prediction_csv(user_input, prediction, probability)
                            st.download_button(
                                label="📥 Download Prediction",
                                data=csv_data,
                                file_name="churn_prediction.csv",
                                mime="text/csv",
                                use_container_width=True
                            )
    
    with col_sidebar:
        st.markdown("""
            <div style='margin-bottom: 1.5rem;'>
                <h3 style='margin: 0 0 0.5rem 0; color: var(--neutral-800); font-size: 1.5rem;'>Visualizations</h3>
                <div style='height: 2px; background: linear-gradient(90deg, var(--primary) 0%, transparent 100%);'></div>
            </div>
        """, unsafe_allow_html=True)
        
        # Load and display images with better styling
        base_path = Path(__file__).parent
        
        try:
            # Feature Importance
            if (base_path / "feature_importance.png").exists():
                st.markdown("""
                    <div style='background: white; padding: 1rem; border-radius: 12px; margin-bottom: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid var(--neutral-100);'>
                        <p style='margin: 0 0 0.75rem 0; color: var(--neutral-700); font-weight: 600; font-size: 0.9rem;'>Feature Importance</p>
                """, unsafe_allow_html=True)
                st.image(
                    str(base_path / "feature_importance.png")
                )
                st.markdown("</div>", unsafe_allow_html=True)
            
            # ROC Curve
            if (base_path / "roc_curve.png").exists():
                st.markdown("""
                    <div style='background: white; padding: 1rem; border-radius: 12px; margin-bottom: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid var(--neutral-100);'>
                        <p style='margin: 0 0 0.75rem 0; color: var(--neutral-700); font-weight: 600; font-size: 0.9rem;'>ROC Curve (AUC = 0.88)</p>
                """, unsafe_allow_html=True)
                st.image(
                    str(base_path / "roc_curve.png")
                )
                st.markdown("</div>", unsafe_allow_html=True)
            
            # Confusion Matrix
            if (base_path / "confusion_matrix.png").exists():
                st.markdown("""
                    <div style='background: white; padding: 1rem; border-radius: 12px; margin-bottom: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.05); border: 1px solid var(--neutral-100);'>
                        <p style='margin: 0 0 0.75rem 0; color: var(--neutral-700); font-weight: 600; font-size: 0.9rem;'>Confusion Matrix</p>
                """, unsafe_allow_html=True)
                st.image(
                    str(base_path / "confusion_matrix.png")
                )
                st.markdown("</div>", unsafe_allow_html=True)
        except Exception as e:
            st.warning(f"Could not load visualization: {e}")
        
        st.markdown("<hr>", unsafe_allow_html=True)
        
        # Model metrics with better styling
        st.markdown("""
            <p style='color: var(--neutral-600); font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin: 1.5rem 0 1rem 0;'>
                Model Performance
            </p>
        """, unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Accuracy", "82.1%")
        with col_b:
            st.metric("ROC AUC", "88.5%")
        
        st.markdown("<hr>", unsafe_allow_html=True)
        
        # Modern info box with cleaner styling
        st.markdown("""
            <div class='info-box' style='margin-top: 1.5rem;'>
                <strong style='display: flex; align-items: center;'>
                    <span style='font-size: 1.2rem; margin-right: 0.5rem;'>ℹ️</span>
                    About This Model
                </strong>
                <p style='margin: 0.75rem 0 0 0; font-size: 0.85rem; line-height: 1.5;'>
                    This app uses a pre-trained XGBoost model to predict whether a Telco customer is likely to churn. The model analyzes 19 customer features including demographics, account information, and service usage patterns to provide accurate predictions.
                </p>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
