from django.shortcuts import render, redirect

# Create your views here.
from web.forms import SearchForm
from web.models import Video, Img, Music


def index(request):
    # 主页
    return render(request, 'web/index.html')


def video(request):
    """视频网页"""
    videos = Video.objects.all()
    context = {'videos': videos}

    return render(request, 'web/video.html', context)


def music(request):
    """音乐网页"""
    re = ''
    re1 = ''
    music = Music.objects.all()
    re = []
    for i in music:
        re.append(i.name)

    # musics = music[0].file

    return render(request, 'web/music.html', locals())


def images(request):
    #     colour = [
    #         'card bg-primary text-white',
    #         'card bg-success text-white',
    #         'card bg-info text-white',
    #         'card bg-warning text-white',
    #         'card bg-secondary text-white',
    # ]
    """视频网页"""
    return render(request, 'web/images1.html')


def search(request):
    """搜索"""

    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入搜索关键词，开始搜索'
        return render(request, 'web/search.html', {'error_msg': error_msg})
    try:
        post_list = Video.objects.get(name=q)
    except:

        error_msg = '抱歉，没有找到你想要的内容'
        return render(request, 'web/search.html', {'error_msg': error_msg})
    else:
        return render(request, 'web/search.html', {'error_msg': error_msg,
                                                   'post_list': post_list})


def search_images(request):
    """搜索图片"""

    response = ""
    response1 = ""

    search_images = request.GET.get('search_images')
    error_msg = ''

    if not search_images:
        error_msg = '请输入搜索关键词，开始搜索'
        return render(request, 'web/search.html', {'error_msg': error_msg})
    try:
        imgs = Img.objects.filter(name=search_images)
    except:

        error_msg = '抱歉，没有找到你想要的内容'
        return render(request, 'web/search-images.html', {'error_msg': error_msg})
    else:

        return render(request, 'web/search-images.html', {'error_msg': error_msg,
                                                          'imgs': imgs})


def tv_play(request):
    data = Video.objects.filter(category_id=2).order_by("-date_time")
    return render(request, 'web/tv-play.html', locals())


def video_details(request,name):
    data = Video.objects.get(name=name)
    return render(request,'web/video_details.html',locals())