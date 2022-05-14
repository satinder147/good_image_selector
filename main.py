import os
import shutil
import argparse
import subprocess
from collections import deque

import cv2

KEY_MAPPING = {'left': 81, 'right': 83, 'select_image': ord('a'), 'deselect_image': ord('d'),
               'exit': ord('q')}


def process(args):
    # Buffer of recently selected images
    recently_select_images = deque()
    src, des = args.src, args.dst
    if not os.path.exists(src):
        print("source folder does not exist")
        return
    dirs = sorted(os.listdir(src))
    print("Total {} images in source folder".format(len(dirs)))
    # Find if we are resuming the task.
    last_processed_idx = -1
    if not os.path.exists(des):
        os.makedirs(des)
    else:
        already_processed = sorted(os.listdir(des))
        if len(already_processed) == 0:
            last_processed_idx = -1
        else:
            last_processed_idx = dirs.index(already_processed[-1])

    print("Already processed {} images".format(last_processed_idx + 1))
    display_height = int(0.75 * args.display_height)
    # Filter required extensions
    dirs = [i for i in dirs if i.find(args.ext) != -1]
    remaining_images = dirs[last_processed_idx + 1:]
    i = 0
    num_images_back = args.buffer_size
    max_image = i
    while i < len(remaining_images):
        img_path = remaining_images[i]
        path = os.path.join(src, img_path)
        img = cv2.imread(path)
        if img is None:
            i = i + 1
            continue
        h, w = img.shape[:2]
        aspect = w/h
        new_width, new_height = int(aspect * display_height), display_height
        img = cv2.resize(img, (new_width, new_height))
        if path in recently_select_images:
            cv2.rectangle(img, (0, 0), (400, 50), (0, 255, 0), -1)
        else:
            cv2.rectangle(img, (0, 0), (400, 50), (0, 0, 255), -1)
        cv2.putText(img, str(i) + '/' + str(len(remaining_images)),
                    (120, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
        cv2.imshow('img', img)
        key = cv2.waitKey(0)
        if key == KEY_MAPPING['select_image']:
            recently_select_images.append(path)
            i = i + 1
            
        elif key == KEY_MAPPING['deselect_image']:
            try:
                recently_select_images.remove(path)
                i = i + 1
            except ValueError:
                print("image not marked for copy")
            
        elif key == KEY_MAPPING['left']:
            i = max(max(i - 1, 0), max_image - num_images_back)
        elif key == KEY_MAPPING['right']:
            i = i + 1
        elif key == KEY_MAPPING['exit']:
            break
        
        max_image = max(i, max_image)
        if len(recently_select_images) > num_images_back:
            image_to_copy = recently_select_images[0]
            recently_select_images.popleft()
            shutil.copy(image_to_copy, os.path.join(des, image_to_copy.split('/')[-1]))

    # Copy all pending.
    while len(recently_select_images):
        image_to_copy = recently_select_images[0]
        recently_select_images.popleft()
        shutil.copy(image_to_copy, os.path.join(des, image_to_copy.split('/')[-1]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', required=True, type=str, help="src path")
    parser.add_argument('--dst', required=True, type=str, help="destination path")
    parser.add_argument('--buffer_size', type=int, default=10, help="buffer of images,"
                                                                    " which is kept before"
                                                                    " copying the images. "
                                                                    "Look at the repository "
                                                                    "ReadMe to understand")
    parser.add_argument('--ext', default=['JPG'], help="image extension to copy")
    parser.add_argument('--display_height', type=int, default=1080, help="in pixels, "
                                                                         "while maintainng aspect"
                                                                         "ratio, scale height to 75"
                                                                         " percent")
    args = parser.parse_args()
    process(args)


