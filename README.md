# celebrity-face-detection
Note : Please read comments in python files and do the necessary changes accordingly

--------------------------------------------------------------------------------------------------------
Data Collection

Collect dataset by using crawler 
File to be executed : Data Collection/Crawler.py

Before exceuting create a csv file with names of celebrity whose data set wants to be created:


--------------------------------------------------------------------------------------------------------
Data Preprocessing:
Cleaning data by extracting and cropping faces from new created dataset above using Haar Cascade
File to be executed: Data Collection/face_crop.py




------------------------------------------------------------------------------------------------------------------
Data spliting:

Spliting dataset into Train/Test as required

File to be executed: Data Collection/split.py

-------------------------------------------------------------------------------------------------------------------
Feature and encoding Extration from Faces 

1>Facenet and MTCNN

Pre Requisite:- for Facenet first download 'facenet_keras_weights' from web.

For feature extraction:
File to be executed: Facenet/train_v2.py

After execution encodings.pkl (pickle) file will be created

For Face Detection:
By using above encoding file face will be labelled.

File to be executed: Facenet/detect_Facenet.py

==================================================================================================================

2>VGG16 and Haar cascades


For feature extraction:

File to be executed: VGG16/model_2.py

After execution trained model file(.h5) will be created.

For Face Detection:
By using above model.h5 file face will be labelled.

File to be executed: Vgg16/detect_Vgg.py


----------------------------------------------------------------------------------------------------------------------
Note : Please read comments in python files and do the necessary changes accordingly


