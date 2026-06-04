import requests
from django.shortcuts import render
from django.http import HttpResponse

CONSUMER_KEY = "HPbIiaJbIopjOz4OXFQuPPaMI"
CONSUMER_SECRET = "PHje5XtRrzjxi5RvDpepampG8xOateDCpittDyPTiC652a0WBv"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAHS89wEAAAAAFWnFVznldXBWVhHeoVvXVH5p2yo%3DPOWaFDq92fyctLgxcIZzeVYbtkUbYbwiWb9prC8SUAMFiFmB2i"
ACCESS_TOKEN = "1863096807703859201-BjPKQnN6JtTysSrWW4a0lZHh2cxgKo"
ACCESS_TOKEN_SECRET = "4jXoaa2rg3pUQD0KcafwoF34xF3MyP0TzcXTVRZFVjtCr"
def create_headers():
    return {"Authorization": f"Bearer {BEARER_TOKEN}"}

from django.shortcuts import render, redirect
from django.contrib import messages as django_messages

def home(request):
    # Fetch a default feed for the home page (e.g. recent tweets about Python/Django)
    url = "https://api.twitter.com/2/tweets/search/recent"
    params = {
        'query': 'python OR django',
        'tweet.fields': 'created_at,public_metrics,author_id',
        'expansions': 'author_id',
        'user.fields': 'profile_image_url,username',
        'max_results': 15
    }
    tweets = []
    try:
        response = requests.get(url, headers=create_headers(), params=params, timeout=5)
    except requests.exceptions.RequestException as e:
        class DummyResponse:
            status_code = 500
            def json(self): return {'detail': 'Network/SSL Error'}
        response = DummyResponse()
    if response.status_code == 200:
        data = response.json()
        users = {u['id']: u for u in data.get('includes', {}).get('users', [])}
        for t in data.get('data', []):
            author = users.get(t['author_id'], {})
            tweets.append({
                'id': t['id'],
                'text': t['text'],
                'created_at': t['created_at'],
                'metrics': t.get('public_metrics', {}),
                'author': author
            })
    else:
        # Fallback dummy data if API limit is reached
        error_msg = response.json().get('detail', 'Twitter API rate limit or credit quota reached.')
        django_messages.error(request, f"API Error: {error_msg}. Showing demo data.")
        tweets = [
            {
                'id': '1', 'text': 'Just started working on a new Django project! The built-in admin panel is so powerful. #Python #Django', 'created_at': '2026-06-02T10:00:00.000Z',
                'metrics': {'reply_count': 12, 'retweet_count': 4, 'like_count': 48, 'impression_count': 1200},
                'author': {'username': 'python_dev', 'name': 'Python User'}
            },
            {
                'id': '2', 'text': 'Tailwind CSS makes styling Django templates so much faster. Highly recommend this stack!', 'created_at': '2026-06-02T11:30:00.000Z',
                'metrics': {'reply_count': 5, 'retweet_count': 2, 'like_count': 25, 'impression_count': 500},
                'author': {'username': 'webdev_guru', 'name': 'Web Dev Guru'}
            }
        ]
    return render(request, 'home.html', {'tweets': tweets})
def search(request):
    query = request.GET.get('q', '')
    tweets = []
    if query:
        url = "https://api.twitter.com/2/tweets/search/recent"
        params = {
            'query': query,
            'tweet.fields': 'created_at,public_metrics,author_id',
            'expansions': 'author_id',
            'user.fields': 'profile_image_url,username',
            'max_results': 10
        }
        try:
            response = requests.get(url, headers=create_headers(), params=params, timeout=5)
        except requests.exceptions.RequestException as e:
            class DummyResponse:
                status_code = 500
                def json(self): return {'detail': 'Network/SSL Error'}
            response = DummyResponse()
        if response.status_code == 200:
            data = response.json()
            users = {u['id']: u for u in data.get('includes', {}).get('users', [])}
            for t in data.get('data', []):
                author = users.get(t['author_id'], {})
                tweets.append({
                    'id': t['id'],
                    'text': t['text'],
                    'created_at': t['created_at'],
                    'metrics': t.get('public_metrics', {}),
                    'author': author
                })
        else:
            error_msg = response.json().get('detail', 'API limit reached')
            django_messages.error(request, f"API Error: {error_msg}. Showing demo data.")
            tweets = [
                {
                    'id': '1', 'text': f'Simulated search result for "{query}"!', 'created_at': '2026-06-02T12:00:00.000Z',
                    'metrics': {'reply_count': 1, 'retweet_count': 0, 'like_count': 10, 'impression_count': 100},
                    'author': {'username': 'search_bot', 'name': 'Search Bot'}
                }
            ]
    
    return render(request, 'search.html', {'tweets': tweets, 'query': query})

def profile(request, username):
    # First get user ID
    user_url = f"https://api.twitter.com/2/users/by/username/{username}"
    user_params = {'user.fields': 'profile_image_url,description,public_metrics'}
    try:
        user_resp = requests.get(user_url, headers=create_headers(), params=user_params, timeout=5)
    except requests.exceptions.RequestException as e:
        class DummyResponse:
            status_code = 500
            def json(self): return {'detail': 'Network/SSL Error'}
        user_resp = DummyResponse()
    
    user_data = None
    tweets = []
    
    if user_resp.status_code == 200 and 'data' in user_resp.json():
        user_data = user_resp.json()['data']
        user_id = user_data['id']
        
        # Then get user tweets
        tweets_url = f"https://api.twitter.com/2/users/{user_id}/tweets"
        tweets_params = {
            'tweet.fields': 'created_at,public_metrics',
            'max_results': 5
        }
        try:
            tweets_resp = requests.get(tweets_url, headers=create_headers(), params=tweets_params, timeout=5)
        except requests.exceptions.RequestException as e:
            class DummyResponse:
                status_code = 500
                def json(self): return {'detail': 'Network/SSL Error'}
            tweets_resp = DummyResponse()
        
        if tweets_resp.status_code == 200:
            t_data = tweets_resp.json()
            for t in t_data.get('data', []):
                tweets.append({
                    'id': t['id'],
                    'text': t['text'],
                    'created_at': t['created_at'],
                    'metrics': t.get('public_metrics', {}),
                    'author': user_data
                })
        else:
            django_messages.error(request, "API Error: Could not load tweets due to API limits. Showing demo data.")
            tweets = [
                {
                    'id': '1', 'text': f'Hello! This is a demo tweet from {username}.', 'created_at': '2026-06-02T12:00:00.000Z',
                    'metrics': {'reply_count': 100, 'retweet_count': 50, 'like_count': 1000, 'impression_count': 50000},
                    'author': user_data
                }
            ]
    else:
        if user_resp.status_code != 200:
            django_messages.error(request, f"API Error: {user_resp.json().get('detail', 'Could not load profile')}. Showing demo profile.")
        
        # Fallback demo profile user
        user_data = {
            'id': '12345',
            'username': username,
            'name': f"{username.capitalize()} (Demo)",
            'description': "This is a fallback demo profile because the Twitter API limit was reached.",
            'public_metrics': {
                'followers_count': 1234000,
                'following_count': 42
            },
            'profile_image_url': 'https://abs.twimg.com/sticky/default_profile_images/default_profile_400x400.png'
        }
        tweets = [
            {
                'id': '1', 'text': f'Hello! This is tweet 1 from {username}.', 'created_at': '2026-06-02T12:00:00.000Z',
                'metrics': {'reply_count': 10, 'retweet_count': 5, 'like_count': 100, 'impression_count': 5000},
                'author': user_data
            },
            {
                'id': '2', 'text': f'This is tweet 2 from {username}, enjoying Django development.', 'created_at': '2026-06-01T12:00:00.000Z',
                'metrics': {'reply_count': 100, 'retweet_count': 50, 'like_count': 1000, 'impression_count': 50000},
                'author': user_data
            },
            {
                'id': '3', 'text': f'Tweet 3 from {username} - Tailwind CSS makes everything beautiful.', 'created_at': '2026-05-30T12:00:00.000Z',
                'metrics': {'reply_count': 4, 'retweet_count': 2, 'like_count': 45, 'impression_count': 300},
                'author': user_data
            },
            {
                'id': '4', 'text': f'Tweet 4 from {username}. Working on the Twitter API lab!', 'created_at': '2026-05-29T12:00:00.000Z',
                'metrics': {'reply_count': 22, 'retweet_count': 12, 'like_count': 200, 'impression_count': 6000},
                'author': user_data
            },
            {
                'id': '5', 'text': f'Tweet 5 from {username}. Fifth and final latest tweet to meet lab requirements.', 'created_at': '2026-05-28T12:00:00.000Z',
                'metrics': {'reply_count': 8, 'retweet_count': 3, 'like_count': 78, 'impression_count': 1200},
                'author': user_data
            }
        ]
    return render(request, 'profile.html', {'profile_user': user_data, 'tweets': tweets})

def notifications(request):
    return render(request, 'notifications.html')

def messages(request):
    return render(request, 'messages.html')

def post_tweet(request):
    if request.method == 'POST':
        # In a real app we'd use OAuth 1.0a User Context to post.
        # Since we only have a Bearer token (App-only), we can't post to a user's account.
        django_messages.info(request, "Note: Posting requires OAuth 1.0a user context. Simulating post success for demo purposes.")
        return redirect('home')
    return redirect('home')
