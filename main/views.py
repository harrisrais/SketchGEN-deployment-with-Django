import os
import cv2
import torch
import numpy as np
from . import Generator
import matplotlib.pyplot as plt

from django.conf import settings
from django.shortcuts import render


model_500_path = os.path.join(
            settings.BASE_DIR, "Model", 'p2p_501.pt'
        )

# model_451_path = os.path.join(
#             settings.BASE_DIR, "Model", 'p2p_451.pt'
#         )

# output_path_451 = os.path.join(
#             settings.BASE_DIR, "Main", 'static','output','pred_451.jpg'
#         )

output_path_500 = os.path.join(
            settings.BASE_DIR, "Main", 'static','output','pred_500.jpg'
        )
# Create your views here.
def index(request):
    return render(request,'index.html') 

def sketch(request):
    if request.method == "POST":
        input_img = request.FILES.get("portrait")
        img_content = input_img.read()

        with open('img.jpg', "wb") as file:
            file.write(img_content)
        
        img = cv2.imread('img.jpg')
        img = cv2.resize(img,(256,256))
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        img = np.transpose(img, (2, 0, 1))/255.0
        img = np.expand_dims(img, axis=0)
        img = torch.tensor(img,dtype=torch.float32)


        #check_451 = torch.load(model_451_path,map_location='cpu')
        check_500 = torch.load(model_500_path,map_location='cpu')
        
        gen = Generator.Generator().to('cpu')
        # gen.load_state_dict(check_451['gen_state_dict'])

        # gen.eval()
        # with torch.no_grad():
        #    pred_451 = gen(img)

        gen.load_state_dict(check_500['gen_state_dict'])

        gen.eval()
        with torch.no_grad():
           pred_500 = gen(img)

        # pred_451 = np.array(pred_451.detach())
        # pred_451 = pred_451[0].transpose(1, 2, 0)
        # pred_451 = np.clip(pred_451, 0.0, 1.0)

        pred_500 = np.array(pred_500.detach())
        pred_500 = pred_500[0].transpose(1, 2, 0)
        pred_500 = np.clip(pred_500, 0.0, 1.0)
        
        #plt.imsave(output_path_451, pred_451)
        plt.imsave(output_path_500, pred_500)
        return render(request,'sketch.html')
         
        
    return render(request,'index.html')