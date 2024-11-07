# Stratus

**Authors**: Ruida Zeng, Aadarsh Jha, Ashwin Kumar, Terry Luo  
**arXiv Link**: [Cloud-Based Deep Learning: End-To-End Full-Stack Handwritten Digit Recognition](https://arxiv.org/abs/2304.13506)

**Vanderbilt University Fall 2021 Immersion Vanderbilt Project** – [Program Information](https://www.vanderbilt.edu/immersion/)  
**Professor & Faculty Mentor**: Dr. Aniruddha Gokhale, Professor of Computer Science, Vanderbilt University

<img src="https://github.com/user-attachments/assets/cd996a6b-7aca-451d-aee7-ea75b6e9d465" alt="stratus" width="400"/>

## Cloud-Based Deep Learning for Handwritten Digit Recognition

**Stratus** is a cloud-deployed, end-to-end deep learning application for real-time handwritten digit recognition. It combines cloud infrastructure and

## Cloud-Based Deep Learning for Handwritten Digit Recognition

**Stratus** is a cloud-deployed, end-to-end deep learning solution designed to recognize handwritten digits in real time. This project integrates cloud computing and distributed deep learning principles to deliver a scalable, production-grade pipeline for digit recognition. It leverages an ensemble of cloud-based tools and modern full-stack technologies to streamline real-time predictions via a web interface.

## Demo

Try the live demo at [stratus-final.ml](http://stratus-final.ml)

## Overview

Stratus is an end-to-end, full-stack application built for handwritten digit classification. Users draw a digit in the web interface, which is then sent to the cloud infrastructure where the deep learning model makes a prediction. The cloud-based backend processes and returns the result in real time.

The system combines:
- **Deep Learning** for accurate digit recognition using the MNIST dataset.
- **Cloud Computing** for distributed, scalable processing.
- **Full-Stack Architecture** with a user-friendly web interface.

## Features

- **End-to-End Machine Learning Pipeline**: From user input to model prediction, all components are integrated and productionized.
- **Distributed Architecture**: Scales to handle variable user traffic with load balancing and real-time data processing.
- **Intuitive User Interface**: A canvas for digit drawing, real-time feedback, and prediction probability graph.

## Tech Stack

- **Front-end**: HTML, JavaScript
- **Back-end**: Python Flask, Apache Kafka
- **Data Processing**: Apache Spark ML
- **Cloud Infrastructure**: Chameleon Cloud, Kubernetes, Docker
- **Orchestration & Automation**: Ansible, Vagrant
- **Database**: CouchDB
- **Web Server**: Nginx

## Architecture

The Stratus architecture comprises three main components:
1. **Cloud-Based Infrastructure**: Managed through Docker and Kubernetes across multiple VMs, ensuring scalability and robustness.
2. **Full-Stack Web Application**: A user interface to draw digits and view predictions, with Flask managing backend requests.
3. **Deep Learning Model**: A Convolutional Neural Network (CNN) trained on the MNIST dataset, deployed via Spark for distributed model inference.

## Installation and Setup

### Prerequisites

- Python 3.x
- Docker, Kubernetes, Ansible, Vagrant, Nginx, CouchDB

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ruidazeng/stratus.git
   cd stratus
   ```

2. **Set up Virtual Machines**:
   ```bash
   vagrant up
   ```

3. **Deploy services using Ansible**:
   ```bash
   ansible-playbook playbook_demo_master.yml
   ```

4. **Run the Flask server**:
   ```bash
   python3 fullstack-python/app.py
   ```

### Usage

After deployment, navigate to the live link or access the application locally on `localhost:5000`. Draw a digit on the canvas and press "Predict" to see the model's prediction along with a probability graph.

## Evaluation

The project has been rigorously tested for:
- **Model Accuracy**: Achieved 97.4% accuracy on the MNIST dataset.
- **Load Balancing**: Stress tests were conducted to determine the optimal user load for fast and reliable predictions.
- **Response Time**: System is optimized for minimal response time under various user loads.

For more details on testing and evaluation, see the [technical report](https://www.ruidazeng.com/files/Cloud-Based%20Deep%20Learning%20End-To-End%20Full-Stack%20Handwritten%20Digit%20Recognition.pdf).

## Future Directions

Potential improvements include:
- Support for multi-digit recognition.
- Enhanced model robustness and accuracy for varied input styles.
- Real-world deployment in a large-scale production environment.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributors

- [Ruida Zeng](https://github.com/ruidazeng)
- [Aadarsh Jha](https://github.com/aadarshjha)
- [Ashwin Kumar](https://github.com/ashwinkumargb)
- [Terry Luo](https://github.com/t-luo)

For questions, feel free to reach out via GitHub Issues or email.
