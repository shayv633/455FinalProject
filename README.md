# 455 Final Project

For this project, Cody Heale and Shay Vainer decided to use Machine Learning to identify faces in photographs and "deep-fry" them in order to anonymize the individuals in the photographs. This project idea came about originally as a silly idea to learn how to create the "deep-fry" filters that are often used in memes such as this one: https://www.reddit.com/r/deepfriedsurrealmemes/comments/uxijue/four_fingers_fried/

However as we did further research, we found that this filtering could be used as a fun way of anonymizing people in photographs. The process of creating a "deep-fried" meme involves passing the image through multiple filters to the point of unrecognizablity. It originally came about from images that had been saved and reposted on the internet over and over again, eventually leading to such terrible artifacting that the original image was practically unrecognizable.

For the facial recognition portion of the project, we did a lot of research about what would be best for our project before eventually settling on OpenCV and their open source haar cascades. We sourced them from this Git repo: https://github.com/opencv/opencv/blob/master/data/haarcascades

Thanks to their pretrained haar cascades, we were able to focus on creating the image filters and how best to only anonymize the faces. We ended up using a mask and cutting out circles for each face detected by the haar cascade. We could then copy and "deep-fry" the entire image, and using the mask remove all of the image expect for the faces. Then we removed everything but the background in the original image and combined both images together to get our final image.

To see our final project video, download it from this link: https://drive.google.com/file/d/1cNE5OxjUxcIT2a1rvff5MfFq_slxTQef/view?usp=sharing
