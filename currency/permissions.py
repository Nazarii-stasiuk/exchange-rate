from rest_framework.permissions import BasePermission, SAFE_METHODS

CURREMCY_NAME = {
    'btc': 'Bitcoin',
    'eth': 'Etherium',
    'ltc': 'Litecoin',
    'xrp': 'Rippel',
}

class IsAvailable(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        data = request.data
        symbol = data.get('symbol', None)
        slug = False
        if symbol == 'btc':
            slug = request.user.is_bitcoin
        elif symbol == 'eth':
            slug = request.user.is_ethereum
        elif symbol == 'ltc':
            slug = request.user.is_litecoin
        elif symbol == 'xrp':
            slug = request.user.is_ripple
        
        return bool(request.user and request.user.is_authenticated and slug)

