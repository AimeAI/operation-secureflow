# 🏗️ System Architecture

## Tech Stack
*   **Frontend:** [Streamlit](https://streamlit.io/) - Used for rapid dashboard deployment and interactive UI.
*   **Data Processing:** [Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/) - Handles telemetry data manipulation.
*   **Machine Learning:** [Scikit-Learn](https://scikit-learn.org/) - Implements the **Isolation Forest** algorithm for unsupervised anomaly detection.
*   **Visualization:** [Plotly](https://plotly.com/) - Renders interactive, high-performance charts.

## Data Flow
1.  **Data Ingestion (Simulated):** The system generates synthetic network traffic data (Packet Size, Latency, Requests/Sec).
2.  **Preprocessing:** Data is formatted into DataFrames.
3.  **AI Inference:**
    *   The **Isolation Forest** model analyzes features to assign an "Anomaly Score."
    *   Scores of `-1` are flagged as threats.
4.  **UI Rendering:** Streamlit updates the DOM in real-time based on python script execution.

## Key Models
### Anomaly Detection (Security)
*   **Algorithm:** Isolation Forest.
*   **Reasoning:** Effective at identifying outliers in high-dimensional datasets without needing labelled "attack" data (Unsupervised).
*   **Features:** `packet_size`, `latency_ms`.

### Predictive Analytics (Performance)
*   **Method:** Linear trend extrapolation with randomized noise (Simulated for PoC).
*   **Future State:** Will integrate LSTM (Long Short-Term Memory) networks for accurate time-series forecasting.

## Integration Points
*   **Future API:** The app is structured to accept REST API calls from real network hardware (Cisco/Juniper logs).
*   **LLM Integration:** The Chatbot currently uses rule-based logic but is architected to swap in **Gemini** or **Llama 3** models via API for advanced reasoning.

## Security Considerations
*   **Authentication:** Future versions will implement CAC-based authentication
*   **Data Handling:** All simulated data in this PoC; production would use encrypted channels
*   **Audit Logging:** All compliance actions should be logged for review

## Scalability
*   **Current State:** Single-server Streamlit deployment suitable for pilot (up to 100 concurrent users)
*   **Production:** Can be containerized with Docker and deployed to Kubernetes for fleet-wide scale
