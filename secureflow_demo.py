import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import IsolationForest
from datetime import datetime, timedelta
import random
import time
from fpdf import FPDF
import base64

# ==========================================
# CONFIGURATION & PAGE SETUP
# ==========================================
st.set_page_config(
    page_title="Operation SecureFlow | P-1071",
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
    div[data-testid="stSidebarNav"] {display: none;}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# DATA PERSISTENCE (Fixes Jitter)
# ==========================================
def init_session_state():
    """Initialize session state to prevent data regeneration on each interaction."""
    if 'traffic_data' not in st.session_state:
        # Generate data once
        n_samples = 300
        data = {
            'timestamp': [datetime.now() - timedelta(minutes=i) for i in range(n_samples)],
            'packet_size': np.random.normal(500, 50, n_samples),
            'latency_ms': np.random.normal(20, 5, n_samples),
            'requests_per_sec': np.random.normal(100, 10, n_samples)
        }
        df = pd.DataFrame(data)

        # Inject Anomalies
        indices = np.random.choice(n_samples, size=15, replace=False)
        df.loc[indices, 'packet_size'] = np.random.normal(3000, 200, 15)
        df.loc[indices, 'latency_ms'] = np.random.normal(200, 50, 15)

        # Train Model Once
        model = IsolationForest(contamination=0.05, random_state=42)
        features = ['packet_size', 'latency_ms']
        df['anomaly'] = model.fit_predict(df[features])
        df['status'] = df['anomaly'].apply(lambda x: 'Normal' if x == 1 else 'THREAT DETECTED')

        st.session_state.traffic_data = df

    if 'messages' not in st.session_state:
        st.session_state.messages = []

# ==========================================
# PDF GENERATOR
# ==========================================
def create_pdf(report_type):
    """Generate official DoD-style PDF report."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Courier", size=12)

    # Header
    pdf.cell(200, 10, txt="UNCLASSIFIED // FOUO", ln=1, align='C')
    pdf.cell(200, 10, txt=f"SECUREFLOW AUDIT: {report_type.upper()}", ln=1, align='C')
    pdf.cell(200, 10, txt=f"DATE: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Z", ln=1, align='C')
    pdf.line(10, 40, 200, 40)
    pdf.ln(20)

    # Body
    pdf.set_font("Courier", size=10)
    content = [
        "UNIT: USS EXAMPLE (DDG-00)",
        "PILOT ID: P-1071",
        "------------------------------------------------",
        "AUDIT RESULTS:",
        "[ PASS ] FIPS 140-2 ENCRYPTION STANDARDS",
        "[ PASS ] MULTI-FACTOR AUTHENTICATION",
        "[ PASS ] LOG RETENTION POLICY",
        "[ FAIL ] PORT SECURITY (802.1x) - REMEDIATION REQ",
        "------------------------------------------------",
        "AUTOMATED GENERATION via OPERATION SECUREFLOW",
        "DO NOT DISTRIBUTE WITHOUT AUTHORIZATION"
    ]

    for line in content:
        pdf.cell(200, 10, txt=line, ln=1, align='L')

    return pdf.output(dest='S').encode('latin-1')

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

    # Data Source Selection
    mode = st.radio(
        "Data Source",
        ["Synthetic Telemetry (Demo)", "Upload Network Log (CSV)"],
        horizontal=True
    )

    df = pd.DataFrame()

    # MODE A: SYNTHETIC DATA (Demo Mode)
    if mode == "Synthetic Telemetry (Demo)":
        st.caption("📡 STATUS: Using simulated network traffic patterns")
        df = st.session_state.traffic_data

    # MODE B: CSV UPLOAD (Live Data Ingestion)
    else:
        st.caption("📂 STATUS: Ready for external data ingestion")
        uploaded_file = st.file_uploader("Upload Network Log (.csv format)", type=['csv'])

        if uploaded_file is not None:
            try:
                # Read uploaded CSV
                df = pd.read_csv(uploaded_file)

                # Validate required columns
                required = ['packet_size', 'latency_ms']
                if not all(col in df.columns for col in required):
                    st.warning(f"⚠️ Expected columns: {', '.join(required)}. Auto-mapping available columns...")
                    # Fallback to demo data if columns don't match
                    df = st.session_state.traffic_data
                else:
                    # Generate timestamps if not present
                    if 'timestamp' not in df.columns:
                        df['timestamp'] = [datetime.now() - timedelta(minutes=i) for i in range(len(df))]
                    else:
                        # Try to parse timestamp column
                        try:
                            df['timestamp'] = pd.to_datetime(df['timestamp'])
                        except:
                            df['timestamp'] = [datetime.now() - timedelta(minutes=i) for i in range(len(df))]

                    # Run anomaly detection on uploaded data
                    model = IsolationForest(contamination=0.05, random_state=42)
                    df['anomaly'] = model.fit_predict(df[['packet_size', 'latency_ms']])
                    df['status'] = df['anomaly'].apply(lambda x: 'Normal' if x == 1 else 'THREAT DETECTED')

                    st.success(f"✅ Ingested {len(df)} data points. Running inference...")

            except Exception as e:
                st.error(f"Error parsing file: {e}")
                st.info("Reverting to demo mode. Ensure CSV has 'packet_size' and 'latency_ms' columns.")
                return
        else:
            st.info("⬆️ Upload a CSV file to begin analysis")
            return

    # Visualization (works for both modes)
    col1, col2 = st.columns([3, 1])

    with col1:
        fig = px.scatter(df, x='timestamp', y='packet_size', color='status',
                         color_discrete_map={'Normal': '#00CC96', 'THREAT DETECTED': '#EF553B'},
                         title="Network Traffic Analysis (Packet Size vs Time)",
                         labels={'packet_size': 'Packet Size (bytes)'})
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Active Threats")
        threats = df[df['status'] == 'THREAT DETECTED']
        if not threats.empty:
            for _, row in threats.tail(4).iterrows():
                ts = row['timestamp'].strftime('%H:%M:%S') if isinstance(row['timestamp'], datetime) else str(row['timestamp'])
                st.error(f"🚨 {ts}Z\nHigh Latency: {row['latency_ms']:.0f}ms")
        else:
            st.success("System Secure.")

# ==========================================
# CORE COMPONENT 2: PERFORMANCE ANALYTICS
# ==========================================
def run_performance_module():
    st.header("📊 B. Performance Analytics")
    st.caption("Predictive modeling for network degradation")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("System Uptime", "99.98%", "+0.01%")
    col2.metric("Avg Latency", "24ms", "-2ms")
    col3.metric("Bandwidth", "4.2 Gbps", "Stable")
    col4.metric("Active Nodes", "1,240", "Online")

    # Predictive Graph (Forecast)
    dates = pd.date_range(start=datetime.now(), periods=24, freq='H')
    predicted_load = [50 + (i * 1.5) + (random.random() * 10) for i in range(24)]

    df_perf = pd.DataFrame({'Time': dates, 'Predicted CPU Load (%)': predicted_load})

    fig = px.line(df_perf, x='Time', y='Predicted CPU Load (%)', markers=True,
                  title="24-Hour Load Forecast")

    # Add a threshold line
    fig.add_hline(y=85, line_dash="dot", annotation_text="Critical Threshold", line_color="red")
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

    st.plotly_chart(fig, use_container_width=True)

    st.info("💡 **AI Recommendation:** Re-route Traffic Node B-7 to reduce latency spike predicted at 1400Z.")

# ==========================================
# CORE COMPONENT 3: AUTOMATED COMPLIANCE
# ==========================================
def run_compliance_module():
    st.header("✅ C. Automated Compliance Engine")
    st.caption("Automated DoD 8500.01 & NIST 800-53 Validation")

    # Mock Compliance Checks
    compliance_checks = {
        "FIPS 140-2 Encryption": True,
        "MFA Active": True,
        "Patch Management": True,
        "Port Security (802.1x)": False,
        "Log Retention": True
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
        st.subheader("Official Reporting")
        report_type = st.selectbox("Report Type", ["Daily Security Summary", "Full Audit", "Incident Log"])

        if st.button("Generate Official PDF"):
            with st.spinner("Querying Audit Logs & Compiling PDF..."):
                time.sleep(1.5)

            pdf_bytes = create_pdf(report_type)
            b64 = base64.b64encode(pdf_bytes).decode()
            href = f'<a href="data:application/octet-stream;base64,{b64}" download="SECUREFLOW_AUDIT_{int(time.time())}.pdf" style="background-color:#00FF41; color:black; padding:10px; text-decoration:none; border-radius:5px; font-weight:bold;">📥 DOWNLOAD SIGNED PDF</a>'
            st.markdown(href, unsafe_allow_html=True)
            st.success("Report generated and signed.")

# ==========================================
# CORE COMPONENT 4: IT SERVICE PORTAL
# ==========================================
def run_service_portal():
    st.header("⚓ D. IT Service Portal")
    st.caption("AI-Assisted Tier 1 Support")

    col1, col2 = st.columns([2, 1])

    with col1:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Describe your issue (e.g., 'Reset CAC PIN')..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Upgraded AI-Assisted Logic with Randomization
            response = ""
            p_lower = prompt.lower()

            # Dynamic Ticket ID generation to prevent repetition
            ticket_id = f"TKT-{random.randint(1000, 9999)}"

            # 1. Latency / Network Issues
            if any(k in p_lower for k in ["slow", "lag", "internet", "latency", "down", "network", "connection", "wifi", "outage"]):
                options = [
                    f"I've detected packet loss at your local node. Auto-generating **{ticket_id}** for priority re-routing.",
                    f"Network diagnostics indicate high traffic load. Switching your endpoint to the backup gateway. Ref: **{ticket_id}**.",
                    f"Acknowledged. Throughput is below baseline. I have flagged this for the Watch Officer. Ticket **{ticket_id}** created."
                ]
                response = random.choice(options)

            # 2. Access / Password Issues
            elif any(k in p_lower for k in ["password", "pin", "login", "access", "cac", "locked", "account"]):
                options = [
                    "I've initiated the secure reset protocol. Please check your secondary device for 2FA verification.",
                    "Identity verification required. I have queued a reset request with the Security Officer.",
                    "Access denied due to credential expiration. Redirecting you to the identity portal..."
                ]
                response = random.choice(options)

            # 3. Software / Installation
            elif any(k in p_lower for k in ["software", "install", "application", "program", "download"]):
                options = [
                    f"Software request logged. Verifying your authorization level... Ticket **{ticket_id}** created.",
                    "I will push the installer to your device within 5 minutes after security clearance.",
                    f"Checking NMCI approved software list. Request queued as **{ticket_id}**."
                ]
                response = random.choice(options)

            # 4. Crash / Failure (Predictive Support)
            elif any(k in p_lower for k in ["crash", "fail", "error", "broken", "stopped", "freeze"]):
                response = f"⚠️ **PREDICTIVE ALERT:** Logs indicate a memory leak in Server Cluster Alpha. I recommend a preemptive service restart to prevent total outage. Ticket **{ticket_id}** logged."

            # 5. Ticket Status
            elif any(k in p_lower for k in ["ticket", "status"]):
                options = [
                    f"Your most recent ticket is **{ticket_id}** (Status: In Progress). Estimated resolution: 15 minutes.",
                    "Checking active tickets... You have 1 open request with Tier 2 support.",
                    f"Ticket **{ticket_id}** has been escalated to the Watch Officer for expedited handling."
                ]
                response = random.choice(options)

            # 6. Fallback
            else:
                options = [
                    f"Request logged. Routing to Tier 2 support. Ticket **{ticket_id}**.",
                    "I am processing your query against the knowledge base...",
                    "Stand by. Verifying authorization level...",
                    f"I have created **{ticket_id}** and notified the on-duty technician."
                ]
                response = random.choice(options)

            time.sleep(0.7)  # Slightly longer delay feels more "thinking"
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)

    with col2:
        st.subheader("Quick Actions")
        st.button("🔑 Reset CAC PIN", use_container_width=True)
        st.button("📡 Report Outage", use_container_width=True)

# ==========================================
# MAIN NAVIGATION
# ==========================================
def main():
    init_session_state()

    st.sidebar.title("SecureFlow")
    st.sidebar.info("Pilot ID: **P-1071**")
    menu = st.sidebar.radio("Module", ["Dashboard Home", "Security Monitor", "Performance Analytics", "Compliance Engine", "IT Service Portal"])
    st.sidebar.divider()
    st.sidebar.caption("Status: **ONLINE**")
    st.sidebar.caption("Unit: **USS EXAMPLE**")

    # Air-Gap Export Capability
    st.sidebar.markdown("---")
    st.sidebar.caption("🔐 **AIR-GAP EXPORT**")
    with open(__file__, "rb") as file:
        st.sidebar.download_button(
            label="Download Source Protocol",
            data=file,
            file_name="secureflow_core_v1.py",
            mime="text/x-python",
            help="Export system core for offline SIPRNet deployment.",
            use_container_width=True
        )

    if menu == "Dashboard Home":
        st.title("Operation SecureFlow")
        st.warning("⚠️ **SIMULATION MODE:** Displaying synthetic telemetry for Pilot Demo P-1071.")

        col1, col2, col3 = st.columns(3)
        col1.metric("Threats Blocked", "14", "+2")
        col2.metric("Health Score", "94/100", "Optimal")
        col3.metric("Open Tickets", "8", "-5")

        st.markdown("### Mission Objective")
        st.markdown("Demonstrate **AI-driven automation** for Naval IT infrastructure to reduce manual workload and increase operational readiness.")

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
