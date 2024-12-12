

### **Phase 1: Project Setup and User Authentication**
#### 1. **Environment Setup**
   - Install Django and Django REST Framework:  
     ```bash
     pip install django djangorestframework
     ```
   - Create the project and app:  
     ```bash
     django-admin startproject social_media_api
     cd social_media_api
     python manage.py startapp accounts
     ```
   - Add `'rest_framework'` and `'accounts'` to `INSTALLED_APPS` in `settings.py`.

#### 2. **Custom User Model**
   - Extend `AbstractUser`:
     ```python
     from django.contrib.auth.models import AbstractUser
     from django.db import models

     class CustomUser(AbstractUser):
         bio = models.TextField(blank=True)
         profile_picture = models.ImageField(upload_to='profiles/', blank=True)
         followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
     ```
   - Update `settings.py`:
     ```python
     AUTH_USER_MODEL = 'accounts.CustomUser'
     ```

#### 3. **Authentication System**
   - Install `rest_framework.authtoken` and run migrations:
     ```bash
     pip install djangorestframework-simplejwt
     python manage.py makemigrations accounts
     python manage.py migrate
     ```
   - Use JWT for token-based authentication:
     ```python
     REST_FRAMEWORK = {
         'DEFAULT_AUTHENTICATION_CLASSES': [
             'rest_framework_simplejwt.authentication.JWTAuthentication',
         ],
     }
     ```

#### 4. **Create Registration and Login Views**
   - Write serializers and views for `register`, `login`, and `profile`.  
     Example `RegisterSerializer`:
     ```python
     from rest_framework import serializers
     from .models import CustomUser

     class RegisterSerializer(serializers.ModelSerializer):
         class Meta:
             model = CustomUser
             fields = ['username', 'password', 'email', 'bio', 'profile_picture']

         def create(self, validated_data):
             user = CustomUser.objects.create_user(**validated_data)
             return user
     ```

---

### **Phase 2: Posts and Comments Functionality**
#### 1. **Create Models**
   - Define models in `posts/models.py`:
     ```python
     from django.db import models
     from accounts.models import CustomUser

     class Post(models.Model):
         author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
         title = models.CharField(max_length=255)
         content = models.TextField()
         created_at = models.DateTimeField(auto_now_add=True)
         updated_at = models.DateTimeField(auto_now=True)

     class Comment(models.Model):
         post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
         author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
         content = models.TextField()
         created_at = models.DateTimeField(auto_now_add=True)
         updated_at = models.DateTimeField(auto_now=True)
     ```
   - Run migrations.

#### 2. **Create Serializers**
   - Example `PostSerializer`:
     ```python
     from rest_framework import serializers
     from .models import Post, Comment

     class PostSerializer(serializers.ModelSerializer):
         class Meta:
             model = Post
             fields = '__all__'
     ```

#### 3. **Define Views and Routes**
   - Use `ModelViewSet` for CRUD operations.

---

### **Phase 3: User Follows and Feed**
#### 1. **Update User Model for `following`**
   - Ensure the `followers` relationship is working correctly.

#### 2. **Follow/Unfollow Views**
   - Create views to handle follow actions.

#### 3. **Feed Functionality**
   - Use a query like:
     ```python
     posts = Post.objects.filter(author__in=request.user.following.all())
     ```

---

### **Phase 4: Likes and Notifications**
#### 1. **Models**
   - Create a `Like` model in `posts` and a `Notification` model in `notifications`.

#### 2. **Views**
   - Write views for liking/unliking posts and fetching notifications.

---

### **Phase 5: Deployment**
#### 1. **Configure Deployment Settings**
   - Update `settings.py` for production:
     ```python
     DEBUG = False
     ALLOWED_HOSTS = ['your-domain.com']
     ```

#### 2. **Use Gunicorn and Nginx**
   - Set up `gunicorn` for the WSGI server and Nginx for static files.

#### 3. **Deploy to Heroku or Render**
   - Configure `Procfile`, `requirements.txt`, and database settings for deployment.

