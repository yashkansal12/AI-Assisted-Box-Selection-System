from .models import Box


def recommend_box(products):

    package_length = max(product.length for product in products)
    package_width = max(product.width for product in products)
    package_height = sum(product.height for product in products)
    package_weight = sum(product.weight for product in products)

    suitable_boxes = []

    for box in Box.objects.all():

        if (
            box.length >= package_length
            and box.width >= package_width
            and box.height >= package_height
            and box.max_weight >= package_weight
        ):
            suitable_boxes.append(box)

    if not suitable_boxes:
        return None

    suitable_boxes.sort(key=lambda x: x.cost)

    return suitable_boxes[0]