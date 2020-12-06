# QA Practical Project

**Story Prompt Generator App** _By Isaac Lister_

## Resources

Website: http://35.246.80.16 (subject to GCP)<space><space> \
Trello: https://trello.com/b/5ElPMT3w/qa-practical-project <space><space> \
Risk Assessment: https://docs.google.com/spreadsheets/d/1kQLrGaM1gW0HIWIjLm2u13QtCvqEP9KuL1jlGq1TjD0/edit?usp=sharing

## Contents

* Brief
    * [Project Brief](#project-brief)
* Designs
    * [Basic Designs](#basic-designs)
* [Risk Assessment](#risk-assessment)
* [CI Pipeline](#ci-pipeline)
* [Back End](#back-end)
* [Front End](#front-end)
* [Deployment Log](#deployment-log)
* [Known Issues](#known-issues)
* [Future Improvements](#future-improvements)
* [Unit Testing](#unit-testing)
* [Branching](#branching)

## Brief
### Project Brief

The simple brief of this project was to create an application with four discrete services, communicating on ports 5000:5003.
The focus of the brief was on the deployment side. Agreed practices and tools as follows needed implementation in order to achieve a pass mark for the project:

**Kanban Board: Trello**  \
Trello was used as a Kanban board for this project. It allows for 'cards' containing user stories and the product backlog, in addition to basic risks and issues assessment. Cards can be colour coded to aggregate their importance by story points or to demarcate the position of the task in the MOSCOW prioritisation.

![trello][trello]


**Version Control: Git VCS**  \
Git VCS was used for version control of this project. It permits a push/pull relationship between virtual machine and repository for portability; allows branching for rolling updates, and can be polled by Jenkins build triggers via a webhook. This ensures that changes to the code are updated on the live application as quickly as possible.

**CI Server: Jenkins**  \
Jenkins was used as a CI Server for this project. Jenkins creates project builds from a multi-stage pipeline script, and checks for updates to the source code in the Git repository. Within the pipeline, Jenkins also runs unit tests using pytest, and builds and deploys the project using Docker Compose and Docker Stack.

**Configuration Management: Ansible**  \
Ansible was used as a configuration management tool for this project. Ansible uses YAML files known as playbooks to install containerisation tools such as Docker and configure the virtual machines it subsequently deploys in the stack as part of a Docker Swarm. The Swarm roles are defined in Ansible and are configured using Ansible roles and hostvars. Hostvars allow us to access variables defined for any host in the play, for greater configuration customisation. I have chosen to use Ansible because it automates and simplifies repetitive operations, and has a simple and effective architecture.

**Cloud Server: Google Cloud Platform**  \
Google Cloud Platform (GCP) was used as a Cloud Server for this project. GCP is a competitively priced cloud host allowing live migration of virtual machines with state of the art security. GCP VMs and SQL instances are reliable and highly scalable, making them a perfect foil for a containerised web application deployed in a CI pipeline.

**Containerisation: Docker**  \
Docker was used as a containerisation tool for this project. As Docker containers encapsulate everything an application needs to run, it enables much greater portability- as any host with Docker installed can run a Docker container, meaning applications can be shuttled between machines seamlessly. Dockerfiles also allow Gunicorn WSGI servers to run in each container, handling the load across each individual service.

**Orchestration Tool: Docker Swarm**  \
Deploying a Stack in a Docker Swarm allows for greater availability and efficiency, using 'worker' machines as nodes to handle resources. Docker Compose YAML files ensure that image builds are consistent with the containers they run in.

**Reverse Proxy: NGINX**  \
NGINX reverse proxies perform load balancing. This assists with the distribution of requests across backend servers (such as within the worker machines of a Swarm. If one server goes down, NGINX will reroute requests to a different server in accordance with the routing policy. Serving the application to the HTTP port 80 of an NGINX machine means that all other ports can be closed on other virtual machines in the Swarm, increasing security.

## Designs
### Basic Designs

Here are some basic designs and diagrams underpinning the various aspects of this project.

**Entity Relationship Diagram**

The entity relationship diagram (ERD) is a simple one for this project. As it is just designed to persist generated stories and scenes in an SQL database, we require one simple table with a primary key and no other relationships, as follows:

![erd][erd]

The primary key is the ID of each story generated by the application, which auto increments with each refresh.
Scene and Story are generated by services (2,3) and (4) respectively, and are persisted in the database as strings. One potential limitation would be the 255 character limit on the Story, but this is permissible within the scope of this project. As this design is so simple, it was implemented in exactly this way in the project, so a revision of diagram was not needed.

**High Level Architecture Diagram**

Initially, I imagined the architecture of the project to simply be four containers, one for each service, with Service 1 exposed on port 5000 for inbound connections and making HTTP requests to ports 5001->5003 for each of the other three services respectively:

![initial][initial]

Ultimately, I realised that this diagram does not instruct the presence of the NGINX reverse proxy on its own machine, running in a container outside the Ansible configured Docker Swarm, so the final diagram reflects this:

![final][final]

## Risk Assessment

Here is a screenshot of the risk assessment performed before work on the project began. It can be seen in full at the link provided in the Resources section, and has been revisited at a later date to report on what mitigation has been taken to the intolerable risks to the project. Not all mitigation was possible, as it would require development of the application beyond the scope of this brief, but most risks have been mitigated.

![risk][risk]

## CI Pipeline

Here is my CI Pipeline for this project:

![cipipe][cipipe]

The only part of my pipeline that has not been explained is the Artifact Repository. For this I have chosen to use Dockerhub. Although we have been taught Nexus, Dockerhub uses a familiar collaboration model to GitHub, and as I am obviously used to GitHub, the method of pushing and pulling images from a DockerHub image repository makes more sense. The Docker Hub registry is less consistent than Nexus, but it is sufficient for this project.

## Back End

The back end of the project is driven by a Jenkins pipeline script. The Jenkinsfile itself executes shell(.sh) scripts from my project's 'scripts' directory to run Ansible, pytest, and use Docker to build the images, Docker Compose to push them to the dockerhub image repository, and Docker Swarm to deploy a Docker Stack.

![jenkinspipe][jenkinspipe]

## Front End

Here is a front-end view of my application. It is a simple pythonic HTML based web application, which generates new data every time the web page is refreshed and another HTTP request is made. As the focus of this project is the deployment side, the application side is simple, and so is its front-end GUI:

![frontend][frontend]

## Deployment Log

**02/12/2020**  

where n = service number:

Wrote a Dockerfile to build image for service (n).
wrote build_service(n).sh to execute build commands
wrote teardown_service(n).sh to execute teardown if image requires.
Added Gunicorn entrypoint to service (n).

**03/12/2020**  
Successfully got all four service containers running on a network with Docker.
Application is functional.
Moved on to Docker Compose.

Successfully built all containers and images on Docker Compose.
Created systemd service configuration file to obscure environment variables
These can be called from docker-compose.yaml
Did not work - Docker Compose cannot read exported variables as sudo.
DB_URI and SECRET_KEY presently exposed.


**04/12/2020**  
Moved on to Docker Swarm.

Initialised swarm.
Added 2 replicas to each service (makes it more likely the app stays up during an update) before deploying stack.
Stack deployed.

Moved on to Jenkinsfile.
Wrote Jenkinsfile with Test, Build, Push and Deploy scripts called in the pipeline.
Encountered issue of not having set up database-in-memory to Test.

**05/12/2020**  

Created Ansible playbook and Docker/Swarm roles.
Added an Ansible configuration stage to be performed prior to testing in the pipeline.

Jenkins uses the pipeline script Jenkinsfile to successfully deploy the project, will SSH into Swarm-manager and git pull to get latest version before deploying stack.
Added GitSCM webhook to Jenkins and configured in GitHub.
Set up development branch 'dev-branch' using Git to implement the second implementation of the project.

## Known Issues

The main known issue with this project is that the DATABASE_URI and SECRET_KEY are exposed in the docker-compose.yaml. This is incredibly bad practice and the only reason it persists in this project is that I am unsure how to persist environment variables in Jenkins- I have put both DATABASE_URI and SECRET_KEY into the Environment Variables section of Manage Jenkins->Configure System, but if docker-compose.yaml contains DATABASE_URI: DATABASE_URI (instead of the actual URI) etc, then the pipeline script fails to execute, even with the environment variables exported in Jenkins. This is unacceptable, and needs fixing.

The application sometimes goes down briefly during a rolling update. Or, at least, throws a 500 Internal Server Error. It is often fixed by the next refresh. Initially I was SSHing into my NGINX machine to take down and re-deploy the NGINX container. Removing this aspect of the deploy script hasn't solved the problem, so I must need more replicas declared in docker-compose.yaml, as replicas allow the application to remain in its current state whilst changes are made in the back end.

## Future Improvements

Obscure URI in docker-compose.yaml, make application secure  \
Increase number of replicas such that the application always stays live.  \
Implement login functionality and the capacity to save stories to the database exclusive to a user account.  \
Implement a form such that the user can suggest themes and settings which can be computationally processed into stories.  \

## Unit Testing

## Branching


## Authors
Isaac Lister

[trello]: https://i.imgur.com/sSPOug4.png
[erd]: https://i.imgur.com/Jo2H4Qy.png
[risk]: https://i.imgur.com/UUHwLmm.png
[initial]: https://i.imgur.com/AUspyjS.png
[final]: https://i.imgur.com/DI3MXDv.png
[cipipe]: https://i.imgur.com/Tt95F2f.png
[frontend]: https://i.imgur.com/yMYJ2f2.png
[jenkinspipe]: https://i.imgur.com/7u7GNeG.png
