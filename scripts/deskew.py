import os
import cv2
import numpy as np

def rotate_image(image, angle):
    (h, w) = image.shape[: 2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    corrected = cv2.warpAffine(image, M, (w, h), flags = cv2.INTER_CUBIC, borderMode = cv2.BORDER_REPLICATE)
    return corrected

def determine_score(arr):
    histogram = np.sum(arr, axis = 2, dtype = float)
    score = np.sum((histogram[..., 1 :] - histogram[..., : -1]) ** 2, axis = 1, dtype = float)
    return score

def correct_skew(image, delta = 0.1, limit = 20):
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    angles = np.arange(-limit, limit + delta, delta)
    img_stack = np.stack([rotate_image(thresh, angle) for angle in angles], axis = 0)
    scores = determine_score(img_stack)
    best_angle = angles[np.argmax(scores)]
    corrected = rotate_image(image, best_angle)
    return best_angle, corrected

def apply_function_to_images(input_dir, function):
    # Create the output directory
    output_dir = input_dir + "_deskewed"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over all files in the input directory
    for filename in os.listdir(input_dir):
        # Check if the file is an image
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Open the image
            image_path = os.path.join(input_dir, filename)
            image = cv2.imread(image_path, 0)

            # Apply the function to the image
            output_image = function(image)

            # Save the output image to the new output directory
            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, output_image)


# img_path = 'C:/Users/harmera/Dropbox/data/label_ocr/runs/detect/predict5/crops/typed_label/NZAC04268297_label_jpg.rf.38438d2266968be2bb7b47381f8e60a7.jpg'
# img = cv2.imread(img_path, 0)
# angle, corrected = correct_skew(img, limit = 20)

# cv2.imshow('Original Image', img)
# cv2.imshow('Deskewed Image', corrected)
# cv2.destroyAllWindows()

input_dir = 'C:/Users/harmera/Dropbox/data/label_ocr/runs/detect/predict5/crops/typed_label'
apply_function_to_images(input_dir, correct_skew)
