from django.shortcuts import render



def post_list(request):
	return render(request, 'website/post_list.html', {})
