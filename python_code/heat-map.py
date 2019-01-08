#!/usr/bin/python3.6m

import numpy as np
import cv2
import copy

def main():
    cap = cv2.VideoCapture('1.mp4')
    # cap = cv2.VideoCapture('/dev/video1')
    # pip install opencv-contrib-python
    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

    # number of frames is a variable for development purposes, you can change the for loop to a while(cap.isOpened()) instead to go through the whole video
    num_frames = 350

    first_iteration_indicator = 1
    for i in range(0, num_frames):

        # if (first_iteration_indicator == 1):
        ret, frame = cap.read()
        first_frame = copy.deepcopy(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        height, width = gray.shape[:2]
        accum_image = np.zeros((height, width), np.uint8)
        first_iteration_indicator = 0
        # else:

        # for testing purposes, show the current frame
        # cv2.imshow('frame', gray)

        color_image = im_color = cv2.applyColorMap(accum_image, cv2.COLORMAP_HOT)
        result_overlay = cv2.addWeighted(first_frame, 0.7, color_image, 0.7, 0)

        cv2.imshow('result_overlay', result_overlay)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imshow('result_overlay', result_overlay)
            break

        # apply a color map
        # COLORMAP_PINK also works well, COLORMAP_BONE is acceptable if the background is dark
    # color_image = im_color = cv2.applyColorMap(accum_image, cv2.COLORMAP_HOT)
    # for testing purposes, show the colorMap image
    # cv2.imwrite('diff-color.jpg', color_image)

    # overlay the color mapped image to the first frame
    # result_overlay = cv2.addWeighted(first_frame, 0.7, color_image, 0.7, 0)

    # save the final overlay image
    cv2.imwrite('diff-overlay.jpg', result_overlay)

    # cleanup
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()