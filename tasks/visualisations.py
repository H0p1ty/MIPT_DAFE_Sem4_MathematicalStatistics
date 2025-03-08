import os
import matplotlib.pyplot as plt
import cv2

plt.rcParams['figure.figsize'] = (10.0, 8.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

IMG_DIRECTORY = "..\\img"

def get_img_file_path(task_name: str, index: str) -> str:
    return os.path.join(IMG_DIRECTORY, task_name + "_" + str(index) + ".jpg")

def get_task_imgs(task_name: str) -> list[str]:
    index = 1
    file_path = get_img_file_path(task_name, index)
    task_pictures = []
    while os.path.isfile(file_path):
        task_pictures.append(file_path)
        index += 1
        file_path = get_img_file_path(task_name, index)
    return task_pictures

def show_task(task_name: str) -> None:
    task_imgs = get_task_imgs(task_name)
    for img_path in task_imgs:
        img = cv2.imread(img_path, 0)
        plt.figure()
        plt.imshow(img)
        plt.axis('off')

    plt.show()