# src/spark_plug_utils/anomaly_definitions.py

ANOMALY_TYPES = [
    "normal_condition", # It's often good to have a "normal" or "no anomaly" category
    "overheating",
    "electrode_wear",
    "oil_fouling",
    "carbon_fouling", 
    "rust",
    "lead_fouling",
    "ash_deposits" 
]

def get_anomaly_types():
    """Returns the predefined list of spark plug anomaly types."""
    return ANOMALY_TYPES

def print_anomaly_details(anomaly_name: str):
    """
    Prints a placeholder detail string for a given anomaly type.
    In a real application, this might fetch details from a database or a more complex config.
    """
    if anomaly_name in ANOMALY_TYPES:
        print(f"Details for {anomaly_name}: [Placeholder - more information would go here, e.g., visual cues, causes, remedies].")
    else:
        print(f"Warning: Anomaly type '{anomaly_name}' is not defined.")