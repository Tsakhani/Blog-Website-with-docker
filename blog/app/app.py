from flask import Flask, render_template, request, redirect, url_for
import redis
import os

app = Flask(__name__)

# Fetch the Redis URL from environment variable (you can set this in docker-compose.yml)
redis_host = os.environ.get('REDIS_HOST', 'redis')  # Default to 'redis' (Docker service name)
redis_port = os.environ.get('REDIS_PORT', 6379)     # Default to port 6379
redis_db = os.environ.get('REDIS_DB', 0)            # Default to database 0

# Create a Redis client connection
redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

# Set up Redis keys for storing blog posts
POSTS_KEY = "posts"

# Home page route
@app.route('/')
def home():
    # Fetch all blog posts from Redis
    posts = redis_client.lrange(POSTS_KEY, 0, -1)
    # Decode the byte strings and prepare for rendering
    posts = [post.decode('utf-8') for post in posts]
    return render_template('index.html', posts=posts)

# Add new blog post route
@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        # Create the blog post (title + content)
        post = f"{title}\n\n{content}"
        
        # Store the post in Redis as a list
        redis_client.rpush(POSTS_KEY, post)
        
        return redirect(url_for('home'))
    return render_template('add_post.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
