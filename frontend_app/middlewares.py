from frontend_app.models import Carousel

class Carousel:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_template_response(self, request, response):
        response.context_data['carousel'] = Carousel.objects.all()
        return response