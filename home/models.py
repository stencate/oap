from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from django.db import models
from django.utils.translation import gettext_lazy as _

class HomePage(Page):
    class Meta:
        verbose_name = "home page"

    hero_title = RichTextField(blank=True)
    sub_title = models.CharField(max_length=200, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('title'),
        FieldPanel('hero_title'),
        FieldPanel('sub_title'),
        InlinePanel('gallery_images', label=_("Gallery images")),
    ]


class ImageGallery(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]
