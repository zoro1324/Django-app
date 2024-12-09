from typing import Any
from blog.models import Catagory
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "To insert Catagories"
    def handle(self, *args : Any, **options : Any):

        catagories = ["Food", "Artificial Intelligence", "Data Science", "Games", "Sports"]
        
        for catagory in catagories:
            Catagory.objects.create(catagories=catagory)

        self.stdout.write(self.style.SUCCESS("Sucessfully inserted Catagories"))
