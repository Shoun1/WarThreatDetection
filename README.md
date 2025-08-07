WarRiskX is a secure, dynamic, and scalable web-based platform built with Django, initially conceptualized as a Software as a Service (SaaS) solution.

Designed primarily for defense applications, this threat detection and rapid prototyping tool is compatible with Windows, Linux, and macOS. It functions as an intelligent location tracking system that identifies the GPS coordinates of enemy targets by analyzing thermal imagery — offering an alternative to traditional drone surveillance systems.

The following is a brief description of the web platform I developed from scratch:
### 1. *Custom Email-Based Authentication*
(i)scalable,modular code
(ii)enforcing password policies with strict data validation

### 2. *Thermal Image Preprocessing(realistic and feasible)*
(i)Supports grayscale image reading and binary thresholding

(ii)Detects high-heat signatures from thermal imagery

(iii)Contour-based object localization using OpenCV

(iv)acts as a preprocessing pipeline essential for the data preparation

### 3. *Gunpoint Detection Prototype-my innovation*

(i)Uses Haar cascade classifiers to detect firearms in uploaded frames

(ii)Gunpoint localization with bounding box logic

(iii)Compatible with future integration of Vision Transformers (ViT) or YOLO models

### 4. *Enemy Movement Mapping with Folium-enable movement tracking with real-time data if possible*
(i)Converts detected image coordinates into approximate GPS data

(ii)Plots markers on an interactive map using Folium

(iii)Automatically saves map to enemy_tracking_map.html for visualization

### 5. *File Upload & Tracking Dashboard-utility of Django's FileSystemStorage to store the data securely and conveniently*
(i)Upload thermal/GunPoint images directly from the UI

(ii)Dynamically view uploaded files

(iii)Built with Django’s file system integration and ORM

Tech Stack
| Layer            | Tech Used                   |
| ---------------- | --------------------------- |
| Backend          | Django (MVT Architecture)   |
| Authentication   | Custom Email Backend        |
| Image Processing | OpenCV, Haar Cascades       |
| Mapping          | Folium                      |
| Frontend         | Django Templates, Bootstrap |
| Storage          | Django File System Storage  |
| Database         | SQLite / PostgreSQL         |

**Agile Techniques**

1. Incremental development through functional MVP (authentication, upload, tracking)
2. Iterative enhancements (Haar cascade prototype, ViT-ready architecture)
3. Rapid feedback via visual outputs (Folium maps, OpenCV image results)
4. Lack of formal Agile structure (no sprints, user stories, CI/CD)
5. No test automation or collaborative workflow (solo development)

**Data Structures / OOPs Aspects**

1. Use of classes (`Tracking`, `Transformer`, `ViT`) demonstrating OOP design
2. Encapsulation of logic in Django views and utility functions
3. Use of lists and tuples for storing image contours and coordinates
4. Modular file handling via Django’s FileSystemStorage abstraction
5. Lack of inheritance or interface design in detection logic and model layers

#Clone and Set Up Environment
git clone https://github.com/your-username/warrisk.git
cd warrisk
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt

Run Migrations & Start Server

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

http://127.0.0.1:8000/








