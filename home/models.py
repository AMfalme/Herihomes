from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from django import forms
from wagtail.search import index



class HomePage(Page):
    body = RichTextField(blank=True)
    def get_context(self, request):
        # Update context to include only published portolio projects, ordered by reverse-chron
        context = super().get_context(request)
        portfolios = self.get_children().live().type(ProjectsPage)
        # featured_projects = portfolios.get_children().filter(Featured = True)
        # context['featured_projects'] = featured_projects
        context['menuitems'] = self.get_children().filter(
        live=True, show_in_menus=True)
        return context
    
    content_panels = Page.content_panels + [
    FieldPanel('body', classname="full"),
    InlinePanel('Sliders', label="Slider section"),
    InlinePanel('Testimonials', label="Testimonials")

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


class PortfolioPage(Page):
    body = RichTextField(blank=True)
    def get_context(self, request):
        context = super().get_context(request)
        portfolios = self.get_children().live().type(ProjectsPage)
        # featured_projects =self.get_children().filter(Featured = True)
        context['portfolios'] = portfolios
        # context['featured_projects'] = featured_projects
        return context
    content_panels = Page.content_panels + [
    FieldPanel('body')
    ]


class ProjectsPage(Page):
    body = RichTextField(blank=True)
    location = models.TextField(blank=True)
    Squarefeet = models.TextField(blank=True)
    beds = models.TextField(blank=True)
    lifts =  models.BooleanField(default=False)
    Featured = models.BooleanField(default=False)
    baths = models.TextField(blank=True)
    garage = models.TextField(default=True)
    floors = models.TextField(blank=True)
    project_image = models.ForeignKey(
    'wagtailimages.Image', on_delete=models.SET_NULL,null= True, related_name='+'
    )
    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('Featured'),
    ]
    content_panels = Page.content_panels + [
    FieldPanel('body'),
    FieldPanel('location'),
    FieldPanel('Squarefeet'),
    FieldPanel('beds'),
    FieldPanel('lifts'),
    FieldPanel('Featured'),
    FieldPanel('baths'),
    FieldPanel('garage'),
    FieldPanel('floors'),
    ImageChooserPanel('project_image'),
    InlinePanel('portfolio_images', label = "Project images")
    ]
class portfolio_images(Orderable):
    Page = ParentalKey(ProjectsPage, on_delete=models.CASCADE, related_name="portfolio_images")
    tag = models.TextField(blank=True)
    pitch = models.TextField(blank=True)
    image = models.ForeignKey(
    'wagtailimages.Image', on_delete=models.CASCADE,null= True, related_name='+'
    )
    panels = [
    FieldPanel('tag'),
    FieldPanel('pitch'),
    ImageChooserPanel('image'),
    ]
class Testimonials(Orderable):
    Page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name = "Testimonials")
    client_quote = models.TextField(blank=True)
    client_testimony =RichTextField()
    client_name = models.TextField(blank=True)
    client_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
        )
    panels =  [
    FieldPanel('client_quote'),
    FieldPanel('client_testimony'),
    FieldPanel('client_name'),
    ImageChooserPanel('client_image')
    ]



class AboutPage(Page):
    body = RichTextField(blank=True)
    about_title = models.TextField(default="Affordable, Quality Housing")
    approach = RichTextField(blank=True)
    value_proposition = RichTextField(blank=True)
    content_panels = Page.content_panels + [
    FieldPanel('body', classname="full"),
    FieldPanel('about_title'),
    FieldPanel('approach'),
    FieldPanel('value_proposition', classname="text-white")
    ]

