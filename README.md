# LOViS

### Code for LOViS
This is the code for the paper ''LOViS: Learning Orientation and Visual Signals for  Vision and Language Navigation''. The paper is accepted by COLING 2022.

### Environment Installation
Please refer to [Env-Dropout](https://github.com/airsplay/R2R-EnvDrop) to install the Matterport3D simulators, download Room-to-room dataset and install the python environments. 

### Pre-training 
Pre-training code is in pre-train file. You can download the [pre-training weights](https://drive.google.com/drive/folders/1YOY5-Bwt8fKJg2T3e3ieKI2sZsQVY2aV?usp=share_link.  Also, please refer to [PREVALENT](https://drive.google.com/drive/folders/1tvg8Kuu5Q1wfFGIa-ha8NNqv0Nd6x-EO) to download the pre-training data.



### Run Agent

    bash run/train_agent.bash 0
   
   0 is the gpu id.

### Test Agent

    bash run/test_agent.bash 0
   

### Best Results
The following is our best val_unseen result.  [Download Weights](https://drive.google.com/drive/folders/1v8yUJ4DDgy_3cjYSi7Eu9oNrz3HOb-F4?usp=sharing)

    Env name: val_unseen, nav_error: 3.5419, oracle_error: 2.2834, steps: 5.9506, lengths: 11.4193, success_rate: 0.6692, oracle_rate: 0.7361, spl: 0.6176
