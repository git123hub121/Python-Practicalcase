import paddlehub as hub
import cv2
import os
import shutil
 
 
def get_all_path(dirpath, *suffix):
  """
  获得所有路径
 
  @param dirpath:目录
  @param *suffix: 后缀
  """
 
  path_array = []
  for r, ds, fs in os.walk(dirpath):
    for fn in fs:
      if os.path.splitext(fn)[1] in suffix:
        fname = os.path.join(r, fn)
        path_array.append(fname)
  return path_array
 
 
def paint_rect(input_img: str, output_path: str,
        labels: list, positions: list):
  """
  画出矩形
    :param input_img: 输入图片
    :param output_path: 输出图片
    :param labels: 标签
    :param positions: 坐标
  """
  img = cv2.imread(input_img)
 
  for position in positions:
    # 画矩形框, 输入参数分别为图像、左上角坐标、右下角坐标、颜色数组、粗细
    cv2.rectangle(
      img, (position['left'], position['top']),
      (position['right'], position['bottom']),
      (0, 255, 0), thickness=10
    )
 
  if 'cat' in labels:
    # 若是猫，则存到另一个地方
    shutil.move(input_img, output_path + os.sep + input_img.split('/')[-1])
    cv2.imwrite(output_path + os.sep + 'rect_%s' % input_img.split('/')[-1], img)
 
 
if __name__ == '__main__':
  source_path = './imgs/'
  target_path = './target/'
 
  # 获得所有jpg和png图片
  image_paths = get_all_path(source_path, '.jpg', '.JPG', 'png', 'PNG')
 
  # 加载模型
  yolov3 = hub.Module(name="yolov3_darknet53_coco2017")
 
  # 输入图片
  input_dict = {"image": image_paths}
 
  # 输出结果
  results = yolov3.object_detection(data=input_dict, labels=['cat'])
  for result in results:
    path = result['path']
    labels = []
    positions = []
    for target in result['data']:
      labels.append(target.get('label', ''))
      positions.append({
        'left': target.get('left', -1),
        'top': target.get('top', -1),
        'right': target.get('right', -1),
        'bottom': target.get('bottom', -1)
      })
    paint_rect(path, target_path, labels, positions)


#https://pythondict.com/python-data-analyze/python-auto-find-cats/