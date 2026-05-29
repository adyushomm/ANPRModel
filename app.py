import streamlit as st
import cv2
import numpy as np
import easyocr
from ultralytics import YOLO
from PIL import Image

st.set_page_config(page_title="ANPR System", layout="centered")
st.title("Automated Number Plate Recognition")
st.markdown("Upload an image of a vehicle to extract the license plate number.")

@st.cache_resource
def load_models() -> tuple:
    
    try:
        object_detector = YOLO('best.pt')
        text_reader = easyocr.Reader(['en'], gpu=True) 
        return object_detector, text_reader
    except Exception as e:
        st.error(f"Failed to initialize models: {e}")
        return None, None

model, ocr = load_models()

if model and ocr:
    uploaded_file = st.file_uploader("Select Vehicle Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        img_array = np.array(image)
        img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        if st.button("Process Image", use_container_width=True):
            with st.spinner("Analyzing..."):
                
                results = model(img_bgr)[0]
                
                if len(results.boxes) > 0:
                    x1, y1, x2, y2 = results.boxes[0].xyxy[0].cpu().numpy().astype(int)
                    plate_crop = img_array[y1:y2, x1:x2]
                    
                    raw_text_list = ocr.readtext(plate_crop, detail=0, allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
                    raw_text = "".join(raw_text_list)
                    
                    final_plate_number = raw_text.replace("IND", "").replace("INO", "").replace("IN0", "").replace(" ", "").upper()
                    
                    st.success("Extraction successful.")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.image(plate_crop, caption="Isolated License Plate", use_container_width=True)
                    with col2:
                        st.metric(label="Recognized Plate Number", value=final_plate_number)
                        
                else:
                    st.warning("No license plate detected in the uploaded image. Please ensure the plate is clearly visible.")