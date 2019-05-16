from django.urls import path
from dimensionsapp.views import AuthorDetailView, SerieDetailView, JenreDetailView, PublishingHouseDetailView, \
     FormatBookDetailView, BindingDetailView, AgeRestrictionDetailView, SerieListView, AuthorListView, \
     JenreListView, PublishingHouseListView, FormatBookListView, BindingListView, AgeRestrictionListView, \
     MenuView, SerieCreateView, AuthorCreateView, JenreCreateView, PublishingHouseCreateView, \
     FormatBookCreateView, BindingCreateView, AgeRestrictionCreateView, AuthorUpdateView, SerieUpdateView, \
     JenreUpdateView, PublishingHouseUpdateView, FormatBookUpdateView, BindingUpdateView, AgeRestrictionUpdateView, \
     SerieDeleteView, AuthorDeleteView, JenreDeleteView, PublishingHouseDeleteView, FormatBookDeleteView, \
     BindingDeleteView, AgeRestrictionDeleteView, OrderStatusCreateView, OrderStatusDeleteView, OrderStatusDetailView, \
     OrderStatusListView, OrderStatusUpdateView


urlpatterns = [

    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('serie/<int:pk>/', SerieDetailView.as_view(), name='serie_detail'),
    path('jenre/<int:pk>/', JenreDetailView.as_view(), name='jenre_detail'),
    path('publishing/<int:pk>/', PublishingHouseDetailView.as_view(), name='publishing_house_detail'),
    path('format/<int:pk>/', FormatBookDetailView.as_view(), name='format_book_detail'),
    path('binding/<int:pk>/', BindingDetailView.as_view(), name='binding_detail'),
    path('agerestriction/<int:pk>/', AgeRestrictionDetailView.as_view(), name='age_restriction_detail'),
    path('orderstatus/<int:pk>/', OrderStatusDetailView.as_view(), name='order_status_detail'),

    path('author/', AuthorListView.as_view(), name='author_list'),
    path('serie/', SerieListView.as_view(), name='serie_list'),
    path('jenre/', JenreListView.as_view(), name='jenre_list'),
    path('publishing/', PublishingHouseListView.as_view(), name='publishing_house_list'),
    path('format/', FormatBookListView.as_view(), name='format_book_list'),
    path('binding/', BindingListView.as_view(), name='binding_list'),
    path('agerestriction/', AgeRestrictionListView.as_view(), name='age_restriction_list'),
    path('orderstatus/', OrderStatusListView.as_view(), name='order_status_list'),

    path('serie/create/', SerieCreateView.as_view(), name='serie_create'),
    path('author/create/', AuthorCreateView.as_view(), name='author_create'),
    path('jenre/create/', JenreCreateView.as_view(), name='jenre_create'),
    path('publishing/create/', PublishingHouseCreateView.as_view(), name='publishing_house_create'),
    path('format/create/', FormatBookCreateView.as_view(), name='format_book_create'),
    path('binding/create/', BindingCreateView.as_view(), name='binding_create'),
    path('agerestriction/create/', AgeRestrictionCreateView.as_view(), name='age_restriction_create'),
    path('orderstatus/create/', OrderStatusCreateView.as_view(), name='order_status_create'),

    path('author/<int:pk>/update/', AuthorUpdateView.as_view(), name='author_update'),
    path('serie/<int:pk>/update/', SerieUpdateView.as_view(), name='serie_update'),
    path('jenre/<int:pk>/update/', JenreUpdateView.as_view(), name='jenre_update'),
    path('publishing/<int:pk>/update/', PublishingHouseUpdateView.as_view(), name='publishing_house_update'),
    path('format/<int:pk>/update/', FormatBookUpdateView.as_view(), name='format_book_update'),
    path('binding/<int:pk>/update/', BindingUpdateView.as_view(), name='binding_update'),
    path('agerestriction/<int:pk>/update/', AgeRestrictionUpdateView.as_view(), name='age_restriction_update'),
    path('orderstatus/<int:pk>/update/', OrderStatusUpdateView.as_view(), name='order_status_update'),

    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
    path('serie/<int:pk>/delete/', SerieDeleteView.as_view(), name='serie_delete'),
    path('jenre/<int:pk>/delete/', JenreDeleteView.as_view(), name='jenre_delete'),
    path('publishing/<int:pk>/delete/', PublishingHouseDeleteView.as_view(), name='publishing_house_delete'),
    path('format/<int:pk>/delete/', FormatBookDeleteView.as_view(), name='format_book_delete'),
    path('binding/<int:pk>/delete/', BindingDeleteView.as_view(), name='binding_delete'),
    path('agerestriction/<int:pk>/delete/', AgeRestrictionDeleteView.as_view(), name='age_restriction_delete'),
    path('orderstatus/<int:pk>/delete/', OrderStatusDeleteView.as_view(), name='order_status_delete'),


    path('', MenuView.as_view(), name='dimensions_list')
]
