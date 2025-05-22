# examples/run_utils_demo.py

# Because we did 'pip install -e .', we can now directly import our package
from spark_plug_utils import (
    get_anomaly_types,
    print_anomaly_details,
    load_sparkplug_image,
    preprocess_image
)

def main():
    print("--- Spark Plug Anomaly Utilities Demo ---")

    print("\nAvailable Anomaly Types:")
    types = get_anomaly_types()
    for t in types:
        print(f"- {t}")

    print("\nDetails for 'overheating':")
    print_anomaly_details("overheating")
    print_anomaly_details("unknown_anomaly") # Test a non-existent one

    print("\nSimulating Image Loading & Preprocessing:")
    # Example image paths (these don't need to exist for the placeholder functions)
    image1_path = "/path/to/real_spark_plug_images/plug_A_001.jpg"
    image2_path = "spark_plug_dataset/batch1/plug_X_075.png"

    img_data1 = load_sparkplug_image(image1_path)
    if img_data1:
        processed_img1 = preprocess_image(img_data1)
        if processed_img1:
            print(f"Status of processed image 1: {processed_img1.get('status')}")

    print("-" * 20)
    img_data2 = load_sparkplug_image(image2_path) # A different style of path
    if img_data2:
        processed_img2 = preprocess_image(img_data2)
        if processed_img2:
            print(f"Status of processed image 2: {processed_img2.get('status')}")

    print("\n--- Demo Complete ---")

if __name__ == "__main__":
    main()