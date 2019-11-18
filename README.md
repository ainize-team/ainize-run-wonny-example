# Ainize-run-wonny-example ![alt text](/images/wonny.jpeg =50x)

This repository is about Image Quality Assessment based on "NIMA: Neural Image Assessment" from Google's research. We refer to [open source](https://github.com/idealo/image-quality-assessment). 

You can use this project when you want to evaluate your image between 1 - 10 score. We develop a server using node js so when you provide image storage url, you can receive score for that image. 


## Docker build
```
docker build -t wonny .
```

## Docker run 
Open port 80 for docker and we use port 8080 for server, so we see clearly using option p.
```
docker run -p 80:8080 -it wonny
```

## How to request using https
```
https://${host}:80/evaluate?image=${imagePath}
```
You have to pass url for image using imagePath variable.

For convience, we open public [google drive](https://drive.google.com/drive/folders/1Ou30F1YEa0Wnh6V1gPjSwmxNmobqe_X2) for upload images. 

You can get image id from shareable link then you pass image link like below.
https://drive.google.com/uc?export=view&id=${imageId}


## References
1. [Introducing NIMA: Neural Image Assessment](https://ai.googleblog.com/2017/12/introducing-nima-neural-image-assessment.html) Google AI Blog
2. https://github.com/idealo/image-quality-assessment