import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import IsolationForest
from datetime import datetime, timedelta
import random
import time

# ==========================================
# CONFIGURATION & PAGE SETUP
# ==========================================
st.set_page_config(
    page_title="Operation SecureFlow | PEO Digital",
    page_icon="⚓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stAlert { background-color: #262730; border: 1px solid #4b4b4b; }
    .metric-card { background-color: #262730; padding: 20px; border-radius: 10px; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# CORE COMPONENT 1: AI SECURITY MONITORING
# ==========================================
def generate_network_traffic(n_samples=200):
    """Simulates network traffic data for AI training."""
    # Normal traffic
    data = {
        'timestamp': [datetime.now() - timedelta(minutes=i) for i in range(n_samples)],
        'packet_size': np.random.normal(500, 50, n_samples),
        'latency_ms': np.random.normal(20, 5, n_samples),
        'requests_per_sec': np.random.normal(100, 10, n_samples)
    }
    df = pd.DataFrame(data)

    # Inject Anomalies (Simulated Attacks)
    indices = np.random.choice(n_samples, size=10, replace=False)
    df.loc[indices, 'packet_size'] = np.random.normal(3000, 200, 10) # DDoS packet size
    df.loc[indices, 'latency_ms'] = np.random.normal(200, 50, 10)    # Network congestion

    return df

def run_security_module():
    st.header("🛡️ A. AI-Powered Security Monitoring")
    st.caption("Real-time anomaly detection using Isolation Forest (Unsupervised Learning)")

    # 1. Data Simulation
    df = generate_network_traffic()

    # 2. AI Model Training (Isolation Forest)
    # We use 'packet_size' and 'latency_ms' as features
    model = IsolationForest(contamination=0.05, random_state=42)
    features = ['packet_size', 'latency_ms']
    df['anomaly'] = model.fit_predict(df[features])
    df['status'] = df['anomaly'].apply(lambda x: 'Normal' if x == 1 else 'THREAT DETECTED')

    # 3. Visualization
    col1, col2 = st.columns([3, 1])

    with col1:
        fig = px.scatter(df, x='timestamp', y='packet_size', color='status',
                         color_discrete_map={'Normal': '#00CC96', 'THREAT DETECTED': '#EF553B'},
                         title="Live Network Traffic Analysis",
                         labels={'packet_size': 'Packet Size (bytes)'})
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Live Alerts")
        threats = df[df['status'] == 'THREAT DETECTED']
        if not threats.empty:
            for _, row in threats.tail(5).iterrows():
                st.error(f"🚨 {row['timestamp'].strftime('%H:%M:%S')} | High Latency: {row['latency_ms']:.1f}ms")
        else:
            st.success("System Secure. No active threats.")

# ==========================================
# CORE COMPONENT 2: PERFORMANCE ANALYTICS
# ==========================================
def run_performance_module():
    st.header("📊 B. Performance Analytics Dashboard")
    st.caption("Predictive modeling for network degradation")

    # Simulated Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("System Uptime", "99.98%", "+0.02%")
    col2.metric("Avg Latency", "24ms", "-2ms")
    col3.metric("Bandwidth Usage", "4.2 Gbps", "Stable")
    col4.metric("Active Nodes", "1,240", "All Online")

    # Predictive Graph (Forecast)
    dates = pd.date_range(start=datetime.now(), periods=24, freq='H')
    predicted_load = [50 + (i * 1.5) + (random.random() * 10) for i in range(24)]

    df_perf = pd.DataFrame({'Time': dates, 'Predicted CPU Load (%)': predicted_load})

    fig = px.line(df_perf, x='Time', y='Predicted CPU Load (%)', markers=True,
                  title="24-Hour Performance Forecast (Predictive Analytics)")

    # Add a threshold line
    fig.add_hline(y=85, line_dash="dot", annotation_text="Critical Threshold", annotation_position="bottom right", line_color="red")

    st.plotly_chart(fig, use_container_width=True)

    with st.expander("View Actionable Recommendations"):
        st.info("💡 **Optimization:** Re-route Traffic Node B-7 to reduce latency spike predicted at 14:00.")
        st.info("💡 **Maintenance:** Schedule patch for Server Cluster Alpha during 03:00 low-traffic window.")

# ==========================================
# CORE COMPONENT 3: AUTOMATED COMPLIANCE
# ==========================================
def run_compliance_module():
    st.header("✅ C. Automated Compliance & Reporting")
    st.caption("Automated DoD 8500.01 & NIST 800-53 Checklists")

    # Mock Compliance Checks
    compliance_checks = {
        "Encryption Standards (FIPS 140-2)": True,
        "Multi-Factor Authentication (MFA) Active": True,
        "Patch Management Status": True,
        "Port Security (802.1x)": False,
        "Log Retention Policy": True
    }

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Live Audit Status")
        for check, status in compliance_checks.items():
            if status:
                st.success(f"✔ {check}: COMPLIANT")
            else:
                st.error(f"❌ {check}: NON-COMPLIANT - Action Required")

    with col2:
        st.subheader("Report Generation")
        st.write("Generate audit-ready PDF reports for command review.")

        report_type = st.selectbox("Select Report Type", ["Daily Security Summary", "Compliance Audit (Full)", "Incident Response Log"])

        if st.button("Generate Report"):
            with st.spinner("Gathering data..."):
                time.sleep(1.5) # Simulate processing
            st.balloons()
            st.success(f"📄 **{report_type}** generated successfully. Sent to Command Server.")
            st.download_button("Download Copy (Mock)", data="Mock Report Data", file_name="report.txt")

# ==========================================
# CORE COMPONENT 4: IT SERVICE PORTAL
# ==========================================
def run_service_portal():
    st.header("⚓ D. User-Centric IT Service Portal")
    st.caption("Self-service interface for Sailors & Marines")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("AI Support Assistant")
        st.markdown("""
        **Chat with SecureFlow Bot** (Simulating Tier 1 Support)
        *Try asking: 'Reset my password', 'Internet is slow', or 'Check ticket status'*
        """)

        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat Input
        if prompt := st.chat_input("Type your IT request here..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Simple Logic for Demo
            response = ""
            prompt_lower = prompt.lower()
            if "password" in prompt_lower:
                response = "I can help with that. Please navigate to the **Identity Management Tab** to reset your CAC PIN or network password securely."
            elif "slow" in prompt_lower or "internet" in prompt_lower:
                response = "I've detected high latency in your sector. A ticket (TKT-492) has been auto-generated. Switching your endpoint to a backup gateway..."
            elif "ticket" in prompt_lower:
                response = "You have 1 active ticket: **TKT-492** (Network Lag). Status: *In Progress*."
            else:
                response = "I'm routing this request to the Help Desk. Estimated wait time: 2 minutes."

            time.sleep(0.5)
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)

    with col2:
        st.subheader("Quick Actions")
        st.button("🔑 Reset CAC PIN", use_container_width=True)
        st.button("📥 Install Software", use_container_width=True)
        st.button("📡 Report Outage", use_container_width=True)

        st.info("Latest Notification: Maintenance scheduled for Sunday 0200Z.")

# ==========================================
# MAIN NAVIGATION
# ==========================================
def main():
    st.sidebar.title("SecureFlow v1.0")
    st.sidebar.markdown("**Operation SecureFlow**\n\n*Ready for PEO Digital Pilot*")

    menu = st.sidebar.radio(
        "Navigation",
        ["Dashboard Home", "Security Monitor", "Performance Analytics", "Compliance Engine", "IT Service Portal"]
    )

    st.sidebar.markdown("---")
    st.sidebar.write("Status: **ONLINE** 🟢")
    st.sidebar.write("Unit: **USS Example (DDG-00)**")

    if menu == "Dashboard Home":
        st.title("Operation SecureFlow Command Center")
        st.markdown("""
        **Objective:** Enhance cybersecurity, network performance, and operational resilience for the Navy and Marine Corps.

        ### 🚀 Live Pilot Overview
        Select a module from the sidebar to begin the demonstration.
        """)

        # Summary Metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("Active Threats Blocked", "14", "+2 today")
        col2.metric("Network Health Score", "94/100", "Optimal")
        col3.metric("Open Support Tickets", "8", "-5 from yesterday")

        st.image("https://images.unsplash.com/photo-1558494949-efc527e73126?auto=format&fit=crop&q=80&w=1000", caption="SecureFlow Network Topology Visualization", use_column_width=True)

    elif menu == "Security Monitor":
        run_security_module()
    elif menu == "Performance Analytics":
        run_performance_module()
    elif menu == "Compliance Engine":
        run_compliance_module()
    elif menu == "IT Service Portal":
        run_service_portal()

if __name__ == "__main__":
    main()
