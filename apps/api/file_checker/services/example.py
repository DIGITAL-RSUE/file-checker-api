
# from service_objects import fields
# from service_objects.services import Service

# from ..models import Order, OrderPosition, SalePoint, Storage


# class OrderCreate(Service):
#     """ Сервис для формирования заказа"""

#     sale_point = fields.ModelField(SalePoint)
#     storage = fields.ModelField(Storage)
#     product_list = fields.ListField()

#     def process(self):
#         sale_point = self.cleaned_data["sale_point"]
#         storage = self.cleaned_data["storage"]
#         product_list = self.cleaned_data["product_list"]

#         order = Order.objects.create(
#             sale_point=sale_point, storage=storage, state="WAITING"
#         )

#         for product in product_list:
#             OrderPosition.objects.create(
#                 product=product["product_nomenclature"],
#                 count=product["selected_count"],
#                 order=order,
#             )

#         return order
