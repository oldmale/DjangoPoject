import os.path

from django.db import models

# Create your models here.
def upload_to_video(instance,filename):
    return "{0}/{1}/{2}".format(instance.category.name, 'video', filename)

class VideoCategory(models.Model):
    """视频分类"""
    name = models.CharField(max_length=50,verbose_name='名称',unique=True)
    c_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['c_time']
        verbose_name = "视频分类"
        verbose_name_plural = "视频类别"

    def __str__(self):
        return self.name


class Video(models.Model):
    category = models.ForeignKey(VideoCategory,on_delete=models.CASCADE,verbose_name='视频分类')
    name = models.CharField(max_length=256,verbose_name='视频名称',default=None)
    url = models.CharField(max_length=256,verbose_name='视频链接')
    url_code = models.CharField(max_length=20,verbose_name='提取码')
    image = models.ImageField(upload_to=upload_to_video, verbose_name='视频图片')
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_time']
        verbose_name = "视频"
        verbose_name_plural = "视频"



class ImgCategory(models.Model):
    """图片类别"""
    name = models.CharField(max_length=20,verbose_name='名称',unique=True)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_time']
        verbose_name = "类别"
        verbose_name_plural = "图片类别"

    def __str__(self):
        return self.name

def upload_to(instance,filename):
    return "{0}/{1}/{2}".format(instance.category.name,'image',filename)

class Img(models.Model):
    """图片信息"""
    category = models.ForeignKey(ImgCategory, on_delete=models.CASCADE,verbose_name='分类')
    url = models.CharField(max_length=255,null=True,blank=True)
    name = models.CharField(max_length=20,verbose_name='名称')
    image = models.ImageField(upload_to=upload_to,verbose_name='图片')
    date_time = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-date_time']
        verbose_name = "图片"
        verbose_name_plural = "上传图片"

    def __str__(self):
        a = str(self.image) + ',' + str(self.category)
        return a

class Music(models.Model):
    name = models.CharField(max_length=50,verbose_name='歌名')
    singer = models.CharField(max_length=50,verbose_name='歌手')
    album = models.CharField(max_length=20,verbose_name='时长')
    file = models.FileField(upload_to='music',verbose_name='音乐文件')
    c_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-c_time']
        verbose_name = "音乐"
        verbose_name_plural = "上传音乐文件"




   