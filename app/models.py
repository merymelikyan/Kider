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


class FacilityMain(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Facility Main"
        verbose_name_plural = "Facility Main"



class Facilities(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=255)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Facilities"
        verbose_name_plural = "Facilities"



class MainSaction(models.Model):
    title = models.CharField(max_length=255)
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Main Saction"
        verbose_name_plural = "Main Saction"



class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.CharField(max_length=255, blank=True, null=True)
    description2 = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="about_us", blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"



class AboutImages(models.Model):
    image_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="about")
   

    def __str__(self):
        return f"{self.image_title}"
    
    class Meta:
        verbose_name = "About Images"
        verbose_name_plural = "About Images"


class Teacher(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.CharField(max_length=255, blank=True, null=True)
    description2 = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="teacher")
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teacher"



class ClassesMain(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Classes Main"
        verbose_name_plural = "Classes Main"



class Classes(models.Model):
    title = models.CharField(max_length=255)
    image1 = models.ImageField(upload_to="classes", blank=True, null=True)
    image2 = models.ImageField(upload_to="classes_teacher", blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    price= models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    capacity = models.CharField(max_length=255)


    def __str__(self):
       return self.title
    
    class Meta:
        verbose_name = "Classes"
        verbose_name_plural = "Classes"


class Appointment(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="appointment", blank=True, null=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointment"


class TeamMain(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Team Main"
        verbose_name_plural = "Team Main"


class TeamBlocks(models.Model):
    name= models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to="teams_blocks", null=True, blank=True)
    social_title1 = models.CharField(max_length=50, null=True, blank=True)
    social_title2 = models.CharField(max_length=50, null=True, blank=True)
    social_title3 = models.CharField(max_length=50, null=True, blank=True)
    social_url1 = models.URLField(max_length=255, blank=True)
    social_url2 = models.URLField(max_length=255, blank=True)
    social_url3 = models.URLField(max_length=255, blank=True)
    social_html_class1 = models.CharField(max_length=200, null=True, blank=True)
    social_html_class2 = models.CharField(max_length=200, null=True, blank=True)
    social_html_class3 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.image}"

    class Meta:
        verbose_name = "Team Blocks"
        verbose_name_plural = "Team Blocks"



class Testimonials(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Testimonials"
        verbose_name_plural = "Testimonials"



class TestimonialsBlocks(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="testimonials_blocks", blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    
  
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Testimonials blocks"
        verbose_name_plural = "Testimonials blocks"



class FooterMain(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Footer Main"
        verbose_name_plural = "Footer Main"


class GetInTouch(models.Model):
    title = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
   
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Get In Touch"
        verbose_name_plural = "Get In Touch"



class Socials(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=255, blank=True)
    html_class = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"




class QuickLinks(models.Model):
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255) 
    
    def __str__(self):
        return f"{self.link_name}"
    
    class Meta:
        verbose_name = "Quick Links"
        verbose_name_plural = "Quick Links"



class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletter"


class GalleryImages(models.Model):
    image_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="gallery")
   

    def __str__(self):
        return f"{self.image_title}"
    
    class Meta:
        verbose_name = "Gallery Images"
        verbose_name_plural = "Gallery Images"



class ContactUsMain(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.CharField(max_length=255, blank=True, null=True)
    description2 = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Contact  Us Main"
        verbose_name_plural = "Contact  Us Main"


class ContactBlocks(models.Model):
    title = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=255)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Contact  Blocks"
        verbose_name_plural = "Contact  Blocks"



class Error(models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon_class = models.CharField(max_length=255, blank=True, null=True)
 
    def __str__(self):
        return self.tag
    
    class Meta:
        verbose_name = "Error"
        verbose_name_plural = "Error"
