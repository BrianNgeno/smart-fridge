from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pusher

@api_view(['GET', 'POST'])
def realtime_notify(request):
    """
    generate notification from raspberry pi
        {
            status:FULL,
            item:milk
            action:BUY
        }
    """
    status = request.data['status']
    item = request.data['item']
    action = request.data['action']
    pusher_client = pusher.Pusher(
        app_id='636605',
        key='f102c43c7b54cf8ec7f9',
        secret='a63f00eb6377612e7d0c',
        cluster='ap2',
        ssl=True
    )
    '''
    event sent to pusher
    '''
    pusher_client.trigger('fridge-channel', 'buy-event', {
        'status':status,
        'item':item,
        'action':action
    })
    data = {
        'message':'success',
        'status_code':200
    }
   

    return Response(data)

