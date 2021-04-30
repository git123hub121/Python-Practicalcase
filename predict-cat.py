import paddlehub as hub

yolov3 = hub.Module(name="yolov3_darknet53_coco2017")

test_img_path="imgs/c1.jpg"

input_dict={"image":[test_img_path]}

results= yolov3.object_detection(data=input_dict)
for result in results:
    print(result['path'])
    print(result['data'])
#