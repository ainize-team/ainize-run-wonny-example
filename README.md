# Ainize-run-wonny-example ![alt text](/images/wonny.jpeg)

This repository provides an API server, called Wonny server, that evaluates images based on an aesthetic and technical image quality model. The model used in the server is from [Image Quality Assessment](https://github.com/idealo/image-quality-assessment), which is an implementation of Google's research paper "NIMA: Neural Image Assessment". 

The evaluation using Wonny server is done in the following steps:
1. User publishes an image file
2. User queries Wonny server with the image url
3. Wonny server returns a quality score of the image in the scale of 1 to 10

Note that the implementation was done using Node.js.

# How to deploy

Wonny server is dockerized, so it can be built and run using docker commands.

## Docker build
```
docker build -t wonny .
```

## Docker run 
```
docker run -it wonny
```

The docker image can be deployed using any docker-based deploy platform (e.g. Ainize Run).

# How to query

## How to publish an image file

The image to be evaluated needs to be published first. You can refer to the two following examples of how to publish image files: 

### Imgur

https://imgur.com/

Upload your image and get link.  
<img src="/images/imgur.png" width="250" />  

### Google Drive 

For your convience, we share a [Google Drive folder](https://drive.google.com/drive/folders/1Ou30F1YEa0Wnh6V1gPjSwmxNmobqe_X2). 

Once uploaded an image file, you can get a sharable link to the uploaded file from the image id provided by Google Drive:

<img src="/images/gdrive.png" width="250" />
<img src="/images/gdrive2.png" width="250" />

```
https://drive.google.com/uc?export=view&id=${imageId}
```

## How to query the server

Finally, you can pass the image url to Wonny server to get the evaluation result:
```
http://${host}:80/evaluate?image=${imageUrl}
```

## References
* [Introducing NIMA: Neural Image Assessment](https://ai.googleblog.com/2017/12/introducing-nima-neural-image-assessment.html) Google AI Blog
* https://github.com/idealo/image-quality-assessment
