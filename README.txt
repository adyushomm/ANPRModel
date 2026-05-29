**LINE NO-17 app.py, set gpu=False if your dont have dedicated graphics card or your if your code fails to run on gpu=True**

READ GUIDE THOROUGHLY TO SMOOTHLY EXECUTE THE PROGRAM

File Details
1. app.py: This is the main file that runs on local system
2. best.pt: This is the best trained model trained using YOLOv8

Import all dependencies mentioned below to make sure the code runs(It might take few minutes)
pip install streamlit opencv-python numpy easyocr ultralytics Pillow

When you try to download all these dependencies your IDE might prompt you to create a virtual envroment to avoid global version conflicts, go ahead and create it

You'd see a .venv file in your project folder after you agree to it. Incase the virtual environment is not active, type ".\.venv\Scripts\activate" in your dedicated terminal

To run the program type "streamlit run app.py". Now the program will succesfulluy run and you'd be redirected to your browser for output

Go ahead and upload images of vehicles to extract their number plate details. Make sure the images are well lit are clearly visible. I have also added few images, feel free to use them

Project Report: https://docs.google.com/document/d/1T7yjYyxGJbJx1zoU7sQPvySYBn7SSphv/edit?usp=sharing&ouid=116545288638278623396&rtpof=true&sd=true