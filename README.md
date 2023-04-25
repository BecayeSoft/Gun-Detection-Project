# Gun-Detection-Project

A web application for performing gun detection on images and videos. This project covers a broad range of topics such as Computer Vision, APIs, Dockers, Orchestrators, PaaS,  and more.
See the PDF files `presentation.pdf` and `report.pdf` - available only in french for now - for more details.

#### TODO:
- [ ] Upload report - FR version
- [ ] Add video support
- [ ] Add real-time detection
- [ ] Deploy Front-end to AWS Beanstalk
- [x] Deploy API to ECS
 
As all of my projects, this one has its own motivation.

## Situation
My goal was to develop my Computer Vision and MLOps skills. So, I decided to solve a security problem. The presence of guns in public places, such as parks or airports, can be dangerous if not monitored efficiently. <br>
However, monitoring such areas requires too many resources and concentration for humans. Thus, I launched this experiment to see how efficient a machine could be in performing such as a tedious task.

## Action
I went through the original YOLO paper, and after some research YOLO seemed to be a great fit, especially the version 8, which was launched by Ultralytics in January 2023. 
However, being a former web developer, I didn't stop at building the model. My goal was to create a whole system, from the front-end to the back-end, to deploying the application and ensure scalability.

### System Architecture
The following is the architecture I proposed:

<img width="646" alt="image" src="https://user-images.githubusercontent.com/87549214/234396072-c98d07ed-1bc7-4dd2-9c4f-639b2195c1ba.png">

### Back-end
The back-end is located in the folder `API`

#### API
The API is built using Flask. It receives requests, calls the YOLOv8 model and returns predictions.

#### Docker
Docker container is used to package the API, facilitating deployment and scaling.

#### Amazon ECR
Amazon ECR (Elastic Container Registry) is a container registry. Containers are hosted there so that other services, such as Amazon ECS (Elastic Container Service), can access them.

#### Amazon ECS
Amazon ECS (Elastic Container Service) is a container orchestrator. It allows for the management and deployment of Docker containers on a cluster.

#### Aws Fargate
Amazon Fargate is an infrastructure that allows us to host our ECS cluster. This service allocates the resources that the cluster needs to operate. Unlike Amazon EC2, manual infrastructure management is not required.


### Front-end
The front-end is located in the folder `frontend`

#### Web-app
HTML, CSS, JavaScript were used to build the interface and make calls to the API.

#### AWS Elastic Beanstalk
AWS Elastic Beanstalk is a PaaS (Platform as a Service) specifically designed for the deployment of web applications. It is used to host web applications. Beanstalk fully manages the infrastructure and auto-scaling. Since there is no need for extensive control over the front-end infrastructure unlike the API, Elastic Beanstack is an excellent choice.

### Desktop-App
A minimalistic GUI was built in Python to easily test the model. Find it in the folder `desktop-app`.


## Results
The interface is minimalistic. In fact, I copied it from my project [SmartEye](https://github.com/BecayeSoft/SmartEye/).

<img width="766" alt="image" src="https://user-images.githubusercontent.com/87549214/233763331-5918702c-9a12-4283-a65d-6ade62ddfbe2.png">

