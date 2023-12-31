from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(str(data), 'django')


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django', create_by_id=1, slug='django', price='20',
                                            image='django')
    def test_products_model_entry(self):
        data=self.data1
        self.assertTrue(isinstance(data,Product))
        self.assertTrue(str(data),'django')