from fastapi import APIRouter


router = APIRouter(tags=['Example'])


@router.get('/hello')
def hello():
    return {'message': 'hello'}
