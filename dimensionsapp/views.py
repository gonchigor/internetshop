# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView
from dimensionsapp.models import Author, Serie, Jenre, PublishingHouse, FormatBook, Binding, \
    AgeRestriction, OrderStatus
from dimensionsapp.form import SearchFormAuthor, AuthorModel, JenreModel, SerieModel, \
    PublishingHouseModel, FormatBookModel, BindingModel, AgeRestrictionModel, SearchForm, \
    OrderStatusModel
from django.views.generic import TemplateView, ListView
# from django.views.generic import DeleteView
from django.urls import reverse_lazy
from orderapp.permissions import ManagerDetailView, ManagerCreateView, ManagerDeleteView, \
    ManagerListView, ManagerUpdateView, ManagerAuthorizationRequired
# from goodsapp.models import Menu
# Create your views here.


class AuthorDetailView(ManagerDetailView):
    model = Author


class SerieDetailView(ManagerDetailView):
    model = Serie


class JenreDetailView(ManagerDetailView):
    model = Jenre


class PublishingHouseDetailView(ManagerDetailView):
    model = PublishingHouse


class FormatBookDetailView(ManagerDetailView):
    model = FormatBook


class BindingDetailView(ManagerDetailView):
    model = Binding


class AgeRestrictionDetailView(ManagerDetailView):
    model = AgeRestriction


class OrderStatusDetailView(ManagerDetailView):
    model = OrderStatus


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
            qs = qs.filter(name__icontains=name)
        return qs


class ManagerListViewFilter(ManagerAuthorizationRequired, ListViewFilter):
    pass


class SerieListView(ManagerListViewFilter):
    model = Serie


class JenreListView(ManagerListViewFilter):
    model = Jenre


class PublishingHouseListView(ManagerListViewFilter):
    model = PublishingHouse


class FormatBookListView(ManagerListViewFilter):
    model = FormatBook


class BindingListView(ManagerListViewFilter):
    model = Binding


class AgeRestrictionListView(ManagerListViewFilter):
    model = AgeRestriction


class AuthorListView(ManagerListViewFilter):
    model = Author
    form = SearchFormAuthor


class OrderStatusListView(ManagerListViewFilter):
    model = OrderStatus


class MenuView(ManagerAuthorizationRequired, TemplateView):
    template_name = 'dimensionsapp/menu_view.html'


class SerieCreateView(ManagerCreateView):
    model = Serie
    form_class = SerieModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('serie_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('serie_detail', kwargs={'pk': self.object.pk})
        return url


class AuthorCreateView(ManagerCreateView):
    model = Author
    form_class = AuthorModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('author_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('author_detail', kwargs={'pk': self.object.pk})
        return url


class JenreCreateView(ManagerCreateView):
    model = Jenre
    form_class = JenreModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('jenre_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('jenre_detail', kwargs={'pk': self.object.pk})
        return url


class PublishingHouseCreateView(ManagerCreateView):
    model = PublishingHouse
    form_class = PublishingHouseModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('publishing_house_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('publishing_house_detail', kwargs={'pk': self.object.pk})
        return url


class FormatBookCreateView(ManagerCreateView):
    model = FormatBook
    form_class = FormatBookModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('format_book_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('format_book_detail', kwargs={'pk': self.object.pk})
        return url


class BindingCreateView(ManagerCreateView):
    model = Binding
    form_class = BindingModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('binding_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('binding_detail', kwargs={'pk': self.object.pk})
        return url


class AgeRestrictionCreateView(ManagerCreateView):
    model = AgeRestriction
    form_class = AgeRestrictionModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('age_restriction_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('age_restriction_detail', kwargs={'pk': self.object.pk})
        return url


class OrderStatusCreateView(ManagerCreateView):
    model = OrderStatus
    form_class = OrderStatusModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('order_status_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('order_status_detail', kwargs={'pk': self.object.pk})
        return url


class SerieUpdateView(ManagerUpdateView):
    model = Serie
    form_class = SerieModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('serie_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('serie_detail', kwargs={'pk': self.object.pk})
        return url


class AuthorUpdateView(ManagerUpdateView):
    model = Author
    form_class = AuthorModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('author_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('author_detail', kwargs={'pk': self.object.pk})
        return url


class JenreUpdateView(ManagerUpdateView):
    model = Jenre
    form_class = JenreModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('jenre_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('jenre_detail', kwargs={'pk': self.object.pk})
        return url


class PublishingHouseUpdateView(ManagerUpdateView):
    model = PublishingHouse
    form_class = PublishingHouseModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('publishing_house_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('publishing_house_detail', kwargs={'pk': self.object.pk})
        return url


class FormatBookUpdateView(ManagerUpdateView):
    model = FormatBook
    form_class = FormatBookModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('format_book_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('format_book_detail', kwargs={'pk': self.object.pk})
        return url


class BindingUpdateView(ManagerUpdateView):
    model = Binding
    form_class = BindingModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('binding_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('binding_detail', kwargs={'pk': self.object.pk})
        return url


class AgeRestrictionUpdateView(ManagerUpdateView):
    model = AgeRestriction
    form_class = AgeRestrictionModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('age_restriction_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('age_restriction_detail', kwargs={'pk': self.object.pk})
        return url


class OrderStatusUpdateView(ManagerUpdateView):
    model = OrderStatus
    form_class = OrderStatusModel

    def get_success_url(self):
        url = super().get_success_url()
        if 'save-and-close' in self.request.POST.keys():
            url = reverse_lazy('order_status_list')
        elif 'save' in self.request.POST.keys():
            url = reverse_lazy('order_status_detail', kwargs={'pk': self.object.pk})
        return url


class AuthorDeleteView(ManagerDeleteView):
    model = Author
    success_url = reverse_lazy('author_list')


class SerieDeleteView(ManagerDeleteView):
    model = Serie
    success_url = reverse_lazy('serie_list')


class JenreDeleteView(ManagerDeleteView):
    model = Jenre
    success_url = reverse_lazy('jenre_list')


class PublishingHouseDeleteView(ManagerDeleteView):
    model = PublishingHouse
    success_url = reverse_lazy('publishing_house_list')


class FormatBookDeleteView(ManagerDeleteView):
    model = FormatBook
    success_url = reverse_lazy('format_book_list')


class BindingDeleteView(ManagerDeleteView):
    model = Binding
    success_url = reverse_lazy('binding_list')


class AgeRestrictionDeleteView(ManagerDeleteView):
    model = AgeRestriction
    success_url = reverse_lazy('age_restriction_list')


class OrderStatusDeleteView(ManagerDeleteView):
    model = OrderStatus
    success_url = reverse_lazy('order_status_list')
