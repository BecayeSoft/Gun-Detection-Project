# Gun-Detection-Project

A web application for performing gun detection on images and videos. This repository covers a broad range of topics such as Computer Vision, APIs, Dockers, CDNs, etc.

#### TODO:
- [ ] Add video support
- [ ] Add real-time detection
- [ ] Deploy Front-end to AWS CloudFront
- [ ] Deploy API to ECS
 
As all of my projects, this one has its own motivation.

## Situation
My goal was to develop my Computer Vision and MLOps skills. So, I decided to solve a security problem. The presence of guns in public places, such as parks or airports, can be dangerous if not monitored efficiently. <br>
However, monitoring such areas requires too many resources and concentration for humans. Thus, I launched this experiment to see how efficient a machine could be in performing such as a tedious task.

## Action
I went through some scientific papers, and YOLO seemed to be a great fit, especially version 8, which was launched by Ultralytics in January 2023. 
However, being a former web developer, I didn't stop at the model. I created a whole system, from the front-end to the back-end, to deploying the application.

### Technologies Used:

#### Front-end
* Front-end:  HTML, CSS, JavaScript were used to build the interface and make calls to the API.
* CDN: the front-end is deployed on AWS CloudFront. A CDN (Content Delivery Network) that enable fast performances.

#### API
* API: the API is built using Flask. It receives requests, calls the YOLOv8 model and returns predictions.
* Container: a Docker container is used to package the API, facilitating deployment and scaling.
* Container Repository: the container is hosted on AWS ECR (Elastic Container Registry).


## Results
The interface is minimalistic. In fact, I copied it from my project [SmartEye](https://github.com/BecayeSoft/SmartEye/).

<img width="766" alt="image" src="https://user-images.githubusercontent.com/87549214/233763331-5918702c-9a12-4283-a65d-6ade62ddfbe2.png">

