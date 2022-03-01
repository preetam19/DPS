from google.cloud import aiplatform

endpoint = aiplatform.Endpoint(
    endpoint_name="projects/630236181889/locations/us-central1/endpoints/4518561781601271808"
)

# A test example we'll send to our model for prediction
test_mpg = test_mpg = [1, 2, 3, 2, -2, -1, -2, -1, 0]


response = endpoint.predict([test_mpg])

print('API response: ', response)

print('Predicted MPG: ', response.predictions[0][0])