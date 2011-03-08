from django.contrib.auth.models import User

class ModelBackend(object):
    """
    Authenticates against django.contrib.auth.models.User.
    """
    # TODO: Model, login attribute name and password attribute name should be
    # configurable.
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.all().filter("username =", username).get()
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        
    def get_user(self, user_id):
        try:
            return User.objects.get(user_id)
        except User.DoesNotExist:
            return None
