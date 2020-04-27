# Quick Respone Code-and-Face-Recognition-for-Access-Control

## Overview
Face Recognition is a recognition technique used to recognize faces of individuals whose mathematical facial features are already stored in the database as faceprints and most of the current face recognition algorithms can achieve satisfactory level of accuracy. However, the problem arises when the database size gets very large. As the database size becomes larger, the computation required to identify a person against the database(1:n matching) increases proportionally. To deal with this problem, in this implementation, face recognition(more precisely face authentication) is paired up with QR-code scanning. This fusion of two modalities i.e QR-code and face authentication serves two purposes. First, it improves the accuracy performance of face recognition systems and second, it narrows down the 1:n matching against a database of face recogniton systems to 1:1 matching.

## How it Works
### New User Registeration
1. The system asks the user to input a email address
2. A unique-id is generated  
2. QR-code, corresponding to the generated unique-id, is sent to the input email address
3. A face capturing camera is opened and on pressing "q", facial features, along with the unique-id get stored in the database

### Face Authentication
For face authentication, the user stands in front of the capturing camera
1. QR-code is scanned positioned in front of the camera
2. The decoded id is searched in the database. If found, the feature vector(embedding vector) is fetched from the database and compared with facial features of person standing in front of the capturing device using a metric called cosine similarity. This metric score authenticates the person by manually determining a threshold value. 


The system can be interfaced with arduino for hardware control using a library named by pyserial. 

## References
https://www.jumio.com/facial-recognition-vs-facial-authentication/

https://arxiv.org/pdf/1604.02878.pdf

https://arxiv.org/pdf/1503.03832.pdf
