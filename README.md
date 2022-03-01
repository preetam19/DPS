# DPS Challenge

My solution cosists of 2 models that were deployed using Vertex AI. The first model being the model that have been used in the custom model with Linear regression. The custom model uses the Random forest regressor model. 

First model is under the directory mpg, while the custom model is under mpg_custom. 


-> Training job in the container

To put the training code in a container we create 2 docker files for two respective training models (Linear regression, Random Forest Regressor). There are 2 training files (train.py and train_custom.py) files that are later deployed and pushed to the Google container registry. 


Model 1  image: https://console.cloud.google.com/gcr/images/neat-domain-341912/global/mpg@sha256:ad50a5ba62371a2e09e8888c9dc7a09811c15097442d2e3424bd0928a87da6d4/details?project=neat-domain-341912


Model 2 image: https://console.cloud.google.com/gcr/images/neat-domain-341912/global/mpg@sha256:ad50a5ba62371a2e09e8888c9dc7a09811c15097442d2e3424bd0928a87da6d4/details?project=neat-domain-341912


We then proceed to train the model through the Training section in the vertex section of our Cloud console. In the container settings step, we pick the respective container registry for both model 1 and 2 respectively. 

-> Now we create the endpoints for our two models. We use these endpoints to get the predictions using the Vertex API. We create deploy.py and deploy_custom.py 
 Model1 -> artifact_uri = 
            serving_containder_image_uri = 
            
            
Model2- >  artifact_uri = 
            serving_containder_image_uri = 
            
            
We then have two different models as shown below





Using the files predict_py and predict_custom.py we acquire following results. 



Since our model2 has been custom trained the model expects the test_mpg to have 8 elements as the given test_mpg also consists of mpg value which is the targe value of the model and therefore is elinated. 
            
            
            
            
            
            
            
            
