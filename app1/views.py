from django.http import JsonResponse
from shared_models.models import User

def user_list(request):
    users = User.objects.all().values('name', 'email', 'created_at', 'updated_at')
    return JsonResponse(list(users), safe=False)
