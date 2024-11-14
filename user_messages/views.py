from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message


@csrf_exempt
def receive_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        cname = request.POST.get('cname')
        cage = request.POST.get('cage')
        content = request.POST.get('content')

        if name and email and cname and cage and content:
            Message.objects.create(name=name, email=email, cname=cname, cage=cage, content=content)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Missing data'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    #     new_message = Message.objects.create(
    #         name=name,
    #         email=email,
    #         cname=cname,
    #         cage=cage,
    #         content=content
    #     )   
    #     new_message.save()

    #     return JsonResponse({'success': True, 'message': 'Data saved successfully'})

    # return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

