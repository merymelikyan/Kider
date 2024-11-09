from django.db import models


class HeaderText(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="header_text")
 
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Header Text"
        verbose_name_plural = "Header Text"


 
class FooterText(models.Model):
    text1 = models.CharField(max_length=55, blank=True, null=True)
    text2 = models.CharField(max_length=255, blank=True, null=True)
    text3 = models.CharField(max_length=255, blank=True, null=True)
    link_url = models.URLField(max_length=200, blank=True, null=True)
    link_url2 = models.CharField(max_length=255, blank=True, null=True)
    link_name1 = models.CharField(max_length=255, blank=True, null=True)
    link_name2 = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.text2

    class Meta:
        verbose_name = "Footer Text"
        verbose_name_plural = "Footer Text"

