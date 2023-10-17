from ninja import Router
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import User
from .schemas import *

userRouter = Router()

@userRouter.post('signup', response={200: UserSchema, 404: dict})
def signup_user(request, credentials: UserSchemaAuth):
    user = User.objects.create_user(credentials.email, **credentials.dict())
    return signin_user(request, credentials)

@userRouter.post('signin', response={200: UserSchema, 404: dict})
def signin_user(request, credentials: UserSchemaAuth):
    user = authenticate(request, email=credentials.email, password=credentials.password)
    if user is not None:
        login(request, user)
        return 200, user
    else:
        return 404, {'detail': 'Failed to login with that email and password'}

@userRouter.post('logout', response={200: dict})
@login_required()
def logout_user(request):
    logout(request)
    return 200, {'success': True}
