import pandas as pd
import numpy as np
import streamlit as st
import requests
import io
from PIL import Image
from PIL import ImageDraw


subscription_key = '84b059f0bedd4a9fac76fc104fad52c7'
assert subscription_key
face_api_url = 'https://20210117.cognitiveservices.azure.com/face/v1.0/detect'


st.title('顔認識アプリ')

uploaded_file = st.file_uploader('choose an image ...', type='jpg')
if uploaded_file is not None:
    img = Image.open(uploaded_file)

    with io.BytesIO() as output:
        img.save(output, format='JPEG')
        binary_img = output.getvalue()

    headers = {'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': subscription_key}
    params = {'returnFaceId': 'true',
              'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion'}

    res = requests.post(face_api_url, params=params,
                        headers=headers, data=binary_img)

    results = res.json()
    for result in results:
        rect = result['faceRectangle']
        at = result['faceAttributes']
        ag = at['age']

        draw = ImageDraw.Draw(img)
        draw.rectangle([(rect['left'], rect['top']), (rect['left']+rect['width'], rect['top']+rect['height'])],
                       fill=None, outline='green', width=5)

    st.image(img, caption='Uploaded Image', use_column_width=True)

#  実行の方法：　streamlit run facedetect.py

#  GitHubへのload
#  cd: streamlit_test (同期するdir )
#  git init  (local に.git という管理ツール)
#  git remote and origin https://github.com/Iamkanshin/face_detect-streamlit.git  　（同期するremote)
#  git add .  (local)
#  git commit -m'1st commit'
#  git push origin master  （remoteにpush)
