from typing import List, Optional
from ninja.files import UploadedFile
from ninja import NinjaAPI, File
from tracks.models import Track
from tracks.schema import TrackSchema, NotFoundSchema

# http://localhost:8000/api/tracks?title=a
# http://localhost:8000/api/tracks/1?title=a

api = NinjaAPI()

@api.get("/tracks", response=List[TrackSchema])
def tracks(request, title: Optional[str] = None): # [중요] 검색 설명
    if title:
        return Track.objects.filter(title__icontains=title)
    return Track.objects.all() # -> [schema.py] [models.py]

# @api.get("/test")
# def test(request):
#     return{'test': 'success'} # http://localhost:8000/api/test

@api.get("/tracks/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def track(request, track_id: int):
    try:
        track = Track.objects.get(pk=track_id)
        return 200, track
    except Track.DoesNotExist as e:
        return 404, {"message": "Track does not exist"}

@api.post(".tracks", response={201: TrackSchema})
def create_track(request, track: TrackSchema): # schema.py 설명
    track = Track.objects.create(**track.dict())
    return track

# 수정
@api.put("/tracks/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def change_track(request, track_id: int, data: TrackSchema):
    try:
        track = Track.objects.get(pk=track_id)
        for attribute, value in data.dict().items():
            setattr(track, attribute, value)
        track.save()
        return 200, track
    except Track.DoesNotExist as e:
        return 404, {"message": "Track does not exist"}

# 삭제
@api.delete("/tracks/{track_id}", response={200: None, 404: NotFoundSchema})
def delete_track(request, track_id: int, data: TrackSchema):
    try:
        track = Track.objects.get(pk=track_id)
        track.delete()
        return 200
    except Track.DoesNotExist as e:
        return 404, {"message": "Track does not exist"}

@api.post("/upload", url_name='upload') # index.html
def upload(request, file: UploadedFile = File(...)):
    data = file.read().decode()
    return {
        'name' : file.name,
        'data' : data
    }












