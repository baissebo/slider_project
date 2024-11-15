from django.views.generic import TemplateView

from slider.models import SliderImage


class SliderView(TemplateView):
    template_name = "slider/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["slider_images"] = SliderImage.objects.all()
        return context
