from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from dimensionsapp.models import Author, Serie, Jenre, PublishingHouse, FormatBook, Binding, \
    AgeRestriction
from dimensionsapp.form import SearchFormAuthor, AuthorModel, JenreModel, SerieModel, \
    PublishingHouseModel, FormatBookModel, BindingModel, AgeRestrictionModel, SearchForm
from django.views.generic import TemplateView, ListView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
# from goodsapp.models import Menu
# Create your views here.


class AuthorDetailView(DetailView):
    model = Author


class SerieDetailView(DetailView):
    model = Serie


class JenreDetailView(DetailView):
    model = Jenre


class PublishingHouseDetailView(DetailView):
    model = PublishingHouse


class FormatBookDetailView(DetailView):
    model = FormatBook


class BindingDetailView(DetailView):
    model = Binding


class AgeRestrictionDetailView(DetailView):
    model = AgeRestriction


class ListViewFilter(ListView):
    form = SearchForm
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'search' in self.request.GET:
            context['form'] = self.form({'search': self.request.GET['search']})
            context['search_string'] = self.request.GET['search']
        else:
            context['form'] = self.form()
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        if 'search' in self.request.GET and self.request.GET['search'] != '':
            name = self.request.GET['search']
            qs = qs.filter(name__istartswith=name)
        return qs


class SerieListView(ListViewFilter):
    model = Serie


class JenreListView(ListViewFilter):
    model = Jenre


class PublishingHouseListView(ListViewFilter):
    model = PublishingHouse

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['url_detail'] = 'publishing_house_detail'
    #     return context


class FormatBookListView(ListViewFilter):
    model = FormatBook


class BindingListView(ListViewFilter):
    model = Binding


class AgeRestrictionListView(ListViewFilter):
    model = AgeRestriction


class AuthorListView(ListViewFilter):
    model = Author
    form = SearchFormAuthor


class MenuView(TemplateView):
    template_name = 'dimensionsapp/menu_view.html'


class SerieCreateView(CreateView):
    model = Serie
    form_class = SerieModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('serie_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('serie_detail', kwargs={'pk': self.object.pk})
        return url


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('author_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('author_detail', kwargs={'pk': self.object.pk})
        return url


class JenreCreateView(CreateView):
    model = Jenre
    form_class = JenreModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('jenre_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('jenre_detail', kwargs={'pk': self.object.pk})
        return url


class PublishingHouseCreateView(CreateView):
    model = PublishingHouse
    form_class = PublishingHouseModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('publishing_house_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('publishing_house_detail', kwargs={'pk': self.object.pk})
        return url


class FormatBookCreateView(CreateView):
    model = FormatBook
    form_class = FormatBookModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('format_book_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('format_book_detail', kwargs={'pk': self.object.pk})
        return url


class BindingCreateView(CreateView):
    model = Binding
    form_class = BindingModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('binding_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('binding_detail', kwargs={'pk': self.object.pk})
        return url


class AgeRestrictionCreateView(CreateView):
    model = AgeRestriction
    form_class = AgeRestrictionModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('age_restriction_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('age_restriction_detail', kwargs={'pk': self.object.pk})
        return url


class SerieUpdateView(UpdateView):
    model = Serie
    form_class = SerieModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('serie_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('serie_detail', kwargs={'pk': self.object.pk})
        return url


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('author_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('author_detail', kwargs={'pk': self.object.pk})
        return url


class JenreUpdateView(UpdateView):
    model = Jenre
    form_class = JenreModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('jenre_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('jenre_detail', kwargs={'pk': self.object.pk})
        return url


class PublishingHouseUpdateView(UpdateView):
    model = PublishingHouse
    form_class = PublishingHouseModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('publishing_house_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('publishing_house_detail', kwargs={'pk': self.object.pk})
        return url


class FormatBookUpdateView(UpdateView):
    model = FormatBook
    form_class = FormatBookModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('format_book_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('format_book_detail', kwargs={'pk': self.object.pk})
        return url

    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        if 'save-as' in self.request.POST.keys() and 'pk' in kwargs.keys():
            print(self.object)
        return result


class BindingUpdateView(UpdateView):
    model = Binding
    form_class = BindingModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('binding_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('binding_detail', kwargs={'pk': self.object.pk})
        return url


class AgeRestrictionUpdateView(UpdateView):
    model = AgeRestriction
    form_class = AgeRestrictionModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('age_restriction_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('age_restriction_detail', kwargs={'pk': self.object.pk})
        return url


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author_list')


class SerieDeleteView(DeleteView):
    model = Serie
    success_url = reverse_lazy('serie_list')


class JenreDeleteView(DeleteView):
    model = Jenre
    success_url = reverse_lazy('jenre_list')


class PublishingHouseDeleteView(DeleteView):
    model = PublishingHouse
    success_url = reverse_lazy('publishing_house_list')


class FormatBookDeleteView(DeleteView):
    model = FormatBook
    success_url = reverse_lazy('format_book_list')


class BindingDeleteView(DeleteView):
    model = Binding
    success_url = reverse_lazy('binding_list')


class AgeRestrictionDeleteView(DeleteView):
    model = AgeRestriction
    success_url = reverse_lazy('age_restriction_list')
