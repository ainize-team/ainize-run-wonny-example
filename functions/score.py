from submit import *
import os
import sys
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

####### select file or directory #########
def image_file_to_json(img_path):
    img_dir = os.path.dirname(img_path)
    img_id = os.path.basename(img_path).split('.')[0]
    return img_dir, [{'image_id': img_id}]


def image_dir_to_json(img_dir, img_type='jpg'):
    img_paths = glob.glob(os.path.join(img_dir, '*.'+img_type))
    print(img_paths)
    samples = []
    for img_path in img_paths:
        img_id = os.path.basename(img_path).split('.')[0]
        samples.append({'image_id': img_id})
    return samples

###### directory settings #######

image_source = '/workspace/images/' + sys.argv[1]

############ main #############

if __name__ == "__main__":
    print(image_source)
    if os.path.isfile(image_source):
        image_dir, samples = image_file_to_json(image_source)
    else:
        image_dir = image_source
        samples = image_dir_to_json(image_dir, img_type='jpg')

    curScore = 0
    print(image_dir)
    print (samples)
    for sample in samples :
        img_file = os.path.join(image_dir, '{}.{}'.format(sample['image_id'], 'jpg'))
        print(img_file)
        output = evaluate(img_file)
        if(output > curScore) :
            curScore = output
    print(curScore)
