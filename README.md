# Detectium

Developed by **Raiyan Aaijaz**, **Ayaan Iqbal**, **Mekhael Thaha**, **Mevan Solanga**, **Arine Peltekian**

This project was developed as part of the **Pearl Sullivan Engineering IDEAs Clinic Health Tech Innovation Challenge**. 

## Summary
Detecium is a real-time patient monitoring system designed for individuals at risk of delirium episodes. It integrates **facial expression analysis**, **speech pattern tracking**, and **heartbeat monitoring** to assist clinical staff in early detection and intervention.

## Table of Contents
- [Features](#features)
- [Tools and Technologies](#tools-and-technologies)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)

## Features
- **Facial Expression Analysis:** Real-time monitoring of facial expressions to detect signs of emotional distress using **DeepFace** and **MediaPipe**.  
- **Speech Pattern Analysis:** Detects and tracks speech emotions (e.g., aggression, anxiety) through **speech-to-emotion models**.  
- **Heartbeat Monitoring:** Tracks heart rate and alerts staff to anomalies using an **Arduino-based sensor**.  
- **Web Dashboard:** Interactive interface built with **Next.js** and **Bootstrap** to visualize patient status in real time.  
- **Alerts System:** Notifies medical staff of dangerous or abnormal behaviors, such as mentions of violence or signs of extreme stress.

## Tools and Technologies
| Tool/Technology   | Purpose                                      |
|------------------|----------------------------------------------|
| **Flask**         | Backend server for video streaming and API routes. |
| **Next.js**       | Frontend framework for the web dashboard.    |
| **Bootstrap**     | CSS framework for responsive design.         |
| **OpenCV**        | Video capture and frame processing.          |
| **MediaPipe**     | Facial landmark detection and pose estimation. |
| **DeepFace**      | Emotion detection from facial expressions.   |
| **PyTorch**       | Speech emotion analysis using Hugging Face’s models. |
| **Arduino**       | Heartbeat monitoring and serial data collection. |
| **Hugging Face Transformers** | Speech-to-emotion classification.  |

## System Architecture
The system is composed of three key modules working together:  

1. **Backend (Flask):**  
   - Processes real-time video feed from the webcam.  
   - Handles serial communication with the Arduino for heart rate monitoring.  
   - Manages speech emotion analysis using audio recordings.  

2. **Frontend (Next.js):**  
   - Displays real-time patient data in an easy-to-navigate dashboard.  
   - Shows facial expression tracking, speech analysis, and heart rate monitoring on a single page.

3. **Hardware:**  
   - Arduino connected to a heart rate sensor for continuous monitoring.  

## Installation
**Prerequisites:**  
- Python 3.11 or higher  
- Node.js v22.13.1 or higher  
- Arduino IDE (for setting up the heartbeat monitor)

1. Clone the Repository:
```bash
   git clone https://github.com/your-repo/detectium.git
   cd detectium
```
2. Set up the Backend:
- Create and activate a virtual environment
```bash
  python -m venv venv
  venv\Scripts\activate
```
- Install required Python packages
```bash
  pip install -r requirements.txt
```
3. Set up the Frontend:
```bash
  cd frontend
  npm install
```
4. Set up Arduino:
- Connect Arduino to computer with heartbeat scanner.
- In `apps_util.py` update port value to the port your Arduino is connected to.
4. Run the Backend:
```bash
  python app.py
```
5. Run the Frontend:
```bash
  npm run dev
```

## Usage
1. Access the dashboard at `http://localhost:3000`
2. Monitor Real-Time Data:
   - View live video analysis of facial expressions.
   - Track heart rate on dashboard.
   - Receive alerts when high stress or abnormal speech pattern detected.

## Preview

## License
