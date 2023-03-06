from django.db import models, User

# Create your models here.


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    desired_product = models.ForeignKey(product, on_delete=models.CASCADE)
    slug = models.CharField(max_length=254, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)

    # update your model
    def serialize(self):

        return {
            "id": self.desired_product.id,
            "slug": self.slug
        }
