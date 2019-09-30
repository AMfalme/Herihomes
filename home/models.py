from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from django import forms




class HomePage(Page):
    body = RichTextField(blank=True)
    

    content_panels = Page.content_panels + [
    FieldPanel('body', classname="full"),
    InlinePanel('Sliders', label="Slider section"),

    ]




class SliderInfo(Orderable):
    Page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name="Sliders")
    inftro_title = models.TextField(blank=True)
    intro_pitch = models.TextField(blank=True)
    pitch = models.TextField(blank=True)
    image = models.ForeignKey(
    'wagtailimages.Image', on_delete=models.CASCADE,null= True, related_name='+'
    )
    panels = [
    FieldPanel('inftro_title'),
    FieldPanel('intro_pitch'),
    FieldPanel('pitch'),
    ImageChooserPanel('image'),
    ]