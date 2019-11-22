# Ainize-run-wonny-example ![alt text](/images/wonny.jpeg)

This repository is about Image Quality Assessment based on [open source](https://github.com/idealo/image-quality-assessment), "NIMA: Neural Image Assessment" from Google's research. 

You can use this project when you want to evaluate your image in the scale of 1 to 10. We developed a server using Node.js so when you provide an image storage url, you can receive marks(1 - 10) for that image. 

[![Run on Ainize](https://ainize-run-web.herokuapp.com/static/images/run_on_ainize_button.png)](https://ainize-dev.web.app/redirect?git_repo=github.com/ainize-team/ainize-run-style-transfer)


## Docker build
```
docker build -t wonny .
```

## Docker run 
```
docker run -it wonny
```

## How to request using https
```
http://${host}:80/evaluate?image=${imagePath}
```
You have to pass url for image using imagePath variable.

### 1. upload image to imgur
https://imgur.com/

Upload your image and get link.  
<img src="/images/guide3.png" width="250" />  

### 2. upload image to google drive 

For convience, we open public [google drive](https://drive.google.com/drive/folders/1Ou30F1YEa0Wnh6V1gPjSwmxNmobqe_X2) for upload images. 

You can get image id from shareable link then you pass image link like below.  
<img src="/images/guide.png" width="250" />
<img src="/images/guide2.png" width="250" />
```
${imagePath} = https://drive.google.com/uc?export=view&id=${imageId}
```


## References
1. [Introducing NIMA: Neural Image Assessment](https://ai.googleblog.com/2017/12/introducing-nima-neural-image-assessment.html) Google AI Blog
2. https://github.com/idealo/image-quality-assessment