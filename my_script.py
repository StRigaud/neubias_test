from skimage.io import imread
from skimage.filters import threshold_otsu
from skimage.measure import label


def otsu_labeling(image):
    image = image > threshold_otsu(image)
    return label(image)


