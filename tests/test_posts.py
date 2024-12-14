import pytest
import requests


def test_get_all_posts(posts_url):
    given = "When requesting all posts"
    when = requests.get(posts_url)
    then = when.json()
        
    assert when.status_code == 200
    assert len(then) == 100
    assert all(isinstance(post, dict) for post in then)
        
def test_get_single_post(posts_url):
    given = "When requesting a single post"
    post_id = 1
    when = requests.get(f"{posts_url}/{post_id}")
    then = when.json()
        
    assert when.status_code == 200
    assert then["id"] == post_id
    assert "title" in then
    assert "body" in then
    assert "userId" in then
        
def test_create_post(posts_url, sample_post):
    given = "When creating a new post"
    when = requests.post(posts_url, json=sample_post)
    then = when.json()
        
    assert when.status_code == 201
    assert then["title"] == sample_post["title"]
    assert then["body"] == sample_post["body"]
    assert then["userId"] == sample_post["userId"]
    assert "id" in then
        
def test_update_post(posts_url, sample_post):
    given = "When updating a post"
    post_id = 1
    when = requests.put(f"{posts_url}/{post_id}", json=sample_post)
    then = when.json()
        
    assert when.status_code == 200
    assert then["id"] == post_id
    assert then["title"] == sample_post["title"]
    assert then["body"] == sample_post["body"]
        
def test_delete_post(posts_url):
    given = "When deleting a post"
    post_id = 1
    when = requests.delete(f"{posts_url}/{post_id}")
        
    assert when.status_code == 200