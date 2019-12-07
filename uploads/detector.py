#!/usr/bin/env python
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import json
import os
files = []

prediction_key = "c53eb590ea864950a841f02a1cc684f6"
ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com/"
#base_image_url = "D:\Study Files\Hackathons\MLH Hackathon\solid.jpg"
#base_image_url = "D:\Study Files\Hackathons\MLH Hackathon\ddhujia.jpg"
#base_image_url = "D:\Study Files\Hackathons\MLH Hackathon\ewew.jpg"
#base_image_url = "D:\Study Files\Hackathons\MLH Hackathon\colgate.jpg"
hey = "321a77e3-2bfc-4b25-ab2a-fc4e5d5a9c20"
publish_iteration_name = "Iteration2"
# Now there is a trained endpoint that can be used to make a prediction
predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

for i in os.listdir(r"C:\wamp64\www\new\uploads"):
    if i.endswith('.jpg'):
        base_image_url=i
        with open(base_image_url, "rb") as image_contents:
            results = predictor.classify_image(
                hey, publish_iteration_name, image_contents.read())

            # Display the results.
            for prediction in results.predictions:
                print("\t" + prediction.tag_name +
                    ": {0:.2f}%".format(prediction.probability * 100))
                break
        data = []
        t = prediction.tag_name
        data.append({
            'name': t,
            'price': "20rs"
            })
        with open('data.json', 'w+') as outfile:
            json.dump(data, outfile)

    # end with
    files = ['data.json']
