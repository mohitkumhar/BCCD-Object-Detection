import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import pandas as pd

st.title("YOLO Object Detection")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    model = YOLO('best.pt')

    image_np = np.array(image)

    st.write("Detecting objects...")
    results = model(image_np)

    st.image(results[0].plot(), caption="Detected Objects", use_container_width=True)

    st.write("### Detected Objects:")
    data = []
    detected_classes = set()
    
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            conf = float(box.conf[0])
            detected_classes.add(class_id)
            data.append([model.names[class_id], f"{conf:.2f}"])

    total_classes = len(model.names)
    recall = len(detected_classes) / total_classes if total_classes > 0 else 0

    data.append(["Recall", f"{recall:.2f}"])

    df = pd.DataFrame(data, columns=["Class", "Confidence"])
    st.table(df)
