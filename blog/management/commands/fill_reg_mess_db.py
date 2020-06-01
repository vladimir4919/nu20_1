
from django.core.management.base import BaseCommand
from blogapp.models import Category, Post, Tag




class Command(BaseCommand):

    def handle(self, *args, **options):
        post= Post.objects.create(name='Ticket№1')
        сategory = Category.objects.create(name='оборудование',description='Область неисправности')
        tag = Tag.objects.create(name='электропитание')
        tag = Tag.objects.create(name='сервер')
        tag = Tag.objects.create(name='сетевое')
        tag = Tag.objects.create(name='кондиционирование')

        post = Post.objects.create(name='Ticket№2')
        сategory== Category.objects.create(name='программное обеспечение (ПО)',description='Область неисправности')

        )
        tag = Tag.objects.create(name='системное ПО')
        tag = Tag.objects.create(name='серверное ПО')
        tag = Tag.objects.create(name='сетевое ПО')

        post = Post.objects.create(name='Ticket№3')
        сategory== Category.objects.create(name='иное')

        tag = Tag.objects.create(name='ремонт')
        tag = Tag.objects.create(name='профилактика')
        tag = Tag.objects.create(name='аварийное элетропитание')