import requests
import json

BASE_URL = "http://localhost:5000"
PUT_URL= f"{BASE_URL}/posts/1"
POSTS_URL = f"{BASE_URL}/posts"
DELETE_URL = f"{BASE_URL}/posts/3"
PUT_POST_DATA = {
    "id": 1,
    "title": "Updated Post Title",
    "body": "This is the updated content.",
    "userId": 1
}

DATA_POST = {
    "title": "My New Post",
    "body": "This is the content of my new post.",
    "userId": 1
}

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    # print(type(response.text))
    # print(json.loads(response.text))
    # print(response.json())
    assert isinstance(response.json(), list)

def test_get_post_by_id():
    post_id = 1
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert int(response.json().get('id')) == post_id

def test_get_nonexistent_post():
    post_id = 9999
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 404


#---------------------------------------------------------------
#----------------------GET POSTS BY ID--------------------------
#---------------------------------------------------------------


def test_status_code_is_200_GET_post_by_id():
    """Test to check if the response status code is 200."""
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200, "Status code is not 200"


def test_post_id_matches_requested_id():
    """Test to check if the post ID matches the requested ID."""
    response = requests.get(f"{BASE_URL}/posts/1")
    json_data = response.json()
    assert json_data['id'] == 1, "Post ID does not match the requested ID"


def test_post_by_id_title_is_not_empty():
    """Test to check if the post title is not empty."""
    response = requests.get(f"{BASE_URL}/posts/1")
    json_data = response.json()
    assert isinstance(json_data['title'], str) and json_data['title'], "Post title is empty"


def test_post_id_is_number_and_not_empty():
    """Test to check if the post ID is a number and not empty."""
    response = requests.get(f"{BASE_URL}/posts/1")
    json_data = response.json()
    assert isinstance(json_data['id'], int) and json_data['id'] is not None, "Post ID is not a valid number"


def test_post_by_id_body_is_not_empty():
    """Test to check if the post body is not empty."""
    response = requests.get(f"{BASE_URL}/posts/1")
    json_data = response.json()
    assert isinstance(json_data['body'], str) and json_data['body'], "Post body is empty"


def test_body_by_id_contains_expected_fields():
    """Test to check if the body contains the expected fields."""
    response = requests.get(f"{BASE_URL}/posts/1")
    json_data = response.json()
    expected_keys = ["userId", "id", "title", "body"]
    for key in expected_keys:
        assert key in json_data, f"Missing key: {key} in response body"




#---------------------------------------------------------------
#----------------------PUT POSTS BY ID--------------------------
#---------------------------------------------------------------

def test_successful_put_post_request():
    """Test to check if the server responds with HTTP status code 200, 201, or 204."""
    response = requests.put(PUT_URL, json=PUT_POST_DATA)
    assert response.status_code in [200, 201, 204], "PUT request failed"

# #NOTE: This test will fail because the server is slow
# def test_put_post_response_time_is_less_than_400ms():
#     """Test to check if the PUT response time is less than 400ms."""
#     response = requests.put(PUT_URL, json=PUT_POST_DATA)
#     assert response.elapsed.total_seconds() < 0.4, "PUT response time is too slow"
    
#     start = time.perf_counter()
#     response = requests.post(url, data=post_fields, timeout=timeout)
#     request_time = time.perf_counter() - start
#     self.logger.info("Request completed in {0:.0f} seconds".format(request_time))


def test_put_post_title_is_updated_correctly():
    """Test to check if the title in the PUT response is updated correctly."""
    response = requests.put(PUT_URL, json=PUT_POST_DATA)
    json_data = response.json()
    assert json_data.get("title") == PUT_POST_DATA["title"], "Title was not updated correctly"


def test_put_post_body_is_updated_correctly():
    """Test to check if the body in the PUT response is updated correctly."""
    response = requests.put(PUT_URL, json=PUT_POST_DATA)
    json_data = response.json()
    assert json_data.get("body") == PUT_POST_DATA["body"], "Body was not updated correctly"


def test_put_post_userid_matches_input():
    """Test to check if the userId in the PUT response matches the input."""
    response = requests.put(PUT_URL, json=PUT_POST_DATA)
    json_data = response.json()
    assert json_data.get("userId") == PUT_POST_DATA["userId"], "UserId does not match input"


def test_put_post_id_matches_input():
    """Test to check if the ID in the PUT response matches the input."""
    response = requests.put(PUT_URL, json=PUT_POST_DATA)
    json_data = response.json()
    assert json_data.get("id") == PUT_POST_DATA["id"], "ID does not match input"





#------------------------------------
#--------Post Posts------------------
#------------------------------------


def test_successful_post_request_POTS_post():
    """Test to check if the server responds with HTTP status code 200 or 201."""
    response = requests.post(POSTS_URL, json=DATA_POST)
    assert response.status_code in [200, 201], "POST request failed"

# #NOTE: This test will fail because the server is slow, sometime it's took more than 500ms
# def test_POTS_postresponse_time_is_less_than_500ms():
   
#     """Test to check if the POST response time is less than 500ms.
#        Sometime this test will fail because the server is slow "it tokes more than 500ms"
#     """
#     response = requests.post(POSTS_URL, json=DATA_POST)
#     assert response.elapsed.total_seconds() < 0.5, "POST response time is too slow"


def test_POTS_post_title_matches_input():
    """Test to check if the title in the POST response matches the input."""
    response = requests.post(POSTS_URL, json=DATA_POST)
    json_data = response.json()
    assert json_data.get("title") == DATA_POST["title"], "Title does not match input"


def test_POTS_post_body_matches_input():
    """Test to check if the body in the POST response matches the input."""
    response = requests.post(POSTS_URL, json=DATA_POST)
    json_data = response.json()
    assert json_data.get("body") == DATA_POST["body"], "Body does not match input"


def test_POTS_post_userid_matches_input():
    """Test to check if the userId in the POST response matches the input."""
    response = requests.post(POSTS_URL, json=DATA_POST)
    json_data = response.json()
    assert json_data.get("userId") == DATA_POST["userId"], "UserId does not match input"




#---------------------------------------------------------------
#----------------------DELETE POSTS BY ID-----------------------
#---------------------------------------------------------------

def test_successful_delete_todio_request():
    """Test to check if the server responds with HTTP status code 200, 202, or 204 for DELETE."""
    response = requests.delete(DELETE_URL)
    assert response.status_code in [200, 202, 204], "DELETE request failed"



def test_delete_post_not_found_after_deletion():
    """Test to check if the post is not found after it has been deleted."""
    # Perform DELETE request
    requests.delete(DELETE_URL)

    # Verify that the post no longer exists
    get_response = requests.get(DELETE_URL)
    assert get_response.status_code == 404, "Post still exists after deletion"

def test_delete_response_contains_success_message():
    """Test to check if the response body after DELETE contains a success message."""
    response = requests.delete(DELETE_URL)
    response_data = response.json()
    
    assert response.status_code in [200, 202, 204], "DELETE request failed"
    assert "message" in response_data, "Response does not contain a 'message' field"
    assert response_data["message"] == "Post deleted", "Response message is not 'Post deleted'"
    assert response_data["status"] == "success", "Response status is not 'success'"
