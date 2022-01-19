from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()


class Order(models.Model):

 CATEGORIES=(
  ('MATOOKE','matooke'),
  ('CASSAVA','cassava'),
  ('RICE','rice'),
  ('POSHO','posho'),
 )

 ORDER_STATUS=(
  ('PENDING','pending'),
  ('IN_TRANSIT','inTransit'),
  ('DELIVERED','delivered'),
 )
 
 
 customer=models.ForeignKey(User,on_delete=models.CASCADE)
 size=models.CharField(max_length=20,choices=CATEGORIES,default=[0][0])
 order_status=models.CharField(max_length=20,choices=ORDER_STATUS,default=[0][0])
 quantity=models.IntegerField()
 created_at=models.DateTimeField(auto_now=True)
 updated_at=models.DateTimeField(auto_now=True)


 def __str__(self):
  return f"<Order{self.size} by {self.customer.id}>"

