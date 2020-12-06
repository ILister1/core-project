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

[trello]: https://i.imgur.com/sSPOug4.png

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

