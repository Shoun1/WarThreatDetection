import cv2  # For image processing
import torch
from torch import nn

from einops import rearrange, repeat
from einops.layers.torch import Rearrange

def pair(t):
    return t if isinstance(t, tuple) else (t, t)

class Transformer(nn.Module):
    def __init__(self,dim,depth,heads,dim_head,mlp_dim,dropout = 0):
        super().__init__()
        self.norm = nn.LayerNorm(dim)
        self.layers = nn.ModuleList([])
        for __,in range(depth):
            self.layers.append(nn.ModuleList([
                Attention(dim,heads=head,dim_head=dim_head,dropout = dropout),
                Feedforward(dim,mlp_dim,dropout=dropout)
            ]))


    def forward(self,x):
        for attn,ff in self.layers:
            x = attn(x) + x
            x = ff(x) + x

        return self.norm(x)

class ViT(nn.Module):
    def __init__(self,*,image_size,patch_size,num_classes,dim,depth,heads,mlp_dim,pool='cls',channels=3,dim_head=64,dropout=0.,emb_dropout=0.):
        super().__init__
        image_height,image_width = pair(image_size)
        patch_height,patch_width = pair(patch_size)

        assert image_height % patch_height == 0 and image_width % patch_width == 0, 'Image dimensions must be divisible by the patch size.'

        num_patches = (image_height*image_width) // (patch_height*patch_width)

        patch_dim = channels*patch_height*patch_width

        assert pool in {'cls', 'mean'}, 'pool type must be either cls (cls token) or mean (mean pooling)'

        self.to_patch_embedding=nn.Sequential(
            Rearrange('b c (h,p1) (w,,p2) -> b (h,w) (p1,p2,c)', p1=patch_height, p2=patch_width),
            nn.LayerNorm(patch_dim),
            nn.Linear(patch_dim, dim),
            nn.LayerNorm(dim),
        )

        self.pos_embeddding = nn.Parameter(torch.randn(1,num_patches+1,dim))
        self.cls_token = nn.Parameter(torch.randn(1,1,dim))
        self.dropout = nn.Dropout(emb_dropout)

        self.transfomer = Transformer(dim, depth, heads, dim_head, mlp_dim, dropout)

        





























import folium
def track_enemy_movements():
    map_display=None
    try:
        # Simulated thermal imaging data (NumPy array)
        # In practice, this would be fetched from sensors or cameras
        thermal_image = cv2.imread('thermalimg.jpg.jpg', cv2.IMREAD_GRAYSCALE)

        # Preprocessing the thermal image
        # Thresholding to highlight potential enemy presence (e.g., higher heat signatures)
        _, threshold_image = cv2.threshold(thermal_image, 128, 255, cv2.THRESH_BINARY)

        # Simulate extracting coordinates of detected enemies
        contours, _ = cv2.findContours(threshold_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        enemy_locations = []
        for contour in contours:
            # Get the center of the contour
            M = cv2.moments(contour)
            if M['m00'] != 0:
                cX = int(M['m10'] / M['m00'])
                cY = int(M['m01'] / M['m00'])
                enemy_locations.append((cX, cY))
        # Plot detected enemy movements on a map
        map_center = [50.0, 30.0]  # Replace with the actual center of your surveillance region
        map_display = folium.Map(location=map_center, zoom_start=12)

        for enemy in enemy_locations:
            # Convert pixel coordinates (thermal image) to real-world GPS (dummy logic)
            latitude = map_center[0] + (enemy[1] - 500) * 0.0001
            longitude = map_center[1] + (enemy[0] - 500) * 0.0001

            # Add markers to the map
            folium.Marker([latitude, longitude], popup="Enemy Detected").add_to(map_display)

        # Save map to an HTML file for visualization
        map_display.save("enemy_tracking_map.html")
        print("Enemy tracking map updated and saved as 'enemy_tracking_map.html'.")

    except Exception as e:
        print("Error processing thermal imaging data:", e)

    return map_display

'''track_enemy_movements()

import matplotlib
import matplotlib.pyplot as plt
import os
#print(os.path.exists('thermalimg.jpg.jpg'))
#matplotlib.use('TkAgg') 
class Tracking():
    def __init__(self,request):
        self.session = request.session
        self.thermal_img = []

    def track_enemy_movements():

        thermal_image = cv2.imread('thermalimg.jpg.jpg',cv2.IMREAD_GRAYSCALE)

        thermal_image = cv2.imread('guns.jpg')

        gun_cascade = cv2.CascadeClassifier('guns1.xml')
        if gun_cascade.empty():
            print("Error loading cascade file.")
        guns = gun_cascade.detectMultiScale(gray_image, 1.3, 5)
        for (x,y,w,h) in guns:
            cv2.rectangle(coloured_image, (x,y), (x+w,y+h), (255,0,0), 2)

        #print(type(thermal_image))

        gray_image = cv2.cvtColor(thermal_image, cv2.COLOR_BGR2GRAY)

        __, threshold_image = cv2.threshold(gray_image,128,255,cv2.THRESH_BINARY)

        #_, binary_image = cv2.threshold(thermal_image, 128, 255, cv2.THRESH_BINARY)

        #plt.imshow(threshold_image,cmap='gray')
        #plt.show()

        contours,_ = cv2.findContours(threshold_image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        enemy_img = cv2.cvtColor(gray_image,cv2.COLOR_GRAY2BGR)
        #plt.imshow(enemy_img)
        #plt.show()
        bottom_left = (654,369)
        top_right = (766,344)
        cv2.rectangle(enemy_img,bottom_left,top_right,(255.,0,0),2)
        plt.imshow(enemy_img)
        plt.show()
        #draw rectangles
        for contour in contours:
            x,y,w,h = cv2.boundingRect(contour)
            print(x,y,w,h)
            if w > 10 and h > 10:  # filter out tiny detections
                cv2.rectangle(coloured_image, (x, y), (x + w, y + h), (0, 255, 0), 10)

        gun_frame = (660,376,111,111)
        for contour in contours:
            x,y,w,h = cv2.boundingRect(contour)
            rect = (x,y,w,h)
            if (gun_frame[0] <= x <= gun_frame[0] + gun_frame[2]) and (gun_frame[1] <= y <= gun_frame[1] + gun_frame[3]):
                print(f"Enemy detected at gunpoint: {rect}")
                cv2.rectangle(coloured_image, (x, y), (x + w, y + h), (0, 0, 255), 2) 

        plt.imshow(coloured_image)
        plt.show()'''



#track_enemy_movements()    