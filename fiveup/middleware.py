from fuauth.models import User


class ReferMiddleware():
    def process_request(self, request):
        uuid = request.GET.get("uuid")
        try:
            obj = User.objects.get(uuid=uuid)
        except:
            obj = None
        if obj:
            request.session['user_ref_id'] = obj.id
