from django.test import TestCase
from .models import Product, Box
from .services import recommend_box


class RecommendationTest(TestCase):

    def test_recommend_box(self):
        # Create Product
        product = Product.objects.create(
            name="Laptop",
            length=35,
            width=25,
            height=4,
            weight=2,
        )

        # Create Boxes
        Box.objects.create(
            name="Small",
            length=20,
            width=20,
            height=20,
            max_weight=5,
            cost=40,
        )

        medium = Box.objects.create(
            name="Medium",
            length=50,
            width=30,
            height=20,
            max_weight=10,
            cost=60,
        )

        # Call recommendation function
        box = recommend_box([product])

        # Verify result
        self.assertEqual(box.id, medium.id)