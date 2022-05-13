from django.shortcuts import render
import json
from django.core.serializers import serialize
# Create your views here.
from django.shortcuts import render
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# Create your views here.
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializer import UploadSerializer
import pickle
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import numpy as np 
from sklearn import preprocessing 
from keras.models import load_model
from keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing import image
from PIL import Image
import cv2
import pytesseract
from pdf2image import convert_from_path
from omni.models import PedigreeNode,Pigeon,Pedigree, StatutPedigree
from omni.serializer import UploadSerializer, PedigreeSerializer, statutSerializer
# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
	serializer_class = UploadSerializer
	
	def list(self, request):
		return Response("GET SERVICE")
	
	def create(self, request):
		#model =  load_model("C:/Users/pc/projects/django-web-app/merchex/nvproject/best_model.h5")
		model =  load_model("best_model.h5")
		global file_uploaded 
		file_uploaded = request.FILES.get('file_uploaded')
		img = Image.open(file_uploaded)
		img = img.convert("RGB")
		img = img.resize((256,256))
		i = img_to_array(img)
		i = preprocess_input(i)
		input_arr = np.array([i])
		result = np.argmax(model.predict(input_arr))
		if result == 0:
			st = StatutPedigree(statut_id='2')
			st.save()
			pd = Pedigree(generation=0,statut=st)
			pd.save()
			pn=PedigreeNode(nodeKey=1,noeudParent=0,isRoot=True,pedigree=pd)
			pn.save()
			pg = Pigeon(pigeonName="",numeroSerie="",description=" ",pedigree=pd,pedigreenode=pn)
			pg.save()
			serializer = statutSerializer(instance= st)
		else :
			pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
			img = Image.open(file_uploaded).convert('L')
			img.save('output_file.jpg')
			img=cv2.imread('output_file.jpg',cv2.IMREAD_GRAYSCALE)
			img2 = Image.open('output_file.jpg')
			_, threshold = cv2.threshold(img, 145, 255, cv2.THRESH_BINARY)
			contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			contenue={}
			coordonée={} 
			font = cv2.FONT_HERSHEY_SIMPLEX
			# configurations
			config = ('-l eng --oem 1 --psm 3')
			rectangle=0
			for cnt in contours:
				approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
				x = approx.ravel()[0]
				y = approx.ravel()[1]
				if len(approx) == 4:
						if -4<=(approx[0][0][0] - approx[1][0][0])<=4 and (abs(approx[0][0][1] - approx[1][0][1])>10) : 
							width = img2.width 
							height = img2.height
							# la formulaire pour minimiser les rectangle qui existe dans les borde 
							seuil= (width+height)*10/100
							
							if ((approx[0][0][0] + approx[0][0][1])> seuil) and (abs(approx[0][0][0]-approx[2][0][0])>20) :
								left = approx[0][0][0]
								top = approx[0][0][1]
								width = approx[2][0][0] - approx[0][0][0]
								height = approx[1][0][1] - approx[0][0][1]
								coordonée[rectangle]=[left,top,width,height]
								box = (left, top, left+width, top+height)
								
								area = img2.crop(box)
								text = pytesseract.image_to_string(area)
								text = text.split('\n')
								z = len(text)
								#print(len(text))
								contenue[rectangle]= [text[0]]
								for i in range(z-1):
									contenue[rectangle].append(text[i+1])
								rectangle= rectangle+1
			for i in range(len(coordonée)):
				  # Trouver le min
					min = i
					for j in range(i+1, len(coordonée)):
						if coordonée[min][0] > coordonée[j][0]:
							min = j
					tmp = coordonée[i]
					coordonée[i] = coordonée[min]
					coordonée[min] = tmp
					tmp2 = contenue[i]
					contenue[i] = contenue[min]
					contenue[min]=tmp2
			i=0
			while(i!=len(coordonée)):
				min_x =i
				for j in range(i+1, len(coordonée)):
					if abs(coordonée[min_x][0]-coordonée[j][0])<10:
						min_x=j
					else:
						break
				if j-i>1:
					for k in range(i,j):
						min = k
						for l in range(k+1,j):
							if coordonée[min][1] > coordonée[l][1]:
								min = l
						tmp = coordonée[k]
						coordonée[k] = coordonée[min]
						coordonée[min] = tmp
						tmp2 = contenue[k]
						contenue[k] = contenue[min]
						contenue[min]=tmp2
				i=i+1
			
			st = StatutPedigree(statut_id='1')
			st.save()
			if rectangle==1:
				pd = Pedigree(generation=0,statut=st)
				pd.save()
			elif 1<rectangle<=3:
				pd = Pedigree(generation=1,statut=st)
				pd.save()
			elif 3<rectangle<=7:
				pd = Pedigree(generation=2,statut=st)
				pd.save()
			elif 7<rectangle<=15:
				pd =Pedigree(generation=3,statut=st)
				pd.save()
			else :
				pd =Pedigree(generation=4,statut=st)
				pd.save()
			for i in range(rectangle):
				x,y,z="","",""
				for j in range(len(contenue[i])):
					if j==0:
						x=contenue[i][0]
					elif j==1:
						y = contenue[i][1]
					else:
						z = z+contenue[i][j]
				if i==0:
					pn=PedigreeNode(nodeKey=1,noeudParent=0,isRoot=True,pedigree=pd)
					pn.save()
					pg = Pigeon(pigeonName=y,numeroSerie=x,description=z,pedigree=pd,pedigreenode=pn)
					pg.save()
				else:
					pn=PedigreeNode(nodeKey=i+1,noeudParent=int((i+1)/2),pedigree=pd)
					pn.save()
					pg = Pigeon(pigeonName=y,numeroSerie=x,description=z,pedigree=pd,pedigreenode=pn)
					pg.save()
			serializer = statutSerializer(instance= st)
		return Response(serializer.data)
		