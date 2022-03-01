from google.cloud import aiplatform

# Create a model resource from public model assets
model = aiplatform.Model.upload(
    display_name="mpg-imported",
    artifact_uri="gs://neat-domain-341912-bucket_custom/model",
    serving_container_image_uri="gcr.io/cloud-aiplatform/prediction/sklearn-cpu.1-0:latest"
)



# Deploy the above model to an endpoint
endpoint = model.deploy(
    machine_type="n1-standard-4"
)