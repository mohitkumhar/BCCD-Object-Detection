# Object Detection Web App  
This project is an Object Detection Web App built using a fine-tuned YOLOv10 model on the BCCD dataset. The app is deployed on Hugging Face Spaces and allows users to upload images for detection of WBC, RBC, and platelets, displaying the predicted class, confidence score, and bounding boxes.

## Project Overview  
- Fine-tuning a YOLOv10 model on the BCCD dataset  
- Data augmentation using rotation, cropping, etc.  
- Building an interactive interface using Gradio/Streamlit  
- Displaying predictions, confidence scores, and bounding boxes  
- Showing precision and recall for each class  
- Deploying the app on Hugging Face Spaces  

## Demo  
[Live Demo on Hugging Face](https://huggingface.co/spaces/mohitkumhar/Healthcare_Systems)  

## Dataset  
- BCCD Dataset: [https://github.com/Shenggan/BCCD_Dataset](https://github.com/Shenggan/BCCD_Dataset)  
- The dataset contains labeled images for detecting White Blood Cells (WBC), Red Blood Cells (RBC), and Platelets.  

## Setup and Installation  
### 1. Clone the Repository  
```bash
git clone https://github.com/mohitkumhar/BCCD-Object-Detection.git  
cd Healthcare_Systems
```

### 2. Create a Virtual Environment  
```bash
python -m venv venv  
source venv/bin/activate   # On Windows use: .\venv\Scripts\activate  
```
### 3. Install Dependencies  
```bash
pip install -r requirements.txt  
```

## Usage  
### 1. Run the App Locally  
To start the app locally:  
```bash
streamlit run app.py  
```  

### 2. Upload an Image  
- The app will display:  
  - Bounding boxes for detected objects  
  - Predicted class and confidence score  
  - Precision and recall for each class  

## Model Training  
1. Fine-tuned YOLOv10 using Ultralytics framework  
2. Applied data augmentation (rotation, cropping, flipping, etc.) to improve accuracy  
3. Inference function to process the image and generate predictions  

## Performance  
| Class | Precision |  
|-------|-----------|
| WBC   | .95       |  
| RBC   | .93       |  
| Platelets | .91   |
| Recall | 0.67     |

## Deployment  
### 1. Create a Hugging Face Space  
- Framework: Streamlit  
- Push the code to the space:
```bash
git add .  
git commit -m "Initial commit"  
git push  
```

## Features  
- Real-time object detection  
- Clean and intuitive UI  
- Supports multiple class predictions  
- Precision and recall table  
- Easy deployment on Hugging Face Spaces  

## Contributing  
Feel free to fork the repository and submit a pull request!  

## License  
This project is licensed under the MIT License.  

## Author  
**Mohit Kumhar**  
[GitHub](https://github.com/mohitkumhar) | [Hugging Face](https://huggingface.co/mohitkumhar)  

If you like this project, give it a ⭐ on GitHub!
